import os


IGNORED_FOLDERS = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__",
    "coverage",
    "venv",
    ".idea",
    ".vscode",
    "target"
}

IGNORED_FILES = {
    ".DS_Store"
}

IGNORED_EXTENSIONS = {
    ".class",
    ".pyc",
    ".log"
}


def build_tree(path):

    tree = []

    for item in sorted(os.listdir(path)):

        item_path = os.path.join(path, item)

        # ==========================================
        # IGNORE FILES/FOLDERS
        # ==========================================

        if item in IGNORED_FOLDERS:
            continue

        if item in IGNORED_FILES:
            continue

        if any(
            item.endswith(ext)
            for ext in IGNORED_EXTENSIONS
        ):
            continue

        # ==========================================
        # DIRECTORY
        # ==========================================

        if os.path.isdir(item_path):

            tree.append({
                "label": f"📁 {item}",
                "value": item_path,
                "children": build_tree(item_path)
            })

        # ==========================================
        # FILE
        # ==========================================

        else:

            tree.append({
                "label": f"📄 {item}",
                "value": item_path
            })

    return tree