from flask import Flask, render_template, request, redirect, url_for
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
    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS rental_info (
                                                property_address VARCHAR(50) PRIMARY KEY,
                                                property_value int,
                                                condition VARCHAR(15),
                                                type VARCHAR(15))"""

        cur.execute(create_script)

        create_script2 = """CREATE TABLE IF NOT EXISTS tenant_info (
                                            tenant_id VARCHAR(100) NOT NULL PRIMARY KEY,
                                            owner VARCHAR(25),
                                            phone_number VARCHAR(18),
                                            arrival_date date,
                                            departure_date date,
                                            property_address VARCHAR(50) NOT NULL,
                                            constraint fk_address foreign key(property_address) 
                                            references rental_info(property_address))"""

        cur.execute(create_script2)

        create_script3 = """CREATE TABLE IF NOT EXISTS payment_info (
                                               payment_id VARCHAR(100) NOT NULL PRIMARY KEY,
                                               monthly_payment int,
                                               tenant_id VARCHAR(100) NOT NULL,
                                               loan_amount int,
                                               constraint fk_tenant foreign key(tenant_id) 
                                               references tenant_info(tenant_id))"""

        cur.execute(create_script3)

        cur.execute('select * from rental_info')
        value = len(cur.fetchall())
        cur.execute("select * from tenant_info")
        value2 = len(cur.fetchall())
        cur.execute("select * from payment_info")
        value3 = len(cur.fetchall())
        conn.commit()

        return render_template('main.html', num_houses=value, num_tenants=value2, num_payments=value3)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return ''

@app.route('/houses')
def houses():
    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS rental_info (
                                                       property_address VARCHAR(50) PRIMARY KEY,
                                                       property_value int,
                                                       condition VARCHAR(15),
                                                       type VARCHAR(15))"""

        cur.execute(create_script)

        cur.execute('select * from rental_info')
        value = cur.fetchall()
        conn.commit()

        return render_template('houses.html', value=value)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return ''


@app.route('/tenants')
def tenants():
    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS tenant_info (
                                                    tenant_id VARCHAR(100) NOT NULL PRIMARY KEY,
                                                    owner VARCHAR(25),
                                                    phone_number VARCHAR(18),
                                                    arrival_date date,
                                                    departure_date date,
                                                    property_address VARCHAR(50) NOT NULL,
                                                    constraint fk_address foreign key(property_address) 
                                                    references rental_info(property_address))"""

        cur.execute(create_script)

        cur.execute("select * from tenant_info")
        value = cur.fetchall()
        conn.commit()

        return render_template('tenants.html', value=value)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return ''

@app.route('/payments')
def payments():
    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS payment_info (
                                        payment_id VARCHAR(100) NOT NULL PRIMARY KEY,
                                        monthly_payment int,
                                        tenant_id VARCHAR(100) NOT NULL,
                                        loan_amount int,
                                        constraint fk_tenant foreign key(tenant_id) 
                                        references tenant_info(tenant_id))"""

        cur.execute(create_script)

        cur.execute("select * from payment_info")
        value = cur.fetchall()
        conn.commit()

        return render_template("payments.html", value=value)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return ''


@app.route('/add_rental_property')
def add_rental_property():
    return render_template('add_rental_property.html')

@app.route('/add_tenant_info')
def add_tenant_info():
    return render_template('add_tenant_info.html')

@app.route('/add_payment_info')
def add_payment_info():
    return render_template('add_payment_info.html')

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

@app.route('/add_houses', methods=['POST'])
def add_houses():
    output = request.get_json()
    result = json.loads(output)

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

        insert_script = 'INSERT INTO rental_info VALUES (%s, %s, %s, %s)'
        for key in result.keys():
            insert_lst.append(result[key])
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

@app.route('/add_tenants', methods=['POST'])
def add_tenants():
    output = request.get_json()
    result = json.loads(output)

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

        insert_script = 'INSERT INTO tenant_info VALUES (%s, %s, %s, %s, %s, %s)'
        for key in result.keys():
            insert_lst.append(result[key])
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

@app.route('/add_payments', methods=['POST'])
def add_payments():
    output = request.get_json()
    result = json.loads(output)

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

        insert_script = 'INSERT INTO payment_info VALUES (%s, %s, %s, %s)'
        for key in result.keys():
            insert_lst.append(result[key])
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

@app.route('/delete_rental_property', methods=['POST'])
def delete_rental_property():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    delete_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            delete_lst.append(result[key])
            break

        delete_script = 'DELETE FROM rental_info WHERE property_address = %s'
        delete_record = (delete_lst[0],)
        cur.execute(delete_script, delete_record)
        cur.execute("select * from rental_info")
        data = cur.fetchall()
        conn.commit()

        return render_template("houses.html", value=data)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result

@app.route('/delete_tenant_info', methods=['POST'])
def delete_tenant_info():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    delete_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            delete_lst.append(result[key])
            break

        delete_script = 'DELETE FROM tenant_info WHERE tenant_id = %s'
        delete_record = (delete_lst[0],)
        cur.execute(delete_script, delete_record)
        cur.execute("select * from tenant_info")
        data = cur.fetchall()
        conn.commit()

        return render_template("tenants.html", value=data)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result

@app.route('/delete_payment_info', methods=['POST'])
def delete_payment_info():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    delete_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            delete_lst.append(result[key])
            break

        delete_script = 'DELETE FROM payment_info WHERE payment_id = %s'
        delete_record = (delete_lst[0],)
        cur.execute(delete_script, delete_record)
        cur.execute("select * from payment_info")
        data = cur.fetchall()
        conn.commit()

        return render_template("payments.html", value=data)

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result


@app.route('/update_houses', methods=['POST'])
def update_houses():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    update_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            update_lst.append(result[key])

        update_script = """UPDATE rental_info SET property_value = %s,
                        condition = %s, type = %s WHERE property_address = %s"""
        update_lst2 = [update_lst[1], update_lst[2], update_lst[3], update_lst[0]]
        cur.execute(update_script, update_lst2)

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result

@app.route('/update_tenants', methods=['POST'])
def update_tenants():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    update_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            update_lst.append(result[key])

        update_script = """UPDATE tenant_info SET owner = %s, phone_number = %s,
                        arrival_date = %s, departure_date = %s, property_address = %s
                        WHERE tenant_id = %s"""
        update_lst2 = [update_lst[1], update_lst[2], update_lst[3],
                       update_lst[4], update_lst[5], update_lst[0]]
        cur.execute(update_script, update_lst2)

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return result

@app.route('/update_payments', methods=['POST'])
def update_payments():
    output = request.get_json()
    result = json.loads(output)

    hostname = 'localhost'
    database = 'Rental_management'
    username = 'postgres'
    pwd = '&1<6.,O7!$O9f*..*E5'
    port_id = 5432
    conn = None
    cur = None
    update_lst = []
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=username,
            password=pwd,
            host=hostname,
            port=port_id)

        cur = conn.cursor()

        for key in result.keys():
            update_lst.append(result[key])

        update_script = """UPDATE payment_info SET monthly_payment = %s, 
                        tenant_id = %s, loan_amount = %s WHERE payment_id = %s"""
        update_lst2 = [update_lst[1], update_lst[2], update_lst[3], update_lst[0]]
        cur.execute(update_script, update_lst2)

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
    app.run(debug=True, port=5001)