import io

import click
import json


class DocumentReader:

    def __init__(self):
        self.path = "C:\\Python\\DocuworksAssessment\\TextFiles\\"

    def readfile(self, file):
        with open(f"{self.path}{file}.txt", 'r') as f:
            txt = f.read()

        print(txt.strip())

    def savefile(self, file):
        with open(f"{self.path}{file}.txt", 'w') as f:
            f.write(file)


if __name__ == "__main__":
    d = DocumentReader()
