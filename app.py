from flask import Flask, render_template, request
import json
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/houses')
def houses():
    return render_template('houses.html')

@app.route('/tenants')
def tenants():
    return render_template('tenants.html')

@app.route('/payments')
def payments():
    return render_template('payments.html')

@app.route('/test', methods=['POST'])
def test():
    result = request.form.to_dict()

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    insert_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS signup_info (
                                    username VARCHAR(59) PRIMARY KEY,
                                    password VARCHAR(25) NOT NULL,
                                    email VARCHAR(59) NOT NULL)"""

        cur.execute(create_script)

        insert_script = 'INSERT INTO signup_info VALUES (%s, %s, %s)'
        for key in result.keys():
            insert_lst.append(result[key])

        cur.execute('SELECT * FROM signup_info')
        data = cur.fetchall()

        if len(data) == 0:
            cur.execute(insert_script, tuple(insert_lst))
            conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result

if __name__ == "__main__":
    app.run(debug=True)