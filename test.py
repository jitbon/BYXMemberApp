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
    resp = client.post('/announcements')
    assert resp.status_code == 405


def test_register_get(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_register_post(client):
    resp = client.post('/register')
    assert resp.status_code == 200


def test_login_get(client):
    resp = client.post('/login')
    assert resp.status_code == 200


def test_login_post(client):
    resp = client.post('/login')
    assert resp.status_code == 200


# logging in with nonexistent user should not log in user but still return 200
def test_login_nonexistent_user(client):
    resp = client.post('/login', json={'username': 'nothing', 'email': 'nothing@gmail.com',
                                       'password': 'nothing123'})
    assert resp.status_code == 200


def test_logout(client):
    resp = client.get('/logout')
    assert resp.status_code == 302;


def test_logout_bad_request(client):
    resp = client.post('/logout')
    assert resp.status_code == 405


def test_account(client):
    resp = client.get('/account')
    assert resp.status_code == 302


def test_account_bad_http_method(client):
    resp = client.post('/account')
    assert resp.status_code == 302


def test_make_announcement(client):
    resp = client.get('/post/new')
    assert resp.status_code == 302


def test_make_announcement_bad_request(client):
    resp = client.post('/post/new')
    assert resp.status_code == 302


def test_view_announcement(client):
    resp = client.get('/post/<int:post_id>', data='something')
    assert resp.status_code == 404


def test_view_announcement_2(client):
    resp = client.post('/post/<int:post_id>')
    assert resp.status_code == 404


def test_update_post(client):
    resp = client.get('/post/<int:post_id>update', data='something')
    assert resp.status_code == 404


def test_update_post_2(client):
    resp = client.post('/post/<int:post_id>/update')
    assert resp.status_code == 404


def test_delete_post(client):
    resp = client.get('/post/<int:post_id>/delete')
    assert resp.status_code == 404


def test_delete_post_2(client):
    resp = client.post('/post/<int:post_id>/delete')
    assert resp.status_code == 404


def test_delete_post(client):
    resp = client.get('/user/<string:username>')
    assert resp.status_code == 404


def test_delete_post_2(client):
    resp = client.post('/user/<string:username>')
    assert resp.status_code == 405


def test_reset_password(client):
    resp = client.get('/reset_password')
    assert resp.status_code == 200


def test_reset_password_2(client):
    resp = client.post('/reset_password')
    assert resp.status_code == 200


def test_reset_password_after_email(client):
    resp = client.get('/reset_password/<token>')
    assert resp.status_code == 302


def test_reset_password_after_email_2(client):
    resp = client.post('/reset_password/<token>')
    assert resp.status_code == 302


def test_schedule(client):
    resp = client.get('/schedule')
    assert resp.status_code == 302


def test_schedule_2(client):
    resp = client.post('/schedule')
    assert resp.status_code == 302


def test_add_user(client):
    resp = client.get('/insert')
    assert resp.status_code == 405


def test_add_user_2(client):
    resp = client.post('/insert')
    assert resp.status_code == 400


def test_update_user(client):
    resp = client.get('/update')
    assert resp.status_code == 500


def test_update_user_2(client):
    resp = client.post('/update')
    assert resp.status_code == 400

# register a user
def test_register_user(client):
    resp = client.post('/register', json={'username': 'jason',
                                          'email': 'hi@gmail.com',
                                          'password': 'Hello123!',
                                          'password': 'Hello123!'})
    assert resp.status_code == 200

# log the user in
def test_login_user(client):
    resp = client.post('/login', json={'email': 'hi@gmail.com',
                                       'password': 'Hello123!'})
    assert resp.status_code == 200



#
# def test_delete_user(client):
#     resp = client.get('/delete/<id>/')
#     assert resp.status_code() == 500
#
#
# def test_delete_user_2(client):
#     resp = client.post('/delete/<id>/')
#     assert resp.status_code() == 500

# def test_home_bad_http_method(client):
#     resp = client.post('/')
#     assert resp.status_code == 405
#
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
