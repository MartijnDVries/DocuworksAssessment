import re
import itertools

class DocumentReader:

    def __init__(self):
        self.path = "C:\\Python\\DocuworksAssessment\\TextFiles\\"

    def readfile(self, file : str) -> str:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return txt.strip()

    def savefile(self, file : str, file_name : str):
        with open(f"{self.path}{file_name}.txt", 'w') as f:
            f.write(file)

    def search(self, file: str, search : str) -> list:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return [word.span() for word in re.finditer(search, txt.strip())]

    def replace(self, file: str, search: str, replace: str) -> str:
        print(search)
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return re.sub(fr"\b{search}\b", replace, txt.strip())

    def common_word(self, file: str) -> list:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()

        word_list = txt.split()
        return self.find_common_word(word_list)

    def find_common_word(self, word_list : list, count_list: list = None) -> list:
        if count_list is None:
            count_list = ['', 0]
        if len(word_list) == 0:
            return count_list
        else:
            if all(word == word_list[0] for word in word_list):
                if word_list.count(word_list[0]) > count_list[1]:
                    count_list = [word_list[0], word_list.count(word_list[0])]
                    return count_list
                else:
                    print(word_list)
                    return count_list
            else:
                word = word_list[0]
                count = word_list.count(word)
                word_list = [not_word for not_word in word_list if not_word != word]
                if count > count_list[1]:
                    count_list = [word, count]
                count_list = self.find_common_word(word_list, count_list)
                return count_list



if __name__ == "__main__":
    d = DocumentReader()
    # print(d.readfile('text'))
    # print(d.replace('text', 'een', ''))
    print(d.common_word('text'))
    # print(d.replace('text', 'publiciteit', ' '))
