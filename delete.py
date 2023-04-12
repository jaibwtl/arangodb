from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('test', username='root', password='admin123')

# Update using AQL 
db.aql.execute('REMOVE {_key: @key} IN students', bind_vars={'key': 'testing'})
