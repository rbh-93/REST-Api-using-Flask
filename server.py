from flask import Flask
from flask_restful import Resource, Api
from config import configDict
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

# Give appropriate Username, Password and Host Name of the Database
# In case it is not PostgreSQL, change 'postgresql' part
db_connect = create_engine('postgresql://USERNAME:PASSWORD@LOCALHOST/' + configDict['db_name'])
app = Flask(__name__)
api = Api(app)


# Get Method to get all data from a table
# Here the table name is 'accounts'
# Put appropriate table name in place of 'accounts'
class GetAll(Resource):
    def get(self):
        conn = db_connect.connect()  # Connect to database
        query = conn.execute("Select * from accounts")  # This line performs query and returns the result
        return {'accounts': [dict(zip(tuple(str(i[0]) for i in query.cursor.description), j)) for j in
                             query.cursor.fetchall()]}  # Fetches all columns


# Get method to get data by particular value from a table
# Here the query is performed on the Primary Key account_id
# Put appropriate search key name in place of account_id
class GetOne(Resource):
    def get(self, account_id):
        conn = db_connect.connect()
        query = conn.execute("select * from accounts where account_id =%d " % int(account_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(GetAll, '/accounts')  # Route_1 for GetAll()
api.add_resource(GetOne, '/accounts/<account_id>')  # Route_2 for GetOne()

if __name__ == '__main__':
    app.run(port='5002')
