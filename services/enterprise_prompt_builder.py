def build_enterprise_prompt(
    traversal_context,
    ftl_context,
    technologies,
    endpoint_details
):
    
    formatted_endpoints = "\n".join(
    [
        f"{e['method']} {e['path']}"
        for e in endpoint_details
    ]
)

    prompt = f"""
You are an enterprise QA automation architect.

Analyze the following Spring Boot banking application context
and generate enterprise-grade test cases.

==================================================
APPLICATION ARCHITECTURE
==================================================

This application follows:

- Workflow-driven architecture
- POST-based orchestration APIs
- Hasura GraphQL persistence
- FTL-based payload transformation
- Utility-driven execution model
- Enterprise approval workflows
- Entitlement validation model

DO NOT assume traditional CRUD APIs.

==================================================
STRICT RULES
==================================================

1. ONLY generate test cases for detected endpoints
2. DO NOT invent APIs
3. DO NOT assume GET/PUT/DELETE APIs unless detected
4. DO NOT assume CRUD architecture
5. APIs are orchestration-based workflow APIs
6. Persistence happens through Hasura GraphQL
7. Generate ONLY repository-relevant test cases

==================================================
TECH STACK
==================================================

{technologies}

==================================================
DETECTED ENDPOINTS
==================================================

{formatted_endpoints}

==================================================
CONTROLLERS
==================================================

{traversal_context.get("controllers", [])}

==================================================
UTILITY CLASSES
==================================================

{traversal_context.get("utility_classes", [])}


==================================================
WORKFLOW OBJECTS
==================================================

{traversal_context.get("workflow_objects", [])}

==================================================
GRAPHQL OPERATIONS
==================================================

{ftl_context.get("graphql_operations", [])}

==================================================
FTL VARIABLES
==================================================

{ftl_context.get("variables", [])[:5]}

==================================================

Generate:

1. Functional Test Cases
2. Negative Test Cases
3. Edge Cases
4. Workflow Validation Tests
5. Entitlement Validation Tests
6. GraphQL Validation Tests
7. Payload Transformation Tests
8. Approval Flow Test Cases

IMPORTANT:
- Generate tests ONLY for detected endpoints
- Do NOT create imaginary APIs
- Use actual workflow terminology from the repository
- Respect orchestration architecture
- Respect Hasura-driven persistence architecture

OUTPUT FORMAT:

For every endpoint generate:

- Functional Tests
- Negative Tests
- Workflow Tests
- Entitlement Tests
- Payload Transformation Tests

Do NOT generate generic banking CRUD APIs.

Return the output in clean markdown format.

"""

    return prompt