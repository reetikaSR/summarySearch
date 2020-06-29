from django.test import Client
from unittest import TestCase
import json
from SumarySearch.string_processing import process_data


class TestApi(TestCase):
    def setUp(self):
        self.client = Client()

        self.url = '/search/'
        self.headers = {'Content-Type': 'application/json' }
    
    def test_search_queries_success(self):
        # Body
        data_json = {"queries": ["achieve take book", "is your problems"], "k": 3}

        # convert dict to json by json.dumps() for body data.
        resp = self.client.post(self.url, headers=self.headers, data=data_json)

        # Validate status code.
        self.assertEqual(resp.status_code, 200)

        # print response full body as text
        data = json.loads(resp.content.decode('utf8').replace("'", '"'))
        self.assertEqual(len(data), 6)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['id'], 20)
        self.assertEqual(data[2]['id'], 14)
        self.assertEqual(data[3]['id'], 0)
        self.assertEqual(data[4]['id'], 48)
        self.assertEqual(data[5]['id'], 7)

    def test_search_queries_missing_k(self):
        # Body
        data_json = {"queries": ["is your problems", "achieve take book"]}

        # convert dict to json by json.dumps() for body data.
        resp = self.client.post(self.url, headers=self.headers, data=data_json)

        # Validate status code.
        self.assertEqual(resp.status_code, 400)

    def test_search_queries_missing_queries(self):
        # Body
        data_json = {"k": 1}

        # convert dict to json by json.dumps() for body data.
        resp = self.client.post(self.url, headers=self.headers, data=data_json)

        # Validate status code.
        self.assertEqual(resp.status_code, 400)

    def test_search_queries_empty_list(self):
        # Body
        data_json = {"queries": [], "k": 1}

        # convert dict to json by json.dumps() for body data.
        resp = self.client.post(self.url, headers=self.headers, data=data_json)

        # Validate status code.
        self.assertEqual(resp.status_code, 400)
