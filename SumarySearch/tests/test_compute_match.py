from unittest import TestCase

from SumarySearch.string_processing import process_data
from SumarySearch.compute_match import calculate_cosine_for_vectors, get_vector_of_query


class TestComputeMatch(TestCase):
    def setUp(self):
        self.list_of_books = [{'id': 1,
                               'summary':'The Book in Three Sentences:\u00a0What if we measured our lives based on '},
                              {'id': 2,
                               'summary':'The quicker you let go of old things, the sooner", bad_chars, stop_words'}]
        self.query = 'The Book in Three Sentences:\u00a0What if we measured our lives based on '

    def test_vectors_success(self):
        list_of_books, idf_map = process_data(self.list_of_books)
        query_vector = get_vector_of_query(self.query, idf_map)
        self.assertEqual(list_of_books[0].vector, query_vector)

    def test_vectors_fail(self):
        list_of_books, idf_map = process_data(self.list_of_books)
        query_vector = get_vector_of_query(self.query, idf_map)
        self.assertNotEqual(list_of_books[1].vector, query_vector)

    def test_calculate_cosine_for_vectors_success(self):
        list_of_books, idf_map = process_data(self.list_of_books)
        query_vector = get_vector_of_query(self.query, idf_map)
        self.assertAlmostEqual(calculate_cosine_for_vectors(list_of_books[0].vector, query_vector), 1)

    def test_calculate_cosine_for_vectors_fail(self):
        list_of_books, idf_map = process_data(self.list_of_books)
        query_vector = get_vector_of_query(self.query, idf_map)
        self.assertNotAlmostEqual(calculate_cosine_for_vectors(list_of_books[1].vector, query_vector), 1)