#!/usr/bin/env python
#
import requests
import pprint
from io import StringIO

# 设定你的SPARQL端点
SPARQL_ENDPOINT = 'http://localhost:3030/s2484724-epcc/sparql'

# 创建一个字符串缓冲区来构建SPARQL查询
sBuffer = StringIO()

# 查询并打印数据集中的所有三元组
sBuffer.write("SELECT ?s ?p ?o where {?s ?p ?o}")
sparql_query = sBuffer.getvalue()
print(f'SPARQL query -> {sparql_query}')
response = requests.post(SPARQL_ENDPOINT, data={'query': sparql_query})
jsonResponse = response.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())

print()
print('*********************')
print()

# 查询RDF数据中的人名
sBuffer.truncate(0)
sBuffer.write('PREFIX foaf: <http://xmlns.com/foaf/0.1/> \n')
sBuffer.write("SELECT ?name WHERE {?person foaf:name ?name}")
sparql_query = sBuffer.getvalue()
print(f'SPARQL query -> {sparql_query}')
#response = requests.post(SPARQL_ENDPOINT, data={'query': sparql_query})
response = requests.post(SPARQL_ENDPOINT, data={'query': sparql_query})
if response.status_code == 200:
    try:
        jsonResponse = response.json()
        pp.pprint(jsonResponse)
    except simplejson.errors.JSONDecodeError:
        print("Failed to decode JSON from response.")
        print(response.text)
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    print(response.text)

#jsonResponse = response.json()
#pp.pprint(response.json())

print()
print('*********************')
print()

# 查询住在爱丁堡附近的人
sBuffer.truncate(0)
sBuffer.write('PREFIX foaf: <http://xmlns.com/foaf/0.1/> \n')
sBuffer.write('PREFIX dbpedia: <http://dbpedia.org/resource/#> \n')
sBuffer.write("SELECT ?name WHERE {?person foaf:based_near dbpedia:Edinburgh; foaf:name ?name}")
sparql_query = sBuffer.getvalue()
print(f'SPARQL query -> {sparql_query}')
response = requests.post(SPARQL_ENDPOINT, data={'query': sparql_query})
jsonResponse = response.json()
pp.pprint(response.json())
