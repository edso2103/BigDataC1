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

    todos = []
    interes = [['area'], ['rooms', 'name'], 
            ['baths', 'name'], ['price'],['locations', 'neighbourhoods', 'name']]
    tam = len(archivo['hits']['hits'])
    for k in range(tam):
        ims = archivo['hits']['hits'][k]['_source']['listing']
        datos = []
        for i in interes:
            for j in range(len(i)):
                sel = [[ims[i[j]][0] if type(ims.get(i[j])) == list else ims.get(i[j], ims)][0] if j ==0 else [sel[i[j]][0] if type(sel.get(i[j])) == list else sel.get(i[j], sel)][0]][0]
            datos.append(sel)
        todos.append(datos)
    

    for i in range(0,len(todos)):
    
        csv+=str(todos[i][0])
        csv+=','
        csv+=str(todos[i][1])
        csv+=','
        csv+=str(todos[i][2])
        csv+=','
        csv+=str(todos[i][3])
        csv+=','
        csv+=str(todos[i][4])
        csv+='\n'

    
    file_name2 ="landing-casas-final-"+ now.strftime("%Y-%m-%d") + ".csv"
    s3 = boto3.resource('s3')
    object = s3.Object('zappa-w3i5doh7f', file_name2)
    object.put(Body=csv)
