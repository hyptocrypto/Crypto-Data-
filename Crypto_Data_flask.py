# Crypto_Data.py

from flask import Flask, request, render_template, jsonify
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)


#########  Webpage -html- routes ##########

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/orderbook_bias')
def orderbook_bias():
    return render_template('orderbook_bias.html')

@app.route('/trader_bias')
def trader_bias():
    return render_template('trader_bias.html')

@app.route('/reddit_posts')
def reddit_posts():
    return render_template('reddit_posts.html')





######  DB CONNECTION #########

class DB_Querry:
    
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        
        self.con = psycopg2.connect( host = self.host,
                        database = self.database,
                        user = self.user,
                        password = self.password,
                        port = self.port)
        
        self.cur = self.con.cursor()
    
    # Method to return all values form column passed as argument
    def querry_column(self, column):
        
        try:
            self.cur.execute(sql.SQL('SELECT {} FROM crypto_data;').format(sql.Identifier(column)))
            data = self.cur.fetchall()
            data = [i[0] for i in data]
            return{column: data}
            cur.close()
            con.close()
        except:
            return 'Invalid Querry Paramater'

   # Method to return all values from date passed as argument     
    def querry_date(self, date):
        
        try:
            self.cur.execute(sql.SQL("SELECT * FROM crypto_data WHERE date = '{}'; ").format(sql.Identifier(date)))
            data = self.cur.fetchall()
            return {date: data}
            cur.close()
            con.close()
        except:
            return 'Invalid Querry Paramater'

 
# DB_Querry instance for AWS_RDS
crypto_data_db = DB_Querry(os.environ.get('DB_HOST'), 
                           'postgres', 'postgres', os.environ.get('DB_PASS'), '5432')












# API Routes 

@app.route('/api/v1/column/<column>', methods=['GET'])
def API_column(column):
    return crypto_data_db.querry_column(column)
    

@app.route('/api/v1/date/<date>', methods=['GET'])
def API_date(date):
    return crypto_data_db.querry_date(date)












if __name__ == '__main__':
    app.run()
