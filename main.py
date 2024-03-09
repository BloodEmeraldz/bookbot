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

main()