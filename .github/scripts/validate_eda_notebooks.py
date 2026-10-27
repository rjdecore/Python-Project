"""Validate the tracked EDA notebooks' JSON and Python cell syntax.

This is a static check; it does not execute analysis cells or verify numeric findings.
"""
import json
from pathlib import Path

NOTEBOOKS = [
    Path("Amazone-sales/Amazon Sale Report.ipynb"),
    Path("project-1/Diwali_Sales_Analysis (1).ipynb"),
]


def clean_cell(source):
    lines = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("%", "!")):
            continue
        if "get_ipython().run_line_magic" in stripped or "get_ipython().system" in stripped:
            continue
        lines.append(line)
    return "\n".join(lines)


def main():
    for path in NOTEBOOKS:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        code_count = 0
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            source = clean_cell(source)
            if not source.strip():
                continue
            try:
                compile(source, f"{path}:cell-{index}", "exec")
            except SyntaxError as exc:
                raise SyntaxError(
                    f"{path}, cell {index}: {exc.msg} at line {exc.lineno}"
                ) from exc
            code_count += 1
        print(f"Validated {path}: {code_count} Python code cells")
    print("Notebook JSON and targeted EDA cell syntax checks passed.")
    

if __name__ == "__main__":
    main()
