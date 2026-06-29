import unittest
import requests


class TestPostApi(unittest.TestCase):
    def add(self):
        return 5 + 5

    def test_get_all_post(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
        body = {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)