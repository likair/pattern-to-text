#! /usr/bin/env python3

"""
This is a command line application that takes at least two arguments as input.

The first argument is a random pattern consisting of characters S and T. For example 'STTTS'.

The following arguments are N (N >= 1) number of integers. For example 1 5 8. Each integer is separated from previous one with a space.

The application must validate input arguments.
- There needs to be enough arguments given
- Pattern must consist only of valid characters
- Numbers need to be integers

The application needs to convert each character in the pattern into human readable text and output the corresponding text. The length of the output is defined by the integer argument. For each input integer, the output needs to follow given pattern.

Character mapping to text.
S = soft
T = tough

Example run:
Input:
SST 5 2

Output:
Soft, Soft, Tough, Soft and Soft.
Soft and Soft.
"""


import sys
import logging

CHAR_MAPPING = {"S": "Soft", "T": "Tough"}

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class InvalidPatternError(Exception):
    """Raised when the pattern contains invalid characters."""

    pass


class InvalidIntegerError(Exception):
    """Raised when the integer is invalid."""

    pass


class InsufficientArgumentsError(Exception):
    """Raised when there are insufficient arguments."""

    pass


def validate_args(args: list[str]) -> None:
    """Validate the command line arguments.

    Args:
        args (list[str]): The command line arguments.

    Raises:
        ValueError: If there are insufficient arguments.
        ValueError: If the pattern contains invalid characters.
        ValueError: If the numbers are not integers.
    """
    if len(args) < 3:
        raise InsufficientArgumentsError(f"There needs to be enough arguments given.")

    pattern = args[1]
    for char in pattern:
        if char not in CHAR_MAPPING:
            raise InvalidPatternError(f"Pattern must consist only of valid characters.")

    for num in args[2:]:
        if not num.isdigit() or int(num) < 1:
            raise InvalidIntegerError(f"Numbers need to be integers.")


def extend_pattern(pattern: str, length: int) -> str:
    """Extend the pattern to fit the given length.

    Args:
        pattern (str): The pattern to be extended.
        length (int): The length of the extended pattern.

    Returns:
        str: The extended pattern.
    """
    repeat_count = length // len(pattern) + 1
    extended = (pattern * repeat_count)[:length]
    logging.debug(f"Extended pattern: {extended}")
    return extended


def pattern_to_words(pattern: str) -> list[str]:
    """Convert the pattern to a list of words.

    Args:
        pattern (str): The pattern to be converted.

    Returns:
        list[str]: The list of words.
    """
    word_list = [CHAR_MAPPING[char] for char in pattern]
    logging.debug(f"Word list: {word_list}")
    return word_list


def format_output(word_list: list[str]) -> str:
    """Format the word list for the final output.

    Args:
        word_list (list[str]): The list of words.

    Returns:
        str: The formatted output.
    """
    if len(word_list) == 0:
        return ""

    if len(word_list) == 1:
        return f"{word_list[0]}."

    return ", ".join(word_list[:-1]) + f" and {word_list[-1]}."


def main():
    """This is the entry point of the program."""
    validate_args(sys.argv)

    pattern = sys.argv[1]

    for num in sys.argv[2:]:
        extended = extend_pattern(pattern, int(num))
        word_list = pattern_to_words(extended)
        print(format_output(word_list))


if __name__ == "__main__":
    main()
