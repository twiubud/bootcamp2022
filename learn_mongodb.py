import pymongo

client = pymongo.MongoClient("mongodb+srv://twi:linuxlinux@cluster0.ukt32xi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"john",
    "email" : "john@ineuron.ai",
    "surname" : "ryan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)