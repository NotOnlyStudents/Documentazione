import sys
import os
import json

extension = ".tex"
includedDirectories = ["DocumentiPubblici", "DocumentiInterni"]

def createFileToInclude(filepath):
    working_directory, filename = os.path.split(filepath);
    
    fields = {
        "working_directory": working_directory,
        "filename": filename
    }
    
    return fields

def findAllTexFiles(dir, prev, matrix):

    files = os.listdir(dir);

    texFile = [ file for file in files if os.path.splitext(file)[1] == extension ]

    if texFile:
        filepath = dir + "/" + texFile[0];
        matrix["include"].append(createFileToInclude(filepath))
        return

    for filename in files:
        filepath = f"{dir}/{filename}"

        if os.path.isdir(filepath) and isIncluded(filepath):
            findAllTexFiles(filepath, dir, matrix)


def isIncluded(dirpath):
    included = False

    for includedDirectory in includedDirectories:
        if includedDirectory in dirpath: 
            included = True

    return included


def main():
    matrix = {
        "include": []
    };

    findAllTexFiles(sys.argv[1], "", matrix);

    print(json.dumps(matrix));


if __name__ == "__main__":
    main();
