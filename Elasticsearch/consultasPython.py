from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

client = Elasticsearch()

#Consulta 1. Obtenemos el nombre y el id del restaurante de los 100 primeros campos ordenados de forma descendente por el nombre
#Ejecutar previamente:
#curl -XPUT 'localhost:9200/lugares/restaurantes/_mapping/?pretty' -H 'Content-Type: application/json' -d' {"properties": {"name": {"type":"text","fielddata": true}}}'

s = client.search(index="lugares", doc_type="restaurantes",
                  body={"query": {"match_all": {}} ,
                        "sort": {"name": {"order": "desc"}},
                        "from": 1, "size": 5 })
restaurantes = s['hits']['hits']

for restaurante in restaurantes:
    print(restaurante['_source']['name'])

#Consulta 2. Obtenemos todos los campos del restaurante que tenga un nombre específico

s = (Search(using=client, index="lugares")
    .query("match", name="Penelope"))

response = s.execute()

for i in response:
    print(i['restaurant_id'] +" "+i['name'] +" "+ i['borough'] + " ")


#Consulta 3. Obtenemos los campos del restaurante de un barrio específico

s = (Search(using=client, index="lugares")
    .query("match", borough="Manhattan"))

response = s.execute()

for i in response:
    print(i['restaurant_id'] +" "+i['name'] +" "+ i['borough'] + " ")


# Consulta 4. Obtener restaurantes japoneses


s = (Search(using=client, index="lugares")
    .query("match", cuisine="Japanese"))

response = s.execute()

for i in response:
    print(i['restaurant_id'] +" "+i['name'] +" "+ i['cuisine'] + " ")



#Consulta 5. Obtener restaurantes solo de Manhattan y que no sean Japoneses ni Chinos

m.query = Q('bool', must=[Q('match', borough="Manhattan")], must_not = [Q('match', cuisine="Japanese")])

s = (Search(using=client, index="lugares")
     .m.query.query())

response = s.execute()

for i in response:
    print(i['restaurant_id'] +" "+i['name'] +" "+ i['cuisine'] + " ")
	
#NUEVO	
s =client.search(index="lugares", doc_type="restaurantes",
                  body={ "query":{ "bool": {"must": {"match": {"borough": "Manhattan"}},
                                            "must_not": [
                                                { "match": { "cuisine": "Japanese" } },
                                                { "match": { "cuisine": "Chinese" } }] }},
                         "sort": { "name": { "order": "desc" } }})

restaurantes = s['hits']['hits']

for restaurante in restaurantes:
    print(restaurante['_source']['name'] +
          "-"+ restaurante['_source']['borough'] + 
          "-"+ restaurante['_source']['cuisine'])

