def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'1654538958' in response.data