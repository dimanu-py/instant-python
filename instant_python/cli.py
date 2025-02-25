import typer

app = typer.Typer()


@app.command()
def generate_project():
    raise NotImplementedError("Not implemented yet")


if __name__ == "__main__":
    app()
