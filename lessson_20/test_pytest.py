import requests
import pytest

@pytest.fixture
def new_post_id():
    body = {
        "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo","body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf","userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',json=body,headers=headers)
    post_id = response.json()['id']
    print(f'Post created: {post_id}')
    yield post_id
    print('deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('bye')

@pytest.mark.smoke
def test_get_one_post(new_post_id):
    print('test')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id
@pytest.mark.smoke
def test_get_all_posts():
    print('test')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100
@pytest.mark.regression
def test_add_post():
    print('test')
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
    assert response.status_code == 201
    assert response.json()['id'] == 101

@pytest.mark.regression
def test_one():
    assert 1 == 1

@pytest.mark.parametrize('logins', ['', ' ', '(*&)^'])
def test_two(logins):
    print(logins)
    assert 2 == 2


def test_three():
    assert 3 == 3