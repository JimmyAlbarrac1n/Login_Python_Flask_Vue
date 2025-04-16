from flask import Flask, request, jsonify, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'clave_secreta_1234567890'  

app.config["MONGO_URI"] = "mongodb://localhost:27017/python-flask-vuejs"
mongo = PyMongo(app)

db = mongo.db.users

@app.route("/users", methods=["POST"])
def createUser():
    # Hashear la contraseña antes de guardarla
    hashed_password = generate_password_hash(request.json['password'])
    id = db.insert_one({
        'name': request.json['name'],
        'lastname': request.json['lastname'],
        'email': request.json['email'],
        'password': hashed_password,
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

@app.route("/login", methods=["POST"])
def login():
    email = request.json['email']
    password = request.json['password']
    
    user = db.find_one({'email': email})
    
    if not user:
        return jsonify({'msg': 'Invalid credentials'}), 401
    
    # Intenta ambos métodos de verificación
    is_password_valid = False
    
    # Primero verifica si es una contraseña hasheada
    if user['password'].startswith('pbkdf2:sha256:') or user['password'].startswith('scrypt:'):
        is_password_valid = check_password_hash(user['password'], password)
    # Si no es hash, compara directamente (contraseñas antiguas)
    else:
        is_password_valid = (user['password'] == password)
        # Opcional: actualizar automáticamente a hash
        if is_password_valid:
            db.update_one(
                {'_id': user['_id']},
                {'$set': {'password': generate_password_hash(password)}}
            )
    
    if is_password_valid:
        session['user_id'] = str(user['_id'])
        return jsonify({
            'msg': 'Login successful',
            'user': {
                '_id': str(user['_id']),
                'name': user['name'],
                'lastname': user['lastname'],
                'email': user['email']
            }
        })
    
    return jsonify({'msg': 'Invalid credentials'}), 401
@app.route("/logout", methods=["POST"])
def logout():
    session.pop('user_id', None)
    return jsonify({'msg': 'Logged out successfully'})

@app.route("/check-auth", methods=["GET"])
def check_auth():
    if 'user_id' in session:
        user = db.find_one({'_id': ObjectId(session['user_id'])})
        return jsonify({
            'authenticated': True,
            'user': {
                '_id': str(user['_id']),
                'name': user['name'],
                'lastname': user['lastname'],
                'email': user['email']
            }
        })
    return jsonify({'authenticated': False})

if __name__ == "__main__":
    app.run(debug=True)