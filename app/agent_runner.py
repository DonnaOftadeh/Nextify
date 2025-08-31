import asyncio
import json
import textwrap
from pathlib import Path

from agents_demo import PROMPTS as BASE_PROMPTS

ENTRY_PROMPTS = {
    "Idea": "The user has an idea for {company}: {product}. Start the multi-agent analysis.",
    "Industry": "The user knows the industry {product} and seeks an idea for a company like {company}. Start the analysis focusing on opportunities.",
    "Explore": "The user wants to explore the next breakthrough company in the {product} space, inspired by {company}. Begin by identifying promising angles.",
    "Improve": "The user wants to improve the product {product} by {company}. Analyze weaknesses and propose enhancements."
}


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


async def run_parallel_agents(company: str, product: str, mode: str = "Idea") -> dict:
    """Run all agents in parallel and prepend an entry message based on mode."""
    entry = ENTRY_PROMPTS.get(mode, ENTRY_PROMPTS["Idea"]).format(
        company=company, product=product
    )
    tasks = [
        _run_agent(name, prompt, company, product) for name, prompt in AGENT_PROMPTS.items()
    ]
    results = await asyncio.gather(*tasks)
    outputs = dict(zip(AGENT_PROMPTS.keys(), results))
    return {"entry": entry, **outputs}
