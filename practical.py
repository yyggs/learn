import rdflib
from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

# Initialize the RDF graph
g = Graph()

# Fetch and parse the RDF data from the SPARQL endpoint
g.parse(SPARQL_ENDPOINT, format="application/rdf+xml")

# Query and print all the triples in the dataset
query = prepareQuery("SELECT ?s ?p ?o WHERE {?s ?p ?o}")
print(f'SPARQL query -> {query}')
for row in g.query(query):
    print(row)

print()
print('*********************')
print()

# Query RDF data for people's names
query = prepareQuery(
    '''
    PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
    SELECT ?name WHERE {?person foaf:name ?name}
    '''
)
print(f'SPARQL query -> {query}')
for row in g.query(query):
    print(row)

print()
print('*********************')
print()

# Query for people who live near Edinburgh
query = prepareQuery(
    '''
    PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
    PREFIX dbpedia: <http://dbpedia.org/resource/#> 
    SELECT ?name WHERE {?person foaf:based_near dbpedia:Edinburgh; foaf:name ?name}
    '''
)
print(f'SPARQL query -> {query}')
for row in g.query(query):
    print(row)
