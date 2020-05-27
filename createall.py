import flask_s3
from Crypto_Data_flask import app 
flask_s3.create_all(app, user = 'AKIA4KONH5DHVJSFI2M3', password = 'LmIDdB53tZNg4QhLnuyRWsoLWVl5KhXn0q/MSbR1', bucket_name = 'crypto-data-bucket', location = 'us-east-1')