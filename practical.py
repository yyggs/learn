#!/usr/bin/env python

from rdflib import Graph, Namespace
import pprint

# 设定你的SPARQL端点
SPARQL_ENDPOINT = 'http://localhost:3030/s2484724-epcc/sparql'

# 创建RDF图形实例
g = Graph()

# 加载RDF数据
g.parse(SPARQL_ENDPOINT, format="application/rdf+xml")

# 使用RDFLib和SPARQL查询数据
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
DBPEDIA = Namespace("http://dbpedia.org/resource/")

# 查询并打印数据集中的所有三元组
for s, p, o in g.triples((None, None, None)):
    print(s, p, o)

print()
print('*********************')
print()

# 查询RDF数据中的人名
q1 = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
SELECT ?name WHERE {
    ?person foaf:name ?name
}
"""
for row in g.query(q1):
    print(row)

print()
print('*********************')
print()

# 查询住在爱丁堡附近的人
q2 = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX dbpedia: <http://dbpedia.org/resource/> 
SELECT ?name WHERE {
    ?person foaf:based_near dbpedia:Edinburgh;
           foaf:name ?name
}
"""
for row in g.query(q2):
    print(row)
