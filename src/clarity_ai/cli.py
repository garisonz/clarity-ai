import typer


app = typer.Typer()


@app.command()
def review():
    """
    Review the codebase and provide feedback.
    """
    typer.echo("Reviewing")

@app.command()
def load():
    """
    Load the codebase and provide feedback.
    """
    typer.echo("Loading")
