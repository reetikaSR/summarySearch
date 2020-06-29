import json
from .models import Book
from .utils import clean_string, calculate_term_frequency, calculate_idf, compute_normalised_vector


# fetch the stop words
def get_stop_words():
    with open('SumarySearch/stopWords.txt') as stop_words_file:
        stop_words = stop_words_file.read().split()
    return set(stop_words)


# fetch the bad characters, removing apostrophe
def get_bad_chars():
    bad_chars = [i for i in range(33, 48)]
    bad_chars.extend([i for i in range(58, 65)])
    bad_chars.extend([i for i in range(91, 97)])
    bad_chars.extend([i for i in range(123, 256)])
    return bad_chars


def process_data(list_entries):
    """
    pre process the data:
    1. clean
    2. calculate term frequency
    3. calculate inverse document frequency
    4. calculate the vector map for each book

    :param list_entries: list of dictionaries withe id and summary
    :return: list of book objects and the IDF map of all the book summaries

    """

    list_books = []
    stop_words = get_stop_words()
    bad_chars = get_bad_chars()
    for book in list_entries:
        new_book = Book(book['id'], book['summary'])
        cleaned_string = clean_string(book['summary'], bad_chars, stop_words)
        term_freq = calculate_term_frequency(cleaned_string)
        new_book.set_term_frequency(term_freq)
        list_books.append(new_book)

    idf_map = calculate_idf(list_books)

    for book in list_books:
        vector = compute_normalised_vector(book.tf, idf_map)
        book.set_vector(vector)

    return list_books, idf_map


def load_data():
    with open('SumarySearch/data.json') as f:
        data = json.load(f)
    return process_data(data['summaries'])
