import rdflib
import requests
from SPARQLWrapper import SPARQLWrapper, JSON


class SemanticOperations:
    def __init__(self, rdf_database = 'drd', server_port = '3030'):
        self.rdf_database = rdf_database
        self.server_port = server_port

    def insertData(self, data):
        # Create a graph
        g = rdflib.Graph()
        EX = rdflib.Namespace("http://drd/")

        for resource in data:
            # Correctly create RDF terms
            subject = EX[resource[0]]  # Creates a URIRef: <http://drd/Device>
            predicate = EX[resource[1]]  # Creates a URIRef: <http://drd/hasFeature>
            obj = rdflib.Literal(resource[2])  # Creates a Literal: "Temperature"
            # Add triples to the graph
            g.add((subject, predicate, obj))

        # Define the Fuseki SPARQL endpoint for updates
        rdf_data = g.serialize(format='turtle')

        # Correct URL for data upload
        url = "http://localhost:"+self.server_port+"/"+self.rdf_database+"/data"

        # Headers for Turtle format
        headers = {
            "Content-Type": "text/turtle"
        }

        # POST the RDF data to the Fuseki server
        response = requests.post(url, data=rdf_data, headers=headers)

        # Check for errors
        if response.status_code == 200:
            print(f"Data successfully stored in Fuseki {response}")
        else:
            print(f"Failed to store data: {response.status_code} {response.reason}")

    def queryData(self):
        # Define the SPARQL endpoint for querying
        sparql = SPARQLWrapper("http://localhost:"+self.server_port+"/"+self.rdf_database+"/query")

        # Define a SPARQL query
        sparql.setQuery("""
            SELECT ?s ?p ?o
            WHERE {
                ?s ?p ?o .
            }
        """)
        sparql.setReturnFormat(JSON)

        # Execute the query
        results = sparql.query().convert()

        # Print the results
        for result in results["results"]["bindings"]:
            print(result)

        return results