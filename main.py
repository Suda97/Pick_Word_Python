import random


def openFile():
    with open('words.txt', 'r') as f:
        line = f.readline().strip()
        file = []
        while line:
            line = f.readline().strip()
            file.append(line)
        f.close()
    return file


if __name__ == '__main__':
    file = openFile()
    file.pop()
    word = file[random.randint(0, len(file) - 1)]
    print(word)
