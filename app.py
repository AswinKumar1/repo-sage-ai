import streamlit as st
from services.git_service import get_remote_branches
from services.repository_service import clone_repository, validate_local_repository
from services.scanner_service import build_tree
from services.detector_service import detect_technologies

from services.analyzer_service import (
    count_files_and_folders,
    extract_repository_name,
    detect_build_tool,
    detect_api_style
)

from services.enterprise_prompt_builder import (
    build_enterprise_prompt
)


from services.ftl_extractor_service import (
    extract_ftl_context
)

from services.traversal_service import (
    traverse_repository,
    extract_endpoint_details
)

from services.java_scanner_service import (
    scan_java_controllers
)

from services.ai.prompt_service import (
    build_testcase_prompt
)

from services.ai.openrouter_service import (
    generate_test_cases
)


st.set_page_config(page_title="RepoSage AI", layout="wide")

if "repo_loaded" not in st.session_state:
    st.session_state["repo_loaded"] = False

st.title("RepoSage AI")
st.caption("AI-Powered Repository Intelligence Platform")

st.markdown("---")


def show_repository_input():
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown(
            """<style>

            .main {
                background-color: #0E1117;
            }

            .tree-node {
                color: white !important;
            }

            li[role="treeitem"] span {
                color: white !important;
            }

            </style>""",
            unsafe_allow_html=True,
        )

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
            "<div class='section-title'>📂 Repository Input</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            Provide either:
            - Git repository URL
            - Local repository path
            """
        )

        git_tab, local_tab = st.tabs(["Git Repository", "Local Repository"])

        # GIT TAB
        with git_tab:
            repo_url = st.text_input(
                "Git Repository URL", placeholder="https://github.com/org/repo.git"
            )

            fetch_button = st.button("Fetch Branches", use_container_width=True)

            if fetch_button:
                if not repo_url:
                    st.error("Please provide repository URL")
                else:
                    with st.spinner("Fetching branches..."):
                        try:
                            branches = get_remote_branches(repo_url)
                            st.session_state["repo_source"] = "git"
                            st.session_state["repo_url"] = repo_url
                            st.session_state["branches"] = branches
                            st.success("Branches fetched successfully")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            if "branches" in st.session_state:
                selected_branch = st.selectbox(
                    "Select Branch", st.session_state["branches"]
                )
                st.session_state["selected_branch"] = selected_branch

                load_repo_button = st.button("Load Repository", use_container_width=True)
                if load_repo_button:
                    with st.spinner("Cloning repository..."):
                        try:
                            repo_path = clone_repository(
                                st.session_state["repo_url"], selected_branch
                            )
                            st.session_state["repo_path"] = repo_path
                            folder_tree = build_tree(repo_path)
                            st.session_state["folder_tree"] = folder_tree
                            technologies = detect_technologies(repo_path)
                            st.session_state["technologies"] = technologies
                            repo_stats = count_files_and_folders(
                            repo_path
                            )
                            st.session_state["repo_stats"] = repo_stats
                            repo_name = extract_repository_name(
                                repo_path
                            )
                            st.session_state["repo_name"] = repo_name
                            build_tool = detect_build_tool(
                                repo_path
                            )
                            st.session_state["build_tool"] = build_tool
                            api_style = detect_api_style(
                                repo_path
                            )
                            st.session_state["api_style"] = api_style
                            st.session_state["repo_loaded"] = True
                            st.success("Repository loaded successfully")
                        except Exception as e:
                            st.error(str(e))

        # LOCAL TAB
        with local_tab:
            local_path = st.text_input(
                "Local Repository Path", placeholder="C:/Projects/payment-service"
            )

            local_button = st.button("Use Local Repository", use_container_width=True)
            if local_button:
                if not local_path:
                    st.error("Please provide local path")
                else:
                    try:
                        repo_path = validate_local_repository(local_path)
                        st.session_state["repo_source"] = "local"
                        st.session_state["local_path"] = local_path
                        st.session_state["repo_path"] = repo_path
                        folder_tree = build_tree(repo_path)
                        st.session_state["folder_tree"] = folder_tree
                        technologies = detect_technologies(repo_path)
                        st.session_state["technologies"] = technologies
                        repo_stats = count_files_and_folders(
                            repo_path
                        )

                        st.session_state["repo_stats"] = repo_stats
                        repo_name = extract_repository_name(
                            repo_path
                        )
                        st.session_state["repo_name"] = repo_name
                        build_tool = detect_build_tool(
                            repo_path
                        )

                        st.session_state["build_tool"] = build_tool
                        api_style = detect_api_style(
                            repo_path
                        )

                        st.session_state["api_style"] = api_style
                        st.session_state["repo_loaded"] = True
                        st.success("Local repository loaded successfully")
                        st.code(local_path)
                    except Exception as e:
                        st.error(str(e))

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            "<div class='section-title'>🚀 About RepoSage AI</div>", unsafe_allow_html=True
        )

        st.markdown(
            """
            RepoSage AI is an AI-powered repository intelligence platform
            designed to accelerate SDLC understanding and engineering productivity.

            The platform analyzes repositories and automatically generates
            engineering artifacts such as:

            ### 🤖 AI Generated Outputs
            - Functional Test Cases
            - Edge Cases
            - Risk Analysis
            - Architecture Summary
            - README Documentation
            - API Discovery

            ### ⚡ Core Capabilities
            - Repository Analysis
            - Branch-Aware Processing
            - Technology Detection
            - Framework Identification
            - AI-Powered SDLC Acceleration

            ### 🛠 Supported Inputs
            - Git Repositories
            - Local Repository Paths

            ### 🎯 Target Users
            - QA Engineers
            - Developers
            - DevOps Teams
            - Architects
            - Engineering Leads
            """,
        )

        st.markdown("---")
        st.markdown("### 🔄 Workflow")
        st.code(
            """
        Input Repository
                ↓
        Repository Scan
                ↓
        Technology Detection
                ↓
        AI Analysis
                ↓
        Artifact Generation
            """
        )


def show_workspace():
    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col1:
        st.subheader("📁 Repository Explorer")

        def render_tree(nodes, level=0):
            for node in nodes:
                label = node.get("label", "")
                children = node.get("children", [])

                if children:
                    with st.expander(label, expanded=False):
                        render_tree(children, level + 1)
                else:
                    st.markdown(
                        f"{'&nbsp;' * (level * 4)}📄 {label.replace('📄 ', '')}",
                        unsafe_allow_html=True,
                    )

        render_tree(st.session_state.get("folder_tree", []))

    # ==========================================
    # COLUMN 2 — AI WORKSPACE
    # ==========================================

    with col2:

        st.subheader("🤖 Repository Traversal")

        if st.button(
            "Analyze FTL Context",
            use_container_width=True
        ):
        
            with st.spinner(
                "Analyzing FTL templates..."
            ):

                try:

                    repo_path = st.session_state[
                        "repo_path"
                    ]

                    ftl_context = extract_ftl_context(
                        repo_path
                    )

                    # ======================================
                    # FTL FILES
                    # ======================================

                    st.markdown("## FTL Files")

                    for file in ftl_context[
                        "ftl_files"
                    ]:

                        st.success(file)

                    # ======================================
                    # VARIABLES
                    # ======================================

                    st.markdown("## Variables")

                    for variable in ftl_context[
                        "variables"
                    ]:

                        st.code(variable)

                    # ======================================
                    # GRAPHQL OPERATIONS
                    # ======================================

                    st.markdown(
                        "## GraphQL Operations"
                    )

                    for operation in ftl_context[
                        "graphql_operations"
                    ]:

                        st.info(operation)

                    # ======================================
                    # FIELD MAPPINGS
                    # ======================================

                    st.markdown("## Field Mappings")

                    for mapping in ftl_context[
                        "field_mappings"
                    ]:

                        st.text(mapping)

                    # ======================================
                    # CONDITIONS
                    # ======================================

                    st.markdown("## Conditions")

                    for condition in ftl_context[
                        "conditions"
                    ]:

                        st.warning(condition)

                except Exception as e:

                    st.error(str(e))
            

        if st.button(
            "Analyze Repository Traversal",
            use_container_width=True
        ):
        

            with st.spinner(
                "Traversing repository..."
            ):

                try:

                    repo_path = st.session_state[
                        "repo_path"
                    ]

                    traversal_context = traverse_repository(
                        repo_path
                    )

                    # ======================================
                    # CONTROLLERS
                    # ======================================

                    st.markdown("## Controllers")

                    for controller in traversal_context[
                        "controllers"
                    ]:

                        st.success(controller)

                    # ======================================
                    # IMPORTS
                    # ======================================

                    st.markdown("## Imports")

                    for imp in traversal_context[
                        "imports"
                    ]:

                        st.code(imp)

                    # ======================================
                    # UTILITY CLASSES
                    # ======================================

                    st.markdown("## Utility Classes")

                    for cls in traversal_context[
                        "utility_classes"
                    ]:

                        st.info(cls)

                    # ======================================
                    # METHOD CALLS
                    # ======================================

                    st.markdown("## Method Calls")

                    for method in traversal_context[
                        "method_calls"
                    ]:

                        st.text(method)

                    # ======================================
                    # WORKFLOW OBJECTS
                    # ======================================

                    st.markdown("## Workflow Objects")

                    for workflow in traversal_context[
                        "workflow_objects"
                    ]:

                        st.warning(workflow)

                except Exception as e:

                    st.error(str(e))

        st.subheader("🤖 AI Workspace")

        st.info(
            "AI-generated test cases will appear here."
        )

        if st.button(
            "Generate Test Cases",
            use_container_width=True
        ):

            with st.spinner(
                "Analyzing Spring Boot APIs..."
            ):

                try:

                    repo_path = st.session_state[
                        "repo_path"
                    ]

                    # ======================================
                    # TRAVERSAL CONTEXT
                    # ======================================

                    traversal_context = traverse_repository(
                        repo_path
                    )

                    # ======================================
                    # End Point Details
                    # ======================================

                    endpointDetails = extract_endpoint_details(
                        repo_path
                    )

                    # ======================================
                    # FTL CONTEXT
                    # ======================================

                    ftl_context = extract_ftl_context(
                        repo_path
                    )

                    # ======================================
                    # TECHNOLOGIES
                    # ======================================

                    technologies = st.session_state.get(
                        "technologies",
                        {}
                    )

                    # ======================================
                    # BUILD ENTERPRISE PROMPT
                    # ======================================

                    prompt = build_enterprise_prompt(
                        traversal_context,
                        ftl_context,
                        technologies,
                        endpointDetails
                    )

                    # OPTIONAL DEBUG
                    # st.code(prompt)

                    # ======================================
                    # GENERATE TEST CASES
                    # ======================================

                    result = generate_test_cases(
                        prompt
                    )

                    with st.expander(
                        "📋 Generated Test Cases",
                        expanded=False
                    ):

                        st.markdown(result)

                except Exception as e:

                    st.error(str(e))
    with col3:
        st.subheader("📊 Repository Insights")
        technologies = st.session_state.get("technologies", {})

        for category, techs in technologies.items():
            st.markdown(f"### {category.title()}")
            if techs:
                for tech in techs:
                    st.success(tech)
            else:
                st.caption("Not Detected")


if not st.session_state["repo_loaded"]:
    show_repository_input()
else:
    show_workspace()
