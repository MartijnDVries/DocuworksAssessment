import sys
import click
from ReadWriteDocument import DocumentReader


Docu = DocumentReader()


# @click.option('--option', help="Enter an option u want to use. The possible commands are: quit, read, and search")
# @click.option('--filename', help="Enter filename without filetype")
# @click.option('--search', help="Enter the word you want to find (case-sensitive)")


@click.command()
@click.option('--option', prompt="What do you want to do (option)?", help="Possible commands are: quit, read, search, replace, email, common, secret")
def start(option):
    if option == "quit":
        sys.exit()
    elif option == "read":
        print_file()
    elif option == "search":
        search_in_file()
    elif option == "replace":
        replace_in_file()
    else:
        print("command not recognized")
        start()

@click.command()
@click.option('--filename', prompt="Which file do you want to read? ")
def print_file(filename):
    click.echo(Docu.readfile(filename))
    start()

@click.command()
@click.option('--filename', prompt="In which file do you want to search? ")
@click.option('--search', prompt="What word do you want to find?")
def search_in_file(filename, search):
    click.echo(Docu.search(filename, search))
    start()


@click.command()
@click.option('--filename', prompt="In which file do you want to replace something?")
@click.option('--searchword', prompt="Enter the text you want to replace")
@click.option('--replaceword', prompt="Enter the replacement text")
def replace_in_file(filename, searchword, replaceword):
    replaced_text = Docu.replace(filename, searchword, replaceword)
    click.echo(replaced_text)
    choice_made = False
    while not choice_made:
        yes_no = input("Do you want to save this file?(y/n) ").lower()
        if yes_no == 'y':
            newfilename = input("Enter a filename: ")
            Docu.savefile(replaced_text, newfilename)
            click.echo("File saved!")
            start()
        elif yes_no == 'n':
            start()
        else: continue


def main():
    start()


if __name__ == "__main__":
    main()
