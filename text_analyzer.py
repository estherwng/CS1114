# Author: <Esther Wang>
# Assignment #2 - TextAnalyzer
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def character_is_whitespace(char):
    """Indicates whether the value referenced by char parameter
    is a whitespace character (' ', '\n', '\t')

    :param char: character to check
    :return: True when char is space character, False otherwise
    """
    if char == " ":
        return True
    if char == "\n":
        return True
    if char == "\t":
        return True
    else:
        return False


def character_ends_sentence(char):
    """Indicates whether the value referenced by char parameter
    is a period, question mark, or exclamation point

    :param char: character to check
    :return: True when char ends sentence, False otherwise
    """
    if char == "!":
        return True
    if char == "?":
        return True
    if char == ".":
        return True
    else:
        return False


def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):
    """Prints the number of total characters, spaces, digits, letters,
    and sentences identified in the text being analyzed.

    :param num_chars: number of total characters in text
    :param num_spaces: number of spaces in text
    :param num_digits: number of digits in text
    :param num_letters: number of letters in text
    :param num_sentences: number of sentences in text
    :return: None

    <BLANKLINE>
    Count of characters: 234
    Count of spaces: 14
    Count of digits: 16
    Count of letters: 201
    Count of sentences: 21
    <BLANKLINE>
    """
    print("\nCount of characters: ", num_chars, sep="")
    print("Count of spaces: ", num_spaces, sep="")
    print("Count of digits: ", num_digits, sep="")
    print("Count of letters: ", num_letters, sep="")
    print("Count of sentences: ", num_sentences, sep="")
    print()


def analyze_text():
    """Calls the functions to compute the number of total characters,
    spaces, digits, letters, and sentences in user-supplied text and to
    output the final counts when text input by user.

    :return: True when text provided, False when no text provided
    """
    text = str(input("Please enter text to analyze (press ENTER/return without text to exit): "))
    num_space = space_num(text)
    num_digit = digit_num(text)
    num_letters = letter_num(text)
    num_sentences = sentence_num(text)
    num_char = len(text)

    if text != "" and text != "\n":
        print_results(num_char, num_space, num_digit, num_letters, num_sentences)
        return True
    else:
        return False


def space_num(text):
    num_space = 0
    for i in range(len(text)):
        if character_is_whitespace(text[i]) is True:
            num_space += 1
    return num_space


def digit_num(text):
    num_digit = 0
    for i in range(len(text)):
        if character_is_digit(text[i]) is True:
            num_digit += 1
    return num_digit


def letter_num(text):
    num_letter = 0
    for i in range(len(text)):
        if character_is_letter(text[i]) is True:
            num_letter += 1
    return num_letter


def sentence_num(text):
    num_sentence = 0
    for i in range(len(text)):
        if character_ends_sentence(text[i]) is True:
            num_sentence += 1
    return num_sentence


####### DO NOT EDIT FUNCTIONS BELOW ########
def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """
    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """
    return char.isalpha()

####### DO NOT EDIT FUNCTIONS ABOVE ########


def run_text_analyzer():
    """run the text analyzer as a repeated sequence of prompting the user for input text and outputting the character counts computed from the input
    :return: None
    """
    print("Welcome to the Text Analyzer!\n")

    text = True
    while text:
        text = analyze_text()
    print("\nGoodbye.")


def main():
    """Runs a program for analyzing character counts from
    input text
    """
    run_text_analyzer()

    
####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    print("Running doctests...")
    import doctest
    doctest.testmod(verbose=True)

    print("\nRunning program...\n")

    main()
