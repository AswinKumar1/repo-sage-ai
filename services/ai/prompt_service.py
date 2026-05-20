def build_testcase_prompt(api_summary):

    endpoints_text = "\\n".join(api_summary)

    prompt = f"""
    You are a senior QA engineer
    for enterprise banking systems.

    Generate:
    1. Functional test cases
    2. Edge cases
    3. Negative scenarios
    4. Risk analysis

    APIs:
    {endpoints_text}

    Output in markdown format.
    """

    return prompt