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

def count_characters(book_text):
    book_text = book_text.lower()
    character_count = {}
    for char in book_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        print("The number of words in the book is:", count_words(file_contents))
        print("Character count:", count_characters(file_contents))
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")

main()
