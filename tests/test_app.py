from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_ziruuu.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/')  # act (ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'ola mundo'} # assert
