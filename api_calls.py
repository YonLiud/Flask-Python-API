import logging
import sqlite3
import secrets

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', filename="api.log", filemode="a", level=logging.DEBUG)
api_keys = []
class api_key():
    def __init__(self, key, name, email):
        self.__key = key
        self.name = name
        self.email = email
    def get_key(self):
        return self.__key
    def get_owner(self):
        return [self.name, self.email]

def set_api_keys(keys_conn):
    api_keys.clear()
    cursor = keys_conn.cursor()
    keys = cursor.execute('SELECT * FROM keys').fetchall()
    for key in keys:
        logging.info("Instance created with "+ key[0] +" " +key[1]+" "+ key[2])
        api_keys.append(api_key(key[0], key[1], key[2]))

def validatekey(key):
    logging.info("Comparing key: " + key)
    if not api_key:
        return False
    for api in api_keys:
        if key == api.get_key():
            logging.warning("Comparing key has successfully finished")
            return True
    else:
        logging.warning("Comparing key has failed")
        return False
def register_key(name, email):
    keys_conn = sqlite3.connect('api_keys.db')
    cursor = keys_conn.cursor()
    generated_key = secrets.token_urlsafe(16)
    try:
        cursor.execute("INSERT INTO keys VALUES(?, ?, ?);", (generated_key, name, email))
        keys_conn.commit()
        logging.info("Registered key: "+generated_key + " to " + name + " / " + email)
        return generated_key
    except Exception as exc:
        print(exc)
        if str(exc).split()[0].lower() == "unique":
            return "Name or Email are already in use"
        return exc
