import boto3
import datetime
import json


def lambda_handler(event, context):
    now = datetime.datetime.now()
    file_name = "landing-casas-" + now.strftime("%Y-%m-%d") + ".txt"

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('bucket2103')
    obj = bucket.Object(file_name)
    body = obj.get()['Body'].read()
    archivo = json.loads(body)

    csv_data = 'Area,#Habitaciones,#Banhos,Precio,Barrio,FechaDescarga\n'

    data = []
    interes = [['area'], ['rooms', 'name'],
               ['baths', 'name'], ['price'],
               ['locations', 'neighbourhoods', 'name']]
    tam = len(archivo['hits']['hits'])
    for i in range(tam):
        ims = archivo['hits']['hits'][i]['_source']['listing']
        datos = []
        for j in interes:
            for k in range(len(j)):
                if k == 0:
                    result = ([ims[j[k]][0] if type(ims.get(j[k])) ==
                              list else ims.get(j[k], ims)][0])
                else:
                    result = ([result[j[k]][0] if type(result.get(j[k])) ==
                              list else result.get(j[k], result)][0])

            datos.append(result)
        data.append(datos)

    for i in range(0, len(data)):
        csv_data += str(data[i][0])
        csv_data += ','
        csv_data += str(data[i][1])
        csv_data += ','
        csv_data += str(data[i][2])
        csv_data += ','
        csv_data += str(data[i][3])
        csv_data += ','
        csv_data += str(data[i][4])
        csv_data += ','
        csv_data += str(now.strftime("%Y-%m-%d"))
        csv_data += '\n'

    file_name2 = "landing-casas-final-" + now.strftime("%Y-%m-%d") + ".csv"
    s3 = boto3.resource('s3')
    obj = s3.Object('zappa-w3i5doh7f', file_name2)
    obj.put(Body=csv_data)
