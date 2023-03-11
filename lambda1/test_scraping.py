from scraping import descargar

def test_descargar(mocker):
    url="http://mipagina.com"
    mocker.patch("requests.get", return_value="...html...")
    response=descargar(url)
    assert response=="...html..."
