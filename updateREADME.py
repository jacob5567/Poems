import os


def main():
    dir_names = [i for i in next(os.walk('.'))[1] if i[0] != '.']
    # TODO use dictionary to hold directory names and files beneath them


if __name__ == "__main__":
    main()
