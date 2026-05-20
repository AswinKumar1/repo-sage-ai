import os
import re



def extract_endpoint_details(repo_path):

    endpoints = []

    for root, _, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".java"):

                file_path = os.path.join(root, file)

                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        # =====================================
                        # CONTROLLER CHECK
                        # =====================================

                        if (
                            "@RestController" in content
                            or "@Controller" in content
                        ):

                            # =====================================
                            # FIND POST MAPPINGS
                            # =====================================

                            post_matches = re.findall(
                                r'@PostMapping\("([^"]+)"\)',
                                content
                            )

                            for endpoint in post_matches:

                                endpoints.append({
                                    "method": "POST",
                                    "path": endpoint
                                })

                            # =====================================
                            # FIND GET MAPPINGS
                            # =====================================

                            get_matches = re.findall(
                                r'@GetMapping\("([^"]+)"\)',
                                content
                            )

                            for endpoint in get_matches:

                                endpoints.append({
                                    "method": "GET",
                                    "path": endpoint
                                })

                            # =====================================
                            # FIND PUT MAPPINGS
                            # =====================================

                            put_matches = re.findall(
                                r'@PutMapping\("([^"]+)"\)',
                                content
                            )

                            for endpoint in put_matches:

                                endpoints.append({
                                    "method": "PUT",
                                    "path": endpoint
                                })

                            # =====================================
                            # FIND DELETE MAPPINGS
                            # =====================================

                            delete_matches = re.findall(
                                r'@DeleteMapping\("([^"]+)"\)',
                                content
                            )

                            for endpoint in delete_matches:

                                endpoints.append({
                                    "method": "DELETE",
                                    "path": endpoint
                                })

                except Exception:
                    pass

    return endpoints



def traverse_repository(repo_path):

    traversal_context = {

        "controllers": [],
        "imports": [],
        "utility_classes": [],
        "method_calls": [],
        "workflow_objects": []
    }

    # ==========================================
    # WALK THROUGH REPOSITORY
    # ==========================================

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".java"):

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

                        # ==================================
                        # DETECT CONTROLLERS
                        # ==================================

                        if (
                            "@RestController" in content
                            or
                            "@Controller" in content
                        ):

                            traversal_context[
                                "controllers"
                            ].append(file)

                        # ==================================
                        # EXTRACT IMPORTS
                        # ==================================

                        imports = re.findall(
                            r'import\s+([\w\.]+);',
                            content
                        )

                        traversal_context[
                            "imports"
                        ].extend(imports)

                        # ==================================
                        # FIND NEW CLASS INSTANTIATIONS
                        # Example:
                        # new GQLActionController(...)
                        # ==================================

                        new_objects = re.findall(
                            r'new\s+(\w+)\(',
                            content
                        )

                        traversal_context[
                            "utility_classes"
                        ].extend(new_objects)

                        # ==================================
                        # METHOD CALLS
                        # Example:
                        # execute(
                        # validate(
                        # ==================================

                        methods = re.findall(
                            r'\.(\w+)\(',
                            content
                        )

                        traversal_context[
                            "method_calls"
                        ].extend(methods)

                        # ==================================
                        # WORKFLOW OBJECTS
                        # Example:
                        # accountsWorkflowCommand
                        # ==================================

                        workflow_objects = re.findall(
                            r'(\w+Workflow\w*)',
                            content
                        )

                        traversal_context[
                            "workflow_objects"
                        ].extend(workflow_objects)

                except Exception as e:

                    print(
                        f"Failed to scan {file}: {e}"
                    )

    # ==========================================
    # REMOVE DUPLICATES
    # ==========================================

    for key in traversal_context:

        traversal_context[key] = list(
            set(traversal_context[key])
        )

    return traversal_context