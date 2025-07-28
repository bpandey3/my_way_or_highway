import ast, os

def find_dependencies(py_file):
    with open(py_file) as f:
        tree = ast.parse(f.read(), filename=py_file)

    imported_files = set()
    file_paths = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if os.path.exists(alias.name + ".py"):
                    imported_files.add(alias.name + ".py")

        elif isinstance(node, ast.ImportFrom):
            if node.module and os.path.exists(node.module.replace(".", "/") + ".py"):
                imported_files.add(node.module.replace(".", "/") + ".py")

        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "open":
                if isinstance(node.args[0], ast.Str):
                    file_paths.add(node.args[0].s)

    return imported_files, file_paths
