import pytest
import requests

from data.db_session import global_init

base_url = 'http://127.0.0.1:5000'


@pytest.fixture
def db_init():
    global_init('db/mars_explorer.db')


def test_get_one_user(db_init):
    response = requests.get(base_url + '/api/v2/users/1')
    sess = create_session()
    user = sess.query(User).get(1)
    assert response.json() == {'user': user.to_dict(rules=('-jobs',))}


def test_get_wrong_user(db_init):
    user_id = 999
    response = requests.get(base_url + f'/api/v2/users/{user_id}')
    assert response.json() == {'error': 'Not found'}


def test_get_all_user(db_init):
    response = requests.get(base_url + '/api/v2/users')
    session = create_session()
    users = session.query(User).all()
    assert response.json() == {'users': [item.to_dict(only=('id', 'name', 'surname', 'email', 'jobs.id', 'jobs.job'))
                                         for item in users]}


def test_post_user(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email@mail.ru'
    }
    response = requests.post(base_url + '/api/x2/users', json=user_json)
    assert response.json() == {'success': 'OK'}


def test_post_user_missed_param(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность'
    }


response = requests.post(base_url + '/api/x2/users', json=user_json)
assert response.json() == {'message': 'error'}


def test_post_user_empty(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email@mail.ru'
    }
    response = requests.post(base_url + '/api/x2/users', json=user_json)
    assert response.json() == {'success': 'OK'}


def test_wrong_param_user(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email4@mail.ru'
    }
    response = requests.post(base_url + '/api/x2/users', json=user_json)
    assert response.json() == {'success': 'OK'}


def test_user_already_exists(db_init):
    user_json = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 10,
        'speciality': 'Специальность',
        'email': 'email@mail.ru'
    }
    response = requests.post(base_url + '/api/x2/users', json=user_json)


def test_delete_user(db_init):
    response = requests.delete(base_url + '/api/v2/users/2')
