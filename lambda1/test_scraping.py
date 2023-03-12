from apps import datos
import json


def test_datos(mocker):
    url = "https://api.fincaraiz.com.co/document/api/1.0/listing/search"

    mocker.patch('requests.post', return_value='23')
    respuesta = datos(url)

    assert isinstance(respuesta, str)
    assert respuesta[0] == '2'
    assert int(respuesta[0]) + int(respuesta[1]) == 5

    mock = mocker.patch('requests.post')
    mock.return_value = '{"casa":{"area":35,"banhos":3,"price":320000000}}'
    respuesta = json.loads(datos(url))
    print(respuesta)
    assert respuesta["casa"]["area"] == 35
