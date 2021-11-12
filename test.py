import os
import tempfile
from Group5.routes import render_template

import pytest

from Group5 import app


@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_home_bad_http_method(client):
    resp = client.post('/')
    assert resp.status_code == 405

def test_account(client):
    resp = client.post('/account', data='something')
    assert resp.status_code == 400

def test_account(client):
    resp = client.post('/account')
    assert resp.status_code == 400

