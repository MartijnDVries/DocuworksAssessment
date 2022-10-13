import click
from ReadWriteDocument import DocumentReader


Docu = DocumentReader()

@click.command()
@click.option('--filename', default='text', prompt="Enter the name of the file")
def file_name(filename):
    click.echo(Docu.readfile(filename))


@click.command()
@click.option('--option', default="read", prompt="What do you want to do?")
def app(option):
    if option == "read":
        file_name()


if __name__ == "__main__":
    app()