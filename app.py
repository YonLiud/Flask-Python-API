import os
import sqlite3
from flask import Flask,redirect,url_for,render_template,request, jsonify, send_from_directory
import requests
import logging
from api_calls import *

app=Flask(__name__)
conn = sqlite3.connect('database.db')
accounts = []
table_name = "contacts"

def setup(conn):
    cursor = conn.cursor()
    desc =  cursor.execute("pragma table_info('" + table_name + "')").fetchall()
    for i in range(1, cursor.execute('SELECT COUNT(*) from '+ table_name).fetchall()[0][0]+1):
        account = {}
        name = ""
        value = []
        try:
            for column in desc:
                name = column[1]
                if name == 'key':
                    continue
                value = cursor.execute('SELECT ' + name + ' FROM contacts WHERE id='+str(i)).fetchall()
                if not value:
                    value = 'void'
                else:
                    value = value[0][0]
                account[name] = value
            accounts.append(account)
        except Exception as exc:
            return jsonify({
            'error': exc
            })


def unspace(str):
    output = ""
    str_list = str.split()
    for word in str_list:
        output+=word
    return output


# Flask Decorators
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/',methods=['GET'])
def home():
    return redirect(url_for('contacts_home'))


@app.route('/api/contacts', methods=['GET', 'POST'])
def contacts_home():
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        no_space_name = unspace(name)

        #?Valid name check
        if not no_space_name.isalpha():
            return render_template('api_gen.html', key="Name must only contains letters!")
        #?Valid email check
        response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params = {'email': email})

        status = response.json()['status']
        if status == "invalid":
            return render_template('api_gen.html', key="Email was invalid!")

        # --------
        key = register_key(name, email)
        return render_template('api_gen.html', key=key)
    return render_template('api_gen.html', key="Fill out the form to register a key")

@app.route('/api/contacts/allAPIKEY=<key>', methods=['GET'])
def api_all(key):
    if not validatekey(key):
        return jsonify({
            'error': "API key is not valid"
        })
    return jsonify(accounts)

@app.route('/api/contacts/ID=<id>APIKEY=<key>', methods=['GET'])
def api_id(id, key):
    if not validatekey(key):
        return jsonify({
            'error': "API key is not valid"
        })
    try:
        for account in accounts:
            if int(account["id"]) == int(id): return jsonify(account)
        else:
            return jsonify({
                'error': 'Account not found'
            })
    except TypeError:
        return jsonify({
            'error': 'An error has occured'
        })
    except Exception as exc:
        exc = str(exc)
        return jsonify({
            'error': exc
        })
@app.route('/api/contacts/NAME=<name>APIKEY=<key>', methods=['GET'])
def api_name(name, key):
    return jsonify({
        'error': 'SERVICE UNAVAILABLE YET'
    })

if __name__ == '__main__':
    keys_conn = sqlite3.connect('api_keys.db')
    set_api_keys(keys_conn)
    setup(conn=conn)
    app.run(port=3034,debug=True, host="0.0.0.0")
    logging.critical("app has stopped running")