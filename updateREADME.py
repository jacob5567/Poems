# This program is run before each push to update the README

import os


def main():
    dir_names = [i for i in next(os.walk('.'))[1] if i[0] != '.']
    file_dict = []
    index = 0
    for i in dir_names:
        file_dict.append([])
        for j in os.listdir("./" + i):
            file_dict[index].append(j[:-3]) # -3 to remove the .md
        index += 1

    # Write to file
    with open("README.md", 'w') as f:
        f.write("# Poems\n")
        f.write("## A collection of some of my favorite poems\n")
        index = 0
        for i in dir_names:
            f.write(f"### {i}\n")
            for j in file_dict[index]:
                f.write(f"\t{j}\n")
            index += 1

if __name__ == "__main__":
    main()
