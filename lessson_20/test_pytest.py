import requests
import pytest
import allure


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('bye')

@allure.feature('Posts')
@allure.story('Get post')
@pytest.mark.smoke
def test_get_one_post(new_post_id):
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check that post id with id {new_post_id} exists'):
        assert response['id'] == new_post_id

@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.smoke
def test_get_all_posts():
    with allure.step('Get all posts'):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Posts')
@allure.story('Manipulate post')
@pytest.mark.regression
def test_add_post():
    with allure.step('create reqauest body'):
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

@allure.feature('Example')
@allure.story('equals')
@pytest.mark.regression
def test_one():
    assert 1 == 2

@allure.feature('Example')
@allure.story('equals')
@pytest.mark.parametrize('logins', ['', ' ', '(*&)^'])
def test_two(logins):
    print(logins)
    assert 2 == 3

@allure.feature('Example')
@allure.story('equals')
def test_three():
    assert 3 == 3

@allure.feature('Example')
@allure.story('equals')
def test_num1(num):
    print(num)