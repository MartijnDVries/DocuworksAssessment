import os
import re
from ErrorCases import NoPalindromeError, NoEmailAddressesError

class DocumentReader:

    def __init__(self):
        self.path = os.getcwd()+"\\TextFiles\\"

    def readfile(self, file : str) -> str:
        """Open the file and return the text of this file"""
        try:
            with open(f"{self.path}{file}.txt", 'r') as f:
                txt = f.read()
            return txt.strip()
        except FileNotFoundError:
            return "File not found"

    def savefile(self, file : str, file_name : str):
        """Save text file with chosen filename"""
        with open(f"{self.path}{file_name}.txt", 'w') as f:
            f.write(file)

    def search(self, file: str, search : str) -> str:
        """Search for a word in the text and return the index/indices in a list"""
        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        search_list = [word.span() for word in re.finditer(search, txt.strip())]
        if search_list:
            return f"Found '{search}' on the following positions: \n{str(search_list)}"

        return f"'{search}' not found in {file}.txt"

    def replace(self, file: str, search: str, replace: str) -> str:
        """replace all occurrences of a word in a textfile with another word"""

        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        if not [word for word in re.finditer(search, txt.strip())]:
            return f"'{search}' not found in '{file}.txt', nothing to replace"

        return re.sub(fr"\b{search}\b", replace, txt.strip())

    def common_word(self, file: str, limit: int = None) -> str:
        """Find the most common word in a textfile"""
        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        word_list = txt.split()
        full_list = self.find_common_word(word_list)
        limited_sorted_list = sorted(full_list, key=lambda tup: tup[1], reverse=True)
        if limit is None \
                or limit > len(limited_sorted_list):
            limit = len(limited_sorted_list)
        return str(limited_sorted_list[:limit])

    def find_common_word(self, word_list : list, count_list: list = None) -> list:
        """Continues common_word function"""
        if count_list is None:
            count_list = list()

        if len(word_list) == 0:
            return count_list

        if all(word == word_list[0] for word in word_list):
            word = word_list[0]
            count = word_list.count(word)
            count_list.append((word, count))
            return count_list

        word = word_list[0]
        count = word_list.count(word)
        count_list.append((word, count))
        word_list = [remaining_word for remaining_word in word_list if remaining_word != word]
        return self.find_common_word(word_list, count_list)

    def palindromes(self, file: str) -> str:
        """Find all palindromes in a text file and return in a list"""
        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        word_list = txt.split()
        palindrome_list = self.find_palindromes(word_list)
        if not palindrome_list:
            raise NoPalindromeError
        return str(palindrome_list)

    def find_palindromes(self, word_list: list, palindromes_list: list = None) -> list:
        """Continues palindromes function"""
        if palindromes_list is None:
            palindromes_list = list()

        if len(word_list) == 0:
            return palindromes_list

        potential_palindrome = word_list[0]
        if len(potential_palindrome) == 1:
            word_list = [remaining_word for remaining_word in word_list if remaining_word != potential_palindrome]
            return self.find_palindromes(word_list, palindromes_list)

        for i in range(len(potential_palindrome)):
            if potential_palindrome[i] != potential_palindrome[-i-1]:
                word_list = [remaining_word for remaining_word in word_list if remaining_word != potential_palindrome]
                return self.find_palindromes(word_list, palindromes_list)

        palindromes_list.append(potential_palindrome)
        word_list = [remaining_word for remaining_word in word_list if remaining_word != potential_palindrome]
        return self.find_palindromes(word_list, palindromes_list)

    def find_email_address(self, file: str) -> str:
        """list all the email addresses in a file"""
        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        mail_list = re.findall(r'([A-Za-z0-9_-]+\.?[A-Za-z0-9_-]+@[A-Za-z0-9]+\.?[A-Za-z]+\.?[A-Za-z]+)', txt)
        if not mail_list:
            raise NoEmailAddressesError
        return str(mail_list)

    def secret_message(self, file: str):
        """Find a very secret message in the text"""
        txt = self.readfile(file)
        if txt == "File not Found":
            return txt

        some_list =  re.findall(r'([A-Z]?[a-z]+[A-Z][a-z]+)', txt)
        print(some_list)
        for word in some_list:
            print(re.search(r'(?![A-Z])', word))



if __name__ == "__main__":
    d = DocumentReader()
    # print(d.readfile('text'))
    # print(d.replace('text', 'een', ''))
    # print(d.common_word('text', limit=10))
    # print(d.secret_message('text'))
    #print(d.palindromes('text'))
    # print(d.find_email_address('text'))
    # print(d.replace('text', 'publiciteit', ' '))

