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

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://rody:CAwpXsTvoU1FpEhTg4TIYZyuqD1IBXky@dpg-cqjqlqmehbks73cgrjo0-a/rody")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()
    
    table = "<table border='1'>"
    table += '<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>'
    for row in records:
        table += "<tr>"
        for col in row:
            table += f'<td>{col}</td>'
        table +="</tr>"
    table += "</table>"
    return table