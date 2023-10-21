#!/usr/bin/env python

import rdflib
from rdflib.plugins.sparql import prepareQuery
import pprint

# 设定你的SPARQL端点
SPARQL_ENDPOINT = 'http://localhost:3030/s2484724-epcc/sparql'

g = rdflib.Graph()
g.parse(SPARQL_ENDPOINT, format="xml")

# 查询并打印数据集中的所有三元组
query_all_triples = prepareQuery("""
SELECT ?s ?p ?o WHERE {
    ?s ?p ?o
}
""", initNs = {"rdf": rdflib.RDF.NAMESPACE})

for s, p, o in g.query(query_all_triples):
    print(s, p, o)

print()
print('*********************')
print()

# 查询RDF数据中的人名
query_names = prepareQuery("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?name WHERE {
    ?person foaf:name ?name
}
""", initNs = {"foaf": rdflib.Namespace("http://xmlns.com/foaf/0.1/")})

for row in g.query(query_names):
    print(row[0])

print()
print('*********************')
print()

# 查询住在爱丁堡附近的人
query_edinburgh = prepareQuery("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX dbpedia: <http://dbpedia.org/resource/> 
SELECT ?name WHERE {
    ?person foaf:based_near dbpedia:Edinburgh;
           foaf:name ?name
}
""", initNs = {"foaf": rdflib.Namespace("http://xmlns.com/foaf/0.1/")})

for row in g.query(query_edinburgh):
    print(row[0])
