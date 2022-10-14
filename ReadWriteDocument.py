import os
import re
from ErrorCases import NoPalindromeError

class DocumentReader:

    def __init__(self):
        self.path = os.getcwd()+"\\TextFiles\\"

    def readfile(self, file : str) -> str:
        """Open the file and return the text of this file"""
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return txt.strip()

    def savefile(self, file : str, file_name : str):
        """Save text file with chosen filename"""
        with open(f"{self.path}{file_name}.txt", 'w') as f:
            f.write(file)

    def search(self, file: str, search : str) -> list:
        """Search for a word in the text and return the index/indices in a list"""
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return [word.span() for word in re.finditer(search, txt.strip())]

    def replace(self, file: str, search: str, replace: str) -> str:
        """replace all occurrences of a word with a new word"""
        print(search)
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return re.sub(fr"\b{search}\b", replace, txt.strip())

    def common_word(self, file: str) -> list:
        """Find the most common word in the text"""
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        word_list = txt.split()
        return self.find_common_word(word_list)

    def find_common_word(self, word_list : list, count_list: list = None) -> list:
        """Continues common_word function"""
        if count_list is None:
            count_list = ['', 0]

        if len(word_list) == 0:
            return count_list

        if all(word == word_list[0] for word in word_list):
            if word_list.count(word_list[0]) > count_list[1]:
                return [word_list[0], word_list.count(word_list[0])]
            else:
                return count_list

        word = word_list[0]
        count = word_list.count(word)
        word_list = [not_word for not_word in word_list if not_word != word]
        if count > count_list[1]:
            count_list = [word, count]
        return self.find_common_word(word_list, count_list)

    def palindromes(self, file: str):
        """Find all palindromes in a text file and return in a list"""
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        word_list = txt.split()
        palindrome_list = self.find_palindromes(word_list)
        if not palindrome_list:
            raise NoPalindromeError
        return palindrome_list


    def find_palindromes(self, word_list: list, palindromes_list: list = None) -> list:
        """Continues palindromes function"""
        if palindromes_list is None:
            palindromes_list = list()

        if len(word_list) == 0:
            return palindromes_list

        potential_palindrome = word_list[0]
        if len(potential_palindrome) == 1:
            word_list = [not_word for not_word in word_list if not_word != potential_palindrome]
            return self.find_palindromes(word_list, palindromes_list)

        for i in range(len(potential_palindrome)):
            if potential_palindrome[i] != potential_palindrome[-i-1]:
                word_list = [not_word for not_word in word_list if not_word != potential_palindrome]
                return self.find_palindromes(word_list, palindromes_list)

        palindromes_list.append(potential_palindrome)
        word_list = [not_word for not_word in word_list if not_word != potential_palindrome]
        return self.find_palindromes(word_list, palindromes_list)



if __name__ == "__main__":
    d = DocumentReader()
    # print(d.readfile('text'))
    # print(d.replace('text', 'een', ''))
    # print(d.common_word('text'))
    print(d.palindromes('text'))
    # print(d.replace('text', 'publiciteit', ' '))
    # print(os.getcwd())
