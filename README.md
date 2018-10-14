# REST-Api-using-Flask
REST (REpresentational State Transfer) is an architectural design for creating web based services taking certain constraints into consideration. REST is used mainly used over HTTP when used for web APIs. In a RESTful web service, requests made to a web resource's Uniform Resource Identifier (URI) and that returns a response with a payload in some format (common ones include HTML, XML and JSON). When HTTP is used, the operations which can be performed on the web resources are GET, POST, PUT, DELETE. 

# Implemetation Details:
Here, a REST API is implemented in Python using Flask framework. It is connected to a PostgreSQL database and runs on the localhost. For any other database and/or server, the appropriate values need to be changed in the server.py file. 

- In our dummy database (a place holder DATABASE_NAME is used instead of the actual db name), there is an 'accounts' table which has account_id as the primary key.
- config.py: Contains a dictionary containing the database name. Further database names can be added as values in the dictionary. 
- server.py: Contains two GET methods. The GetAll method retrieves all records in the 'accounts' table. When the GetAll method is called, 'SELECT * FROM accounts' is called. The route defined for this method is '/accounts'. The GetOne method returns a particular account detail based on account_id passed as an argument by the user. The route for this method is '/accounts/<account_id>'. This method executes the query 'SELECT * FROM accounts WHERE account_id = <account_id>' where <account_id' is provided by the user. 

# To Do:
Methods yet to be implemeted:
- POST
- PUT
- DELETE
