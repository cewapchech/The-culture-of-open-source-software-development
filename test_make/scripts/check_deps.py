import ast
import os
import sys

def get_imports_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=filepath)
    
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def get_requirements():
    reqs = set()
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    pkg = line.split('==')[0].split('>=')[0].split('[')[0].strip().lower()
                    reqs.add(pkg)
    return reqs

def main():
    src_dir = 'src'
    all_imports = set()
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                all_imports.update(get_imports_from_file(filepath))
    
    requirements = get_requirements()
    
    missing = []
    for imp in all_imports:
        stdlib = {'os', 'sys', 'ast', 'typing', 'json', 'pathlib'}
        if imp.lower() not in stdlib and imp.lower() not in requirements:
            missing.append(imp)
            
    if missing:
        print(f"ОШИБКА: Следующие импорты не найдены в requirements.txt: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("Все импорты корректно указаны в requirements.txt.")
        sys.exit(0)

if __name__ == "__main__":
    main()