###
#       This is the init file for the manager 
#       of the database
#
###

from classes import Client

client = Client()

db = client.add_db("Users")

db = client.get_db()

colls = db.get_collections()

colls[0].add_data(id = "2", name = "Get with me")
colls[0].delete_data(colls[0].data)