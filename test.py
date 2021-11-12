import os
import tempfile
from Group5.routes import render_template

import pytest

from Group5 import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/home')
    assert resp.status_code == 200


def test_home_bad_request(client):
    resp = client.post('/home')
    assert resp.status_code == 405


def test_about(client):
    resp = client.get('/about')
    assert resp.status_code == 200


def test_about_bad_request(client):
    resp = client.post('/about')
    assert resp.status_code == 405


def test_announcements_should_redirect(client):
    resp = client.get('/announcements')
    assert resp.status_code == 302


def test_announcements_bad_request(client):
    resp = client.post('/about')
    assert resp.status_code == 405


def test_register_get(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_register_post(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_login_get(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_login_post(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_login_nonexistent_user(client):
    resp = client.post('/login', json={'username': 'nothing', 'email': 'nothing@gmail.com',
                                       'password': 'nothing123'})
    assert resp.status_code == 200

# def test_home_bad_http_method(client):
#     resp = client.post('/')
#     assert resp.status_code == 405
#
# def test_account(client):
#     resp = client.post('/account', data='something')
#     assert resp.status_code == 302
#
# def test_account_bad_http_method(client):
#     resp = client.post('/account')
#     assert resp.status_code == 400
#
# def test_search(client):
#     resp = client.post('/announcements', data='something')
#     assert resp.status_code == 400
#
# def test_search_bad_http_method(client):
#     resp = client.post('/announcements')
#     assert resp.status_code == 400
#
# def test_register(client):
#     resp = client.post('/register', data='something')
#     assert resp.status_code == 400
#
# def test_register_bad_http_method(client):
#     resp = client.post('/register')
#     assert resp.status_code == 400
#
# def test_schedule(client):
#     resp = client.post('/schedule', data='something')
#     assert resp.status_code == 400
#
# def test_schedule_bad_http_method(client):
#     resp = client.post('/schedule')
#     assert resp.status_code == 400
#
# def test_insert(client):
#     resp = client.post('/insert', data='something')
#     assert resp.status_code == 400
#
# def test_insert_bad_http_method(client):
#     resp = client.post('/insert')
#     assert resp.status_code == 400
