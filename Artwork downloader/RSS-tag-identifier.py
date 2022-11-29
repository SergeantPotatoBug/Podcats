

# this is a pattern identifier for RSS feeds that uses regex
# it will record every thing between the opening tag and the closing tag whether on the same line
# or paragraph. it is more inclusive than the other tag-slicer


import re


def slice(tag, filepath):


    # initializations
    file = open(filepath, 'r')  # opening the file in read mode
    line = file.readline()  # reading the first line
    kind = 0  # a default tag kind, it will  be changed to other values depending on the HTML tag kind
    pattern_1 = rf'{tag}'  # the opening tag, or the tag
    output = ''  # the final output


    # checking the format/kind of the tag
    if bool(re.match(r'<(.)+/>', tag)):  # regex matches anything that starts with < and ends with />, AKA empty tag
        kind = 1  # kind = empty tag, the ones with no closing tags like <br/>
    elif bool(re.match(r'<(.)+>', tag)):  # regex matches anthing that starts with < and ends with >, AKA regular tag
        kind = 2  # kind = non-empty tags, the ones that have an opening tag and a closing tag like <h></h>


    # acting based on the kind of the tag, empty or not empty

    if kind == 1:  # if it is empty, it returns the line itself, what is in the tag
        output += line  # appending to the output string
        line = file.readline()  # going to the next line

    elif kind == 2:  # if it is a tag that has an opening and a closing tag
        end_tag = tag.replace('<', '</')  # making the end tag
        if bool(re.search(rf'{tag}', line)):  # checking if the end tag is in the line
            output += line  # if so, write the line to the output string and move on
            line = file.readline()  # on to the next line
        else:
            while not bool(re.search(rf'{end_tag}', line)):
                output += line
                line = file.readline()

            output += line
