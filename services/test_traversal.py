from traversal_service import (
    traverse_repository
)

repo_path = "YOUR_REPO_PATH"

context = traverse_repository(repo_path)

print("\n==============================")
print("REPOSITORY TRAVERSAL OUTPUT")
print("==============================\n")


# ==========================================
# CONTROLLERS
# ==========================================

print("CONTROLLERS")
print("------------------------------")

for controller in context["controllers"]:
    print(f"• {controller}")

print()


# ==========================================
# IMPORTS
# ==========================================

print("IMPORTS")
print("------------------------------")

for imp in context["imports"]:
    print(f"• {imp}")

print()


# ==========================================
# UTILITY CLASSES
# ==========================================

print("UTILITY CLASSES")
print("------------------------------")

for cls in context["utility_classes"]:
    print(f"• {cls}")

print()


# ==========================================
# METHOD CALLS
# ==========================================

print("METHOD CALLS")
print("------------------------------")

for method in context["method_calls"]:
    print(f"• {method}")

print()


# ==========================================
# WORKFLOW OBJECTS
# ==========================================

print("WORKFLOW OBJECTS")
print("------------------------------")

for workflow in context["workflow_objects"]:
    print(f"• {workflow}")

print()