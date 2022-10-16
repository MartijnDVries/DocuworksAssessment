import sys
import click
from ReadWriteDocument import DocumentReader


Docu = DocumentReader()


@click.command()
@click.option(
    '--option',
    prompt="What do you want to do (option)?",
    help="Possible commands are: quit, read, search, replace, email, common"
)
def start(option):
    option = option.lower()
    if option == "quit":
        sys.exit()
    elif option == "read":
        print_file()
    elif option == "search":
        search_in_file()
    elif option == "replace":
        replace_in_file()
    elif option == "email":
        find_email_in_file()
    elif option == "common":
        find_common_in_file()
    else:
        print("Command not recognized")
        start()

@click.command()
@click.option(
    '--filename',
    prompt="Which file do you want to read? ",
    help="Enter the name of the file without filetype"
)
def print_file(filename):
    """Open a textfile and show in commandline"""
    click.echo((Docu.readfile(filename)))
    start()

@click.command()
@click.option(
    '--filename',
    prompt="In which file do you want to search? ",
    help="Enter the name of the file without filetype"
)
@click.option(
    '--search',
    prompt="Wich word do you want to find?",
    help="Enter the word you want to find in the text"
)
def search_in_file(filename, search):
    """Search for a word in a textfile"""
    click.echo(Docu.search(filename, search))
    start()


@click.command()
@click.option(
    '--filename',
    prompt="In which file do you want to replace something?",
    help="Enter the name of the file without filetype"
)
@click.option(
    '--searchword',
    prompt="Enter the text you want to replace",
    help="The word which is going to be replaced in the text"
)
@click.option(
    '--replaceword',
    prompt="Enter the replacement text",
    help="The word(s) which are going to replace the searched word"
)
def replace_in_file(filename, searchword, replaceword):
    """Replace one word with another (word or string) in a textfile"""
    replaced_text = Docu.replace(filename, searchword, replaceword)
    click.echo(replaced_text)
    if replaced_text != f"'{searchword}' not found in '{filename}.txt', nothing to replace":
        choice_made = False
        while not choice_made:
            yes_no = input("Do you want to save this file?(y/n) ").lower()
            if yes_no == 'y':
                newfilename = input("Enter a filename: ")
                Docu.savefile(replaced_text, newfilename)
                click.echo("File saved!")
                choice_made = True
            elif yes_no == 'n':
                choice_made = True
    start()


@click.command()
@click.option(
    '--filename',
    prompt="In which file do you want to search? ",
    help="Enter the name of the file without filetype"
)
def find_email_in_file(filename):
    """Show a list of all email addresses in the file"""
    click.echo(Docu.find_email_address(filename))
    start()


@click.command()
@click.option(
    '--filename',
    prompt="In which file do you want to search? ",
    help="Enter the name of the file without filetype"
)
@click.option(
    '--listlimit',
    prompt="Enter the number of items you want to show",
    type=int,
    help="Enter a the number of words you want to show in a list"
)
def find_common_in_file(filename, listlimit):
    """Show a list of the most common words in a file with their counts, This list can be limited"""
    click.echo(Docu.common_word(filename, listlimit))
    start()


if __name__ == "__main__":
    start()
