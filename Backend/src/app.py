from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/python-flask-vuejs"
mongo = PyMongo(app)

db = mongo.db.users

@app.route("/users", methods=["POST"])
def createUser():
    id = db.insert_one({
        'name': request.json['name'],
        'lastname': request.json['lastname'],
        'email': request.json['email'],
        'password': request.json['password'],
    }).inserted_id
    print(str(ObjectId(id)))
    return jsonify({'msg': 'User created successfully', 'id': str(id)})

@app.route("/users", methods=["GET"])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(doc['_id']),
            'name': doc['name'],
            'lastname': doc['lastname'],
            'email': doc['email']
        })
    return jsonify(users)

@app.route("/users/<id>", methods=["GET"])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(user['_id']),
        'name': user['name'],
        'lastname': user['lastname'],
        'email': user['email']
    })

@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted successfully'})

@app.route("/users/<id>", methods=["PUT"])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'lastname': request.json['lastname'],
        'email': request.json['email'],
        'password': request.json['password']
    }})
    return jsonify({'msg': 'User updated successfully'})

if __name__ == "__main__":
    app.run(debug=True)