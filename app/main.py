from flask import Flask, request, jsonify
#import dnspython
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

# NOTE En CMD correr esto para iniciar el entorno virtual 
# TODO Run .\Scripts\activate.bat

# NOTE user: sagalo Password: xvT2zg3OIcWftSQD
#
#

# ANCHOR Instancia 
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://sagalo:xvT2zg3OIcWftSQD@kboom.wj2u1.mongodb.net/KBoom?retryWrites=true&w=majority'
mongo = PyMongo(app)

# ANCHOR configuacion
CORS(app)

# ANCHOR conexion a la base de datos
db = mongo.db.points

# SECTION Routes
@app.route('/points', methods=['POST'])
def createPoint():
    try:
        point = db.find_one_and_update({'user': request.json['user']},{'$set':{'dataYx': request.json['dataYx'],'dataYv': request.json['dataYv'], 'dataX': request.json['dataX'],'dataYxm2': request.json['dataYxm2'],'dataYvm2': request.json['dataYvm2'], 'dataXm2': request.json['dataXm2'],'dataYxm3': request.json['dataYxm3'],'dataYvm3': request.json['dataYvm3'], 'dataXm3': request.json['dataXm3']}})
        return (str(ObjectId(point['_id']))) 
    except:
        id = db.insert({
            'user': request.json['user'],
            'dataYx': request.json['dataYx'],
            'dataYv': request.json['dataYv'],
            'dataX': request.json['dataX'],
            'dataYxm2': request.json['dataYxm2'],
            'dataYvm2': request.json['dataYvm2'],
            'dataXm2': request.json['dataXm2'],
            'dataYxm3': request.json['dataYxm3'],
            'dataYvm3': request.json['dataYvm3'],
            'dataXm3': request.json['dataXm3']
        })
        return (str(ObjectId(id))) 


# ANCHOR GetPointUser
@app.route('/point/<user>', methods=['GET'])
def getUser(user):
    point = db.find_one({'user': user})
    return jsonify({
        '_id': str(ObjectId(point['_id'])),
        'dataYx': point['dataYx'],
        'dataYv': point['dataYv'],
        'dataX': point['dataX'],
        'dataYxm2': point['dataYxm2'],
        'dataYvm2': point['dataYvm2'],
        'dataXm2': point['dataXm2'],
        'dataYxm3': point['dataYxm3'],
        'dataYvm3': point['dataYvm3'],
        'dataXm3': point['dataXm3'],
    })

# ANCHOR GetPoints
@app.route('/users', methods=['GET'])
def getUsers():
    points = []
    for doc in db.find():
        points.append({
            '_id': str(ObjectId(doc['_id'])),
            'user': doc['user'],
            'data': doc['data'],
        })
    return jsonify(points)

# ANCHOR DeleteUser
@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msj': 'usuario eliminado'})

# !SECTION 
# if __name__ == '__main__':
#     app.run(debug=True)
#    
