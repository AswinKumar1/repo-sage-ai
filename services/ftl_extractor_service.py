import os
import re
import zipfile


def extract_ftl_context(repo_path):

    context = {

        "ftl_files": [],
        "variables": [],
        "graphql_operations": [],
        "field_mappings": [],
        "conditions": []
    }

    # ==========================================
    # SCAN REPOSITORY
    # ==========================================

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".ftl"):

                file_path = os.path.join(
                    root,
                    file
                )

                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        context[
                            "ftl_files"
                        ].append(file)

                        # ==========================
                        # VARIABLES
                        # ==========================

                        variables = re.findall(
                            r'\$\{(.*?)\}',
                            content
                        )

                        context[
                            "variables"
                        ].extend(variables)

                        # ==========================
                        # GRAPHQL OPERATIONS
                        # ==========================

                        operations = re.findall(
                            r'(mutation|query)\s+(\w+)',
                            content
                        )

                        for op in operations:

                            context[
                                "graphql_operations"
                            ].append(op[1])

                        # ==========================
                        # FIELD MAPPINGS
                        # ==========================

                        mappings = re.findall(
                            r'"(.*?)"\s*:\s*"\$\{(.*?)\}"',
                            content
                        )

                        for mapping in mappings:

                            context[
                                "field_mappings"
                            ].append(
                                f"{mapping[1]} -> {mapping[0]}"
                            )

                        # ==========================
                        # CONDITIONS
                        # ==========================

                        conditions = re.findall(
                            r'<#if\s+(.*?)>',
                            content
                        )

                        context[
                            "conditions"
                        ].extend(conditions)

                except Exception as e:

                    print(
                        f"Failed to read {file}: {e}"
                    )

    # ==========================================
    # REMOVE DUPLICATES
    # ==========================================

    for key in context:

        context[key] = list(
            set(context[key])
        )

    return context