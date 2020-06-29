from SumarySearch.utils import clean_string, calculate_term_frequency, compute_normalised_vector
from SumarySearch import books_data, idf_map, stop_words, bad_chars, Priority


def calculate_cosine_for_vectors(vector1, vector2):
    """
    :param vector1:
    :param vector2:
    :return: cosine of two vectors
    """
    cosine = 0
    for word in vector2:
        if word in vector1:
            cosine += vector2[word] * vector1[word]
    return cosine


def get_vector_of_query(query, idf):
    """
    :param query: input query string
    """

    cleaned_string = clean_string(query, bad_chars, stop_words)
    term_freq = calculate_term_frequency(cleaned_string)
    query_vector = compute_normalised_vector(term_freq, idf)
    return query_vector


def match(query, max_count):
    """
    :param query: input query string
    :param max_count: k number of results
    :return:atmost max_count number of results for the query match
    """
    query_vector = get_vector_of_query(query, idf_map)
    k_queue = Priority.PriorityQ(max_count)
    for book in books_data:
         match_score = calculate_cosine_for_vectors(book.vector, query_vector)
         if match_score > 0:
            k_queue.add(match_score, book)

    return k_queue.get_reverse_sorted_elements()
