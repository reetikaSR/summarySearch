from unittest import TestCase

from SumarySearch import utils, bad_chars, stop_words
from SumarySearch.models import Book


class TestUtils(TestCase):
    def setUp(self):
        self.list_of_books = [Book(1, utils.clean_string('The Book in Three Sentences:\u00a0What if we measured our lives based on ',
                                                         bad_chars,
                                                         stop_words)),
                              Book(2, utils.clean_string("The quicker you let go of old things, the sooner",
                                                         bad_chars,
                                                         stop_words))]
        self.str1 = 'The Book in Three Sentences:\u00a0What if we measured our lives based on '
        self.str2 = "???/////  ;;;; ;;::: "
        self.str3 = ''

    def set_term_frequency(self):
        for book in self.list_of_books:
            book.set_term_frequency(utils.calculate_term_frequency(book.summary))

    def get_idf(self):
        return utils.calculate_idf(self.list_of_books)

    def test_clean_string_success(self):
        clean_str = "book sentences  measured lives based"
        self.assertEqual(self.list_of_books[0].summary, clean_str)

    def test_calculate_term_frequency_success(self):
        cleaned_string = utils.clean_string(self.str1, bad_chars, stop_words)
        term_freq = utils.calculate_term_frequency(cleaned_string)
        # term_freq = {"book": 0.2, "sentences": 0.2, "measured": 0.2, "lives": 0.2, "based":0.2}
        self.assertEqual(utils.calculate_term_frequency(self.list_of_books[0].summary), term_freq)

    def test_compute_normalised_vector_success(self):
        self.set_term_frequency()

        idf = self.get_idf()

        cleaned_string = utils.clean_string(self.str1, bad_chars, stop_words)
        term_freq = utils.calculate_term_frequency(cleaned_string)
        expected_idf = utils.compute_normalised_vector(term_freq, idf)

        self.assertEqual(utils.compute_normalised_vector(self.list_of_books[0].tf, idf), expected_idf)

    def test_clean_string_fail(self):
        clean_str = ""
        self.assertEqual(utils.clean_string(self.str2, bad_chars, stop_words), clean_str)

    def test_calculate_term_frequency_fail(self):
        cleaned_string = utils.clean_string(self.str3, bad_chars, stop_words)
        term_freq = {}
        self.assertEqual(utils.calculate_term_frequency(cleaned_string), term_freq)
