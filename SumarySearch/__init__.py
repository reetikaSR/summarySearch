from SumarySearch.string_processing import load_data, get_stop_words, get_bad_chars

# stop words to be removed from the string
stop_words = get_stop_words()

# characters to be removed form the string
bad_chars = get_bad_chars()

# intial data and its vector map
books_data, idf_map = load_data()