import re


def parse(expression, removable1, removable2, file, pre):  # gives the whole line when the expression matches
    dump = []
    with open(file, 'r') as file:
        for line in file:  # looping through the lines of the file
            if bool(re.match(rf"{expression}", line)):  # checking if the line matches the pattern
                line = line.replace(removable1, '')  # removing the first removable tag
                line = line.replace(removable2, '')  # removing the first removable tag

                line = prefix(pre, line)  # adding 'Ep ' to all the elements that don't have 'Ep ' as their prefix

                dump.append(line)  # adding the tag-less string to a list
            else:  # if it doesn't match the pattern
                continue  # on to the next line

        return dump  # is a list of all the matching lines, minus their tags


def prefix(pre, prefixee):  # for titles, to make them uniform as some have 'Ep ' in front of them
    if bool(re.match(rf'{pre}', prefixee)):  # a match means that the suffix already exists
        prefixed = prefixee
        pass
    else:  # if there is no match, it means that the prefix does not exist
        prefixed = pre + prefixee

    return prefixed

print(parse('<title>(Ep )*[0-9]', '<title>', '</title>', 'RSS-feed', 'Ep '))
# dump = parse('<title>(Ep )*[0-9]', '<title>', '</title>', 'RSS-feed', 'Ep ')
# print(prefix('to', 'mato'))
# print(parse('<title>(Ep )*[0-9]', '<title>', '</title>', 'RSS-feed')[0])
