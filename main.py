import string

def count_words(file_contents):
    def remove_punctuation(file_contents):
        translator = str.maketrans("", "", string.punctuation)
        text_without_punctuation = file_contents.translate(translator)
        return text_without_punctuation

    file_contents = remove_punctuation(file_contents)  # Apply remove_punctuation to file_contents
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

def sort_on(dictionary):
    return dictionary["count"]

def count_characters(book_text):
    """
    Counts the occurrences of each alphabetic character in the given book text.

    Args:
        book_text (str): The text of the book.

    Returns:
        list: A list of dictionaries, where each dictionary contains the character and its count.
              The list is sorted in descending order based on the character count.
    """
    book_text = book_text.lower()
    character_count = {}
    for char in book_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1

    # Convert the dictionary into a list of dictionaries
    character_list = [{"char": char, "count": count} for char, count in character_count.items()]

    # Sort the list of dictionaries by the "count" key
    character_list.sort(reverse=True, key=sort_on)

    return character_list

def main():
    """
    Entry point of the program.
    Reads the contents of a file, counts the words and characters,
    and prints a report of the analysis.
    """
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print("The number of words in the document is", count_words(file_contents))
        character_list = count_characters(file_contents)
        for character in character_list:
            print(f"The '{character['char']}' character was found {character['count']} times.")
        print("--- End report ---")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")

def count_words(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The text to count words from.

    Returns:
        int: The number of words in the text.
    """
    # Count the number of words using whitespace as delimiter
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the occurrences of each character in the given text.

    Args:
        text (str): The text to count characters from.

    Returns:
        list: A list of dictionaries, each containing the character and its count.
    """
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return [{'char': char, 'count': count} for char, count in character_count.items()]

main()