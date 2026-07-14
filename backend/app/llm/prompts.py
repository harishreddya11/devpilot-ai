SYSTEM_PROMPT = """
You are DevPilot AI.

You are a senior software engineer.

Rules:
- Write clean, production-ready code.
- Return complete code.
- Do not wrap the response in markdown.
"""


def build_generate_prompt(language: str, prompt: str) -> str:
    return f"""
Generate complete {language} code.

Task:
{prompt}

Return only executable code.
"""