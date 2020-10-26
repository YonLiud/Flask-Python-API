import secrets
import sqlite3
from flask import Flask,redirect,url_for,render_template,request, jsonify
app=Flask(__name__)
conn = sqlite3.connect('database.db')
accounts = []
api_keys = []

def setup(conn):
    cursor = conn.cursor()
    desc =  cursor.execute("pragma table_info('contacts')").fetchall()
    for i in range(1, cursor.execute('SELECT COUNT(*) from contacts').fetchall()[0][0]+1):
        account = {}
        name = ""
        value = []
        try:
            for column in desc:
                name = column[1]
                value = cursor.execute('SELECT ' + name + ' FROM contacts WHERE contact_id='+str(i)).fetchall()
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

def get_api_keys(keys_conn):
    cursor = keys_conn.cursor()
    return cursor.execute('SELECT key FROM keys').fetchall()

def validatekey(key):
    keys_conn = sqlite3.connect('api_keys.db')
    valid_keys = get_api_keys(keys_conn)
    if not valid_keys:
        return 0
    for validate in valid_keys:
        if key == validate[0]:
            return 1
    else:
        return 0


def register_key():
    cursor = keys_conn.cursor()


# Flask Decorators
@app.route('/',methods=['GET'])
def home():
    return redirect(url_for('contacts_home'))


@app.route('/api/contacts', methods=['GET', 'POST'])
def contacts_home():
    key = "hello"
    if request.method=='POST':
        return render_template('api_gen.html', key=key)
    return render_template('api_gen.html', key="Fill out the form to register a key")


@app.route('/api/contacts/all', methods=['GET'])
def api_all():
    return jsonify(accounts)

@app.route('/api/contacts/<id>-<key>', methods=['GET'])
def api_id(id, key):
    if not validatekey(key):
        return jsonify({
            'error': "API key is not valid"
        })
    try:
        for account in accounts:
            if int(account["contact_id"]) == int(id): return jsonify(account)
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


if __name__ == '__main__':

    setup(conn=conn)
    app.run(port=5000,debug=True)