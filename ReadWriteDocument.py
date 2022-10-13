import re

class DocumentReader:

    def __init__(self):
        self.path = "C:\\Python\\DocuworksAssessment\\TextFiles\\"

    def readfile(self, file : str) -> str:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return txt.strip()

    def savefile(self, file : str):
        with open(f"{self.path}{file}.txt", 'w') as f:
            f.write(file)

    def search(self, file: str, search : str) -> list:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return [word.span() for word in re.finditer(search, txt.strip())]


    def replace(self, file: str, search: str, replace: str) -> str:
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()
        return re.sub(search, replace, txt.strip())




if __name__ == "__main__":
    d = DocumentReader()
    # print(d.readfile('text'))
    print(d.replace('text', 'Otje', 'YOLO'))
