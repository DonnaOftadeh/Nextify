import textwrap

# Simple agent functions for demo purposes
# Each function takes user inputs and returns a placeholder response.

PROMPTS = {
    "refine": textwrap.dedent("""
        You are the Idea Refinement Agent.
        The user provided information about {company} and the product idea: {product}.
        Rewrite the idea clearly in one paragraph.
    """),
    "market": textwrap.dedent("""
        You are the Market Research Agent.
        Based on the refined idea of {product} for {company},
        provide a short summary of the target market and competitors.
    """),
    "features": textwrap.dedent("""
        You are the Feature Ideation Agent.
        Suggest three key features for the {product} by {company}.
    """),
    "roadmap": textwrap.dedent("""
        You are the Roadmap Agent.
        Draft a simple three-step roadmap for building {product} at {company}.
    """),
}


def idea_refinement(company: str, product: str) -> str:
    return PROMPTS["refine"].format(company=company, product=product)


def market_research(company: str, product: str) -> str:
    return PROMPTS["market"].format(company=company, product=product)


def feature_ideation(company: str, product: str) -> str:
    return PROMPTS["features"].format(company=company, product=product)


def roadmap_generation(company: str, product: str) -> str:
    return PROMPTS["roadmap"].format(company=company, product=product)


if __name__ == "__main__":
    company = input("Company name: ")
    product = input("Product idea: ")
    print("\n--- Idea Refinement ---")
    print(idea_refinement(company, product))
    print("\n--- Market Research ---")
    print(market_research(company, product))
    print("\n--- Feature Ideation ---")
    print(feature_ideation(company, product))
    print("\n--- Roadmap ---")
    print(roadmap_generation(company, product))
