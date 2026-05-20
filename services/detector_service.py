import os
import json


def detect_technologies(repo_path):

    detected = {
        "backend": [],
        "frontend": [],
        "api": [],
        "database": []
    }

    for root, dirs, files in os.walk(repo_path):

        angular_json_path = os.path.join(
            repo_path,
            "angular.json"
        )

        if os.path.exists(angular_json_path):
            detected["frontend"].append("Angular")

        # ==========================================
        # NODE / REACT
        # ==========================================

        if "package.json" in files:

            package_json_path = os.path.join(
                root,
                "package.json"
            )

            try:

                with open(package_json_path, "r") as f:

                    package_data = json.load(f)

                    dependencies = {
                        **package_data.get("dependencies", {}),
                        **package_data.get("devDependencies", {})
                    }

                    if ("react" in dependencies and "react-dom" in dependencies and "Angular" not in detected["frontend"]):
                        detected["frontend"].append("React")

                    if ("express" in dependencies and "Angular" not in detected["frontend"]):
                        detected["backend"].append("Express.js")

                    if "apollo-server" in dependencies:
                        detected["api"].append("GraphQL")

            except:
                pass

        # ==========================================
        # PYTHON
        # ==========================================

        if "requirements.txt" in files:

            requirements_path = os.path.join(
                root,
                "requirements.txt"
            )

            try:

                with open(requirements_path, "r") as f:

                    content = f.read().lower()

                    if "flask" in content:
                        detected["backend"].append("Flask")

                    if "fastapi" in content:
                        detected["backend"].append("FastAPI")

            except:
                pass

        # ==========================================
        # JAVA
        # ==========================================

        if "pom.xml" in files:
            detected["backend"].append("Spring Boot")

        # ==========================================
        # GRAPHQL FILES
        # ==========================================

        for file in files:

            if file.endswith(".graphql"):
                detected["api"].append("GraphQL")

    # Remove duplicates

    for key in detected:
        detected[key] = list(set(detected[key]))

    return detected