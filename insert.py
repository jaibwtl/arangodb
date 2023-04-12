from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('test', username='root', password='admin123')

# Insert using AQL 
db.aql.execute('INSERT {_key:@key, name: @name, age:@age} INTO students', bind_vars={'key': 'testing','name': 'helloAQL', 'age': 33})

# Execute an AQL query. This returns a result cursor.
cursor = db.aql.execute('FOR doc IN students RETURN doc')

# Iterate through the cursor to retrieve the documents.
student_names = [document['name'] for document in cursor]

for x1 in student_names:
    print(">>>", x1)
