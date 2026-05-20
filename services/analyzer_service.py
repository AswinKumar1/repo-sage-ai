import os


# ==========================================
# COUNT FILES
# ==========================================

def count_files_and_folders(repo_path):

    total_files = 0
    total_folders = 0

    for root, dirs, files in os.walk(repo_path):

        total_files += len(files)
        total_folders += len(dirs)

    return {
        "total_files": total_files,
        "total_folders": total_folders
    }


# ==========================================
# EXTRACT REPOSITORY NAME
# ==========================================

def extract_repository_name(repo_path):

    return os.path.basename(repo_path)


# ==========================================
# DETECT BUILD TOOL
# ==========================================

def detect_build_tool(repo_path):

    files = os.listdir(repo_path)

    if "pom.xml" in files:
        return "Maven"

    elif "build.gradle" in files:
        return "Gradle"

    elif "package.json" in files:
        return "NPM"

    elif "requirements.txt" in files:
        return "Python Pip"

    return "Unknown"


# ==========================================
# DETECT API STYLE
# ==========================================

def detect_api_style(repo_path):

    graphql_keywords = [
        "graphql",
        "apollo",
        "type Query"
    ]

    rest_keywords = [
        "@RestController",
        "@RequestMapping",
        "express.Router",
        "fastapi"
    ]

    graphql_found = False
    rest_found = False

    for root, _, files in os.walk(repo_path):

        for file in files:

            if not file.endswith((
                ".java",
                ".js",
                ".ts",
                ".py",
                ".graphql"
            )):
                continue

            file_path = os.path.join(root, file)

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                    if any(
                        keyword in content
                        for keyword in graphql_keywords
                    ):
                        graphql_found = True

                    if any(
                        keyword in content
                        for keyword in rest_keywords
                    ):
                        rest_found = True

            except:
                pass

    if graphql_found:
        return "GraphQL"

    if rest_found:
        return "REST"

    return "Unknown"