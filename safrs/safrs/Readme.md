## Source Code Implementation details

This readme describes on a high level how safrs_rest is implemented (for low level details you can check the code and comments)
This directory contains the code to construct documented REST APIs:
- [config.py](config.py) : Configurable options
- [db.py](db.py) : sqlalchemy database definitions
- [jsonapi.py](jsonapi.py) : REST web bindings. The source code contains a lot of references to the jsonapi specifiation.
- [safrs_types.py](safrs_types.py) : Custome database types (eg. SAFRSSHA256HashID in case you'd like to use a SHA256 hash instead of UUID is primary key)
- [swagger_doc.py](swagger_doc.py) : API documentation, implemented as decorators
- [errors.py](errors.py) : Exceptions

### Variables for SQLAlchemy, Flask Logging

Some variables have to be globally (cross-module) defined:
- app : flask app
- db  : flask-sqlalchemy database instance
- log : python logging instances

### SAFRSBase

- \_\_new\_\_
- \_\_init\_\_
- get_list
- clone
- sample
- sample_id
- get_swagger_doc: generate swagger object model and POST method documentation.

### Api

The flask_restful_swagger_2 Api class has been extended with following methods:
- ```expose_object``` Create endpoints to access the SAFRSBase classes
- ```expose_relationship```

In addition to creating endpoints, these functions also apply the ```api_decorator``` decorators:
- implement cors
- generate swagger documentation
- wrap the implemented HTTP methods (get, post, put, etc. ) to commit to the database after a request and
- implement exception handling

The standard Api ```add_resource``` method has been modified to parse the parameters generated by the SAFRSBase swagger methods

### SAFRSRestAPI
SAFRSRestAPI is a superclass for dynamically generated flask-restful endpoints.

### SAFRSRestRelationshipAPI

### Swagger Documentation

- ```swagger_doc```
- ```swagger_relationship_doc```

### Serialization

- ```safrs_serialize```
- The restful ```SAFRSJSONEncoder``` class calls the SAFRSBase subclass to_dict method to convert object attributes to a python dictionary which is then converted to JSON.

## Var

I'm pretty happy with the design and quality of code. Given the benefit of hindsight however, a lot of things can be improved :) .