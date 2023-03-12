import boto3
import json
import csv
import datetime

def lambda_handler(event, context):
    
    now = datetime.datetime.now()
    file_name ="landing-casas-"+ now.strftime("%Y-%m-%d") + ".txt"
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('bucket2103')
    obj = bucket.Object(file_name)
    body = obj.get()['Body'].read()
    archivo=json.loads(body)
    
    csv='Area,#Habitaciones,#Banhos,Precio,Barrio\n'

    data = []
    interes = [['area'], ['rooms', 'name'], 
            ['baths', 'name'], ['price'],['locations', 'neighbourhoods', 'name']]
    tam = len(archivo['hits']['hits'])
    for i in range(tam):
        ims = archivo['hits']['hits'][i]['_source']['listing']
        datos = []
        for j in interes:
            for k in range(len(j)):
                r = [[ims[j[k]][0] if type(ims.get(j[k])) == list else ims.get(j[k], ims)][0] if k ==0 else [r[j[k]][0] if type(r.get(j[k])) == list else r.get(j[k], r)][0]][0]
            datos.append(r)
        data.append(datos)
    

    for i in range(0,len(data)):
    
        csv+=str(data[i][0])
        csv+=','
        csv+=str(data[i][1])
        csv+=','
        csv+=str(data[i][2])
        csv+=','
        csv+=str(data[i][3])
        csv+=','
        csv+=str(data[i][4])
        csv+='\n'

    
    file_name2 ="landing-casas-final-"+ now.strftime("%Y-%m-%d") + ".csv"
    s3 = boto3.resource('s3')
    object = s3.Object('zappa-w3i5doh7f', file_name2)
    object.put(Body=csv)
