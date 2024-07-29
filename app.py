from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://rody:CAwpXsTvoU1FpEhTg4TIYZyuqD1IBXky@dpg-cqjqlqmehbks73cgrjo0-a/rody")
    conn.close()
    return "DB Connection Successful!"
@app.route('/')
def hello_world():
    return 'Hello, World! from Rody Bertolini in 3308'
