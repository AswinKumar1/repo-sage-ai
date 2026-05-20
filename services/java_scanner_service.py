import os
import re


def scan_java_controllers(repo_path):

    api_summary = []

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

                        if (
                            "@RestController" in content
                            or
                            "@Controller" in content
                        ):

                            endpoints = extract_endpoints(
                                content
                            )

                            api_summary.extend(
                                endpoints
                            )

                except:
                    pass

    return api_summary


def extract_endpoints(content):

    endpoints = []

    patterns = [

        r'@GetMapping\\(\"(.*?)\"\\)',
        r'@PostMapping\\(\"(.*?)\"\\)',
        r'@PutMapping\\(\"(.*?)\"\\)',
        r'@DeleteMapping\\(\"(.*?)\"\\)'
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            content
        )

        for match in matches:

            endpoints.append(match)

    return endpoints