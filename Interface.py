import sys
import click
from ReadWriteDocument import DocumentReader


Docu = DocumentReader()


@click.group(help="yo")
@click.option('--filename', prompt="In which file do you want to search? ", help="Enter filename without filetype")
@click.option('--search', prompt="Which word do you wint to find? ", help="Enter the word you want to search in the text (Case-sensitive)")
def app():
    app()

@app.command()
def print_file(filename):
    click.echo(Docu.readfile(filename))

@app.command()
def search_in_file(filename, search):
    click.echo(Docu.search(filename, search))


@cli.command()
@click.option('--option', prompt="What do you want to do?")
def app(option):
    if option == "quit":
        sys.exit()
    elif option == "read":
        print_file()
    elif option == "search":
        search_in_file()




if __name__ == "__main__":
    cli()