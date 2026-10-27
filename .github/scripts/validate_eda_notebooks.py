"""Validate and execute the tracked EDA notebooks against their committed CSVs.

This checks notebook JSON and runs every cell in a fresh kernel. It does not assert
that a descriptive finding is causal; numeric findings still need business review.
"""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

NOTEBOOKS = [
    Path("Amazone-sales/Amazon Sale Report.ipynb"),
    Path("project-1/Diwali_Sales_Analysis (1).ipynb"),
]


def main():
    for path in NOTEBOOKS:
        notebook = nbformat.read(path, as_version=4)
        client = NotebookClient(
            notebook,
            timeout=300,
            kernel_name="python3",
            resources={"metadata": {"path": str(path.parent.resolve())}},
            allow_errors=False,
        )
        client.execute()
        code_cells = sum(cell.cell_type == "code" for cell in notebook.cells)
        print(f"Executed {path}: {code_cells} code cells passed")
    print("EDA notebook execution checks passed.")


if __name__ == "__main__":
    main()
