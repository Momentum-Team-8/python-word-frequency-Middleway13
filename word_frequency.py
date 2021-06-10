from typing import Text
import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    with open(file) as the_word:
        text = the_word.read().lower()
        words = text.split()
        no_punc = sorted([word.strip(string.punctuation) for word in words])

        print(no_punc)

        word_count = []
        for word in no_punc:
            if word not in STOP_WORDS:
                word_count.append(word)

        print(no_punc)
        
        counted = {}

        for word in no_punc:
        
            if word in counted:
                counted[word] = counted[word] + 1
            elif word not in counted:
                counted[word] = 1

        print(counted)

        breakpoint()


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)