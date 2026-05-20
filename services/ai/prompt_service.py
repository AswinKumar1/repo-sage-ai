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

# def build_testcase_prompt(api_summary):

#     endpoints_text = "\n".join(api_summary)

#     prompt = f"""
# You are a senior QA engineer specializing in enterprise banking systems.

# Your task is to generate comprehensive FUNCTIONAL TEST SCENARIOS based on the given APIs.

# Focus on REAL-WORLD USER FLOWS, not just isolated API testing.

# ---

# ### REQUIREMENTS

# 1. Cover end-to-end functional scenarios such as:
#    - User authentication and session handling
#    - Account operations (view, update)
#    - Transactions (transfer, deposit, withdrawal)
#    - Error handling and rollback scenarios

# 2. Each scenario MUST:
#    - Involve realistic user behavior
#    - Combine multiple APIs where applicable
#    - Reflect real banking use cases

# 3. Include the following categories:
#    - Functional test cases (primary flows)
#    - Edge cases (boundary conditions, limits)
#    - Negative scenarios (invalid inputs, failures, unauthorized access)
#    - Risk analysis (security, data integrity, concurrency, financial risks)

# ---

# ### OUTPUT FORMAT (STRICT MARKDOWN)

# For each test case, use:

# #### Test Case ID: <ID>
# **Scenario:** <High-level user scenario>

# **Preconditions:**
# - ...

# **Steps:**
# 1. ...
# 2. ...

# **Expected Result:**
# - ...

# **Type:** Functional | Edge | Negative

# ---

# ### ADDITIONAL DEPTH

# - Include concurrency issues (e.g., double transactions)
# - Include validation failures (invalid formats, missing fields)
# - Include security risks (auth bypass, data leakage)
# - Include state-based issues (invalid account state)

# ---

# ### APIs
# {endpoints_text}

# ---

# Generate at least:
# - 10 functional scenarios
# - 5 edge cases
# - 5 negative scenarios

# Avoid generic or obvious test cases. Prioritize realistic and high-impact banking scenarios.
# """

#     return prompt