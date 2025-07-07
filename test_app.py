import json
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data

def test_add():
    tester = app.test_client()
    response = tester.post('/api/add', 
        data=json.dumps({'a': 3, 'b': 4}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 7

