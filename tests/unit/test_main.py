def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Статус ПК'.encode() in response.data


def test_index_with_empty_db(client_empty_db):
    response = client_empty_db.get('/')

    assert response.status_code == 200
    assert 'Похоже что никаких данных еще нет'.encode() in response.data
