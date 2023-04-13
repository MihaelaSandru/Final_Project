import unittest

import requests


class ApiTests(unittest.TestCase):
    # Set the base URL for the API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # Test 1: Verify the API is up and running
    def test_api_status(self):
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200

    # Test 2: Verify the API returns the correct response for a GET request
    def test_get_posts(self):
        response = requests.get(self.BASE_URL + '/posts')
        assert response.status_code == 200
        assert len(response.json()) == 100

    # Test 3: Verify the API returns the correct response for a POST request
    def test_create_post(self):
        post_data = {'title': 'Test Post', 'body': 'This is a test post.'}
        response = requests.post(self.BASE_URL + '/posts', json=post_data)
        assert response.status_code == 201
        assert response.json()['title'] == post_data['title']
        assert response.json()['body'] == post_data['body']

    # Test 4: Verify the API returns the correct response for a PUT request
    def test_update_post(self):
        post_id = 1
        updated_data = {'title': 'Updated Post', 'body': 'This post has been updated.'}
        response = requests.put(self.BASE_URL + '/posts/{}'.format(post_id), json=updated_data)
        assert response.status_code == 200
        assert response.json()['title'] == updated_data['title']
        assert response.json()['body'] == updated_data['body']

    # Test 5: Verify the API returns the correct response for a DELETE request
    def test_delete_post(self):
        post_id = 1
        response = requests.delete(self.BASE_URL + '/posts/{}'.format(post_id))
        assert response.status_code == 200
        assert response.json() == {}

    # Test 6: Verify the API returns the correct response for a GET request for a specific post
    def test_get_specific_post(self):
        post_id = 2
        response = requests.get(self.BASE_URL + '/posts/{}'.format(post_id))
        assert response.status_code == 200
        assert response.json()['id'] == post_id

    # Test 7: Verify the API returns the correct response for a GET request for comments
    def test_get_comments(self):
        response = requests.get(self.BASE_URL + '/comments')
        assert response.status_code == 200
        assert len(response.json()) == 500

    # Test 8: Verify the API returns the correct response for a GET request for a specific comment
    def test_get_specific_comment(self):
        comment_id = 2
        response = requests.get(self.BASE_URL + '/comments/{}'.format(comment_id))
        assert response.status_code == 200
        assert response.json()['id'] == comment_id

    # Test 9: Verify the API returns the correct response for a POST request for comments
    def test_create_comment(self):
        comment_data = {'postId': 1, 'name': 'Test Comment', 'email': 'test@test.com', 'body': 'This is a test comment.'}
        response = requests.post(self.BASE_URL + '/comments', json=comment_data)
        assert response.status_code == 201
        assert response.json()['name'] == comment_data['name']
        assert response.json()['email'] == comment_data['email']
        assert response.json()['body'] == comment_data['body']

    # Test 10: Verify the API returns the correct response for a PUT request for comments
    def test_update_comment(self):
        comment_id = 1
        updated_data = {'name': 'Updated Comment', 'email': 'updated@test.com'}

