import sys
import click
from ReadWriteDocument import DocumentReader


Docu = DocumentReader()


@click.command()
@click.option('--option', help="Enter an option u want to use. The possible commands are: quit, read, and search")
@click.option('--filename', help="Enter filename without filetype")
@click.option('--search', help="Enter the word you want to find (case-sensitive)")
def app():
    start()


@click.command()
@click.option('--option', prompt="What do you want to do (option)?")
def start(option):
    if option == "quit":
        sys.exit()
    elif option == "read":
        print_file()
    elif option == "search":
        search_in_file()

@click.command()
@click.option('--filename', prompt="In which file do you want to search? ")
def print_file(filename):
    click.echo(Docu.readfile(filename))

@click.command()
@click.option('--filename', prompt="In which file do you want to search? ")
@click.option('--search', prompt="What word do you want to find?")
def search_in_file(filename, search):
    click.echo(Docu.search(filename, search))



if __name__ == "__main__":
    start()
