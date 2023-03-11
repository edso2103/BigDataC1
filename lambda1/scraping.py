import requests

def descargar(url):
    response=requests.get(url)
    return response
