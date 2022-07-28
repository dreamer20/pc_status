def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Статус ПК'.encode() in response.data
