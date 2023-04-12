from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('test', username='root', password='admin123')

# Update using AQL 
db.aql.execute('UPDATE {_key: @key} WITH {age: @age} IN students', bind_vars={'key': 'testing', 'age': 100})
