import ast

def test_fetch_any_orders(client):
    response = client.get('/orders')
    assert response.status_code == 200

def test_create_(client):
    response = client.post('/orders?name=test&description=test')
    data = response.data.decode()
    output_dict = ast.literal_eval(data)

    assert response.status_code == 200
    assert output_dict['description'] == 'test'
    assert output_dict['name'] == 'test'


# Incomplete. TODO: more tests like these for each of the functions. make a function that cleans a database fully after making test queries.