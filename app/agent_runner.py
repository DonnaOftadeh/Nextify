import asyncio
import json
import textwrap
from pathlib import Path

from agents_demo import PROMPTS as BASE_PROMPTS


def load_prompts():
    """Load built-in prompts plus agent names from JSON."""
    json_path = Path(__file__).resolve().parents[1] / "prompts" / "nextive_individual_agents_flat.json"
    extra_prompts = {}
    try:
        with json_path.open() as f:
            data = json.load(f)
        for name in data.get("results", {}).keys():
            extra_prompts[name] = textwrap.dedent(
                f"""
                You are the {name} agent.
                Analyze the product '{{product}}' by '{{company}}'.
                """
            )
    except FileNotFoundError:
        pass
    return {**BASE_PROMPTS, **extra_prompts}

AGENT_PROMPTS = load_prompts()


async def _run_agent(name: str, prompt: str, company: str, product: str) -> str:
    await asyncio.sleep(0.1)
    return prompt.format(company=company, product=product)


async def run_parallel_agents(company: str, product: str) -> dict:
    tasks = [_run_agent(name, prompt, company, product) for name, prompt in AGENT_PROMPTS.items()]
    results = await asyncio.gather(*tasks)
    return dict(zip(AGENT_PROMPTS.keys(), results))
