import rdflib
import pprint

graph = rdflib.Graph()
graph.parse("foaf_example.ttl", format="turtle")

sparql_query = """
SELECT ?s ?p ?o WHERE {
    ?s ?p ?o
}
"""
results = graph.query(sparql_query)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)

print()
print('*********************')
print()

sparql_query = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name WHERE {
    ?person foaf:name ?name
}
"""
results = graph.query(sparql_query)
pp.pprint(list(results))

print()
print('*********************')
print()

sparql_query = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dbpedia: <http://dbpedia.org/resource/#>
SELECT ?name WHERE {
    ?person foaf:based_near dbpedia:Edinburgh.
    ?person foaf:name ?name
}
"""
results = graph.query(sparql_query)
pp.pprint(list(results))
