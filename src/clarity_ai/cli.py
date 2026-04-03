from typing import Annotated
from rich import print
from pathlib import Path

import typer

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

app = typer.Typer()

@app.command()
def review(files: list[Path]):
    for path in files:
        if path.is_file():
            print(f"This file exists: {path.name}")

if __name__ == "__main__":
    app()

@app.command()
def check():
    print("Checking data:")
    print(data)