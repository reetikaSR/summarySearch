import numpy


# remove extra spaces
def strip_string(input_string):
    return input_string.strip(' ')


# convert the string to lower case
def to_lower_case(input_string):
    return input_string.lower()


def remove_stop_words(input_string, stop_words):
    return ' '.join([word for word in input_string.split() if (word not in stop_words and word != ' ')])


def remove_bad_chars(input_string, bad_chars):
    """
    :param input_string: string from which the bad characters are to be removed
    :param bad_chars: list of bad characters
    :return: string after removing bad characters
    """
    translation_map = dict((c, ' ') for c in bad_chars)
    return input_string.translate(translation_map)


def calculate_term_frequency(input_string):
    """
    term frequency = (frequency of the word) / (total words in the string)
    :param input_string: string for which term frequency map to be built
    :param stop_words: the words which should not be added to the calculation
    :return: term frequency map for each word
    """

    total_words = 0  # total number of words
    word_map = {}  # term frequency map
    for word in input_string.split(' '):
        if word != '':
            total_words += 1
            word_map[word] = word_map[word] + 1 if word in word_map else 1

    for word in word_map:
        word_map[word] = word_map[word]/total_words

    return word_map


def calculate_idf(list_books):
    """
    IDF = ln((total_numbers of docs)/(number of docs in which the word is present))
    :param list_books: list of the all the books
    :return: IDF of all the books
    """

    total_documents = len(list_books)  # total number of documents
    master_map = {}
    for book in list_books:
        for word in book.tf:
            if word in master_map:
                master_map[word] += 1
            else:
                master_map[word] = 1

    for word in master_map:
        word_count = master_map[word]
        master_map[word] = numpy.log(total_documents/word_count)

    return master_map


def get_tf_idf(doc_tf, idf_map):
    """
    calculate the product of the term frequency and the idf
    :param doc_tf: term frequency map of the string
    :param idf_map: idf map of all the strings
    :return: vector map of a document
    """

    vector = {}

    for word in doc_tf:
        if word in idf_map:
            tf_idf = doc_tf[word] * idf_map[word]
            if tf_idf:
                vector[word] = tf_idf

    return vector


def normalise_vector(vector):
    """
    :param vector: vector map of a string
    :return: normalised data for each word
    """

    sum_of_squares = 0

    for word in vector:
        sum_of_squares += vector[word] * vector[word]

    normalised_denominator = numpy.sqrt(sum_of_squares)

    for word in vector:
        vector[word] /= normalised_denominator

    return vector


# wrapper to get teh normalised vector from term frequency map and the IDF
def compute_normalised_vector(term_freq_map, idf_map):
    vector = get_tf_idf(term_freq_map, idf_map)
    normalised_vector = normalise_vector(vector)
    return normalised_vector


# clean the string by removing punctuations and spaces
def clean_string(input_string, bad_chars, stop_words):
    """
    :param input_string: string to be cleaned
    :param bad_chars: bad characters to be removed from the summary
    :param stop_words: words to be removed while processing the summary
    :return:
    """

    input_string = to_lower_case(input_string)
    input_string = remove_stop_words(input_string, stop_words)
    input_string = remove_bad_chars(input_string, bad_chars)
    input_string = strip_string(input_string)
    return input_string
