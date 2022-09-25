# even pages: a number, followed by two words with a period where 2nd is alphabetically higher than first


#  odd pages: two  wordsd higher than each other followed by a number

import  re
import pathlib

OUTPUT_FILE = "dictionary.txt"


def read_file(file):
    """If a page matches a good enough pattern, append data to outputfile

    This is used in one-time setup of the "words" table
    """
    page_number = file.split('_')[1].split('.')[0]

    try:
        page_number=int(page_number)
    except ValueError:
        print(f"{file} is  unparsable for  page number, skip  it")

    with open(file, "rt") as f:
        try:
            data =  " ".join([x.strip() for x in f.readlines() if x.strip()])
        except UnicodeDecodeError as e:
            print("for file {file}, got {e}\n")
            return
    if two_words(data, page_number):
        print("fine", end="")
        return
    if regexp_two_words(data, page_number):
        print("good", end="")
        return
    if regexp_longest_word(data, page_number):
        print("LONG", end="")
        return
    print(f"<oopsie: {data.strip()} //for file {file}>")

    return


    
def two_words(text, page):
    goodies = "".join([c for c in text if c in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ-']).strip()
    if goodies.startswith('-'): goodies = goodies[1:]
    goodies = re.sub(' +', ' ', goodies)
    words = goodies.split(" ")
    if len(words) == 2:
        with open(OUTPUT_FILE, "at") as outf:
            outf.write(f"{page},{words[0]}\n")
            outf.write(f"{page},{words[1]}\n")
        return True
    else:
        return False
    

words_re = r"^[^A-Z]*(?P<word1>[A-Z][A-Z-]*[A-Z]-?)[\.,]? +(?P<word2>[A-Z][A-Z-]*[A-Z]-?)"
pattern = re.compile(words_re)

def regexp_two_words(text, page):
    matches = pattern.match(text)
    if matches:
        with open(OUTPUT_FILE, "at") as outf:
            outf.write(f"{page},{matches[1]}\n")
            outf.write(f"{page},{matches[2]}\n")
        return True
    else:
        return False

long_pattern = re.compile(r"^[^A-Z]*(?P<longword>[A-Z][A-Z-]*[A-Z]-?)")
def regexp_longest_word(text, page):
    matches = long_pattern.match(text)
    if matches:
        with open(OUTPUT_FILE, "at") as outf:
            outf.write(f"{page},{matches[1]}\n")
        return True
    else:
        return False
 


p =  pathlib.Path('/py/skeat/one-time-load/data/per-page-keywords/')
for counter, f in enumerate(p.glob("skeat_*.txt")):
    read_file(f.name)

    print(f"read {counter} files")


