import typer

app = typer.Typer(help="Manage bot users", no_args_is_help=True)


@app.command(
    name="list",
    help="List users telegrams ids",
)
def list():
    typer.echo("Listing users...")


@app.command(
    name="add",
    help="Add user",
)
def add(
    name: str,
):
    typer.echo(f"Adding user {name}...")
