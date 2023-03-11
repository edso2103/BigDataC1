import json
from urllib.request import urlopen
import boto3
import requests
import datetime
def f(event, context):
    
    url = 'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
    data = {"filter":
           {"offer":
           {"slug":["sell"]},
           "path":"zona-chapinero bogota"},
           "fields":
           {"exclude":[],
            "facets":[],
            "include":["area","baths.id","baths.name","baths.slug",
                      "locations.neighbourhoods.fr_place_id",
                      "locations.neighbourhoods.name",
                       "price",
                       "rooms.id","rooms.name"],"limit":25,
           "offset":0,"ordering":[],"platform":41,"with_algorithm":True}}
        
    headers = {
      'Content-Type': 'application/json',
      'Connection': 'keep-alive',
    }
    
    response = requests.post(url, json=data, headers=headers)
    now = datetime.datetime.now()
    file_name ="landing-casas-"+ now.strftime("%Y-%m-%d") + ".txt"
    
    s3 = boto3.client('s3')
    s3.put_object(
    Bucket='bucket2103',
    Key=file_name,
    Body=response.content,
    ContentType='text/plain')




    
    
    