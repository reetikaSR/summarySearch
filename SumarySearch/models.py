import requests
import json


class Book:
    """
    initializes the Book object
    """

    def __init__(self, id, summary):
        self.id = id
        self.summary = summary
        self.author = None
        self.tf = None
        self.vector = None

    # get the author of the book. If not present, fetch from the given api
    def get_author(self):
        if not self.author:
            data = json.dumps({"book_id": self.id})
            headers = {'Content-Type': 'application/json'}
            author_json = requests.post("https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding",
                                        data=data, headers=headers)
            author_json = json.loads(author_json.content.decode('utf8').replace("'", '"'))
            self.author = author_json['author']
        return self.author

    # set the term frequency map of the book summary
    def set_term_frequency(self, term_freq):
        self.tf = term_freq

    # set the vector map of the book summary
    def set_vector(self, vector_map):
        self.vector = vector_map