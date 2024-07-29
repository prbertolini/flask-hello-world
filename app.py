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
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://rody:CAwpXsTvoU1FpEhTg4TIYZyuqD1IBXky@dpg-cqjqlqmehbks73cgrjo0-a/rody")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
            ''')
    conn.commit()
    conn.close()
    return "Basketball table created!"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://rody:CAwpXsTvoU1FpEhTg4TIYZyuqD1IBXky@dpg-cqjqlqmehbks73cgrjo0-a/rody")
    cur = conn.cursor()
    cur.execute('''
           INSERT INTO Basketball (First, Last, City, Name, Number)
Values
('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
           ''')
           conn.commit()
           conn.close()
    return "Successful DB insert!"