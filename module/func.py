import requests
from psycopg2._psycopg import OperationalError
import pandas as pd
import hashlib
import config as conf


def RequestTokenPassword(email):
    response = requests.post(conf.ENDPOINT, json={'email': email})
    print(response.text, "request token")

def CheckTokenValid(token):
    response = requests.get(conf.ENDPOINT, data={'token': token})
    print(response.text, "check token")

def WriteTokenToCSV(data: dict, token: str):
    data = data
    token_v = {'token': token}
    data.update(token_v)
    columns = ['email', 'password', 'token']
    data_to_csv = [data]
    df = pd.DataFrame(data_to_csv, columns=columns)
    df.to_csv(r'./tmp.csv', mode='a', header=False, index=False)

def Token(email, cursor):
    try:
        cursor.execute(
            f"SELECT * FROM {conf.name_table_email} "
            f"WHERE email = LOWER('{email}');"
        )
        request_id_user = cursor.fetchone()
        cursor.execute(
            f"SELECT * FROM {conf.name_table_token} "
            f"WHERE user_id = {request_id_user[0]}"
            f"ORDER BY created_at DESC;"
        )
        request_token_db = cursor.fetchone()
        email = email.lower()
        hash_mail = hashlib.md5(email.encode()).hexdigest()
        finish_token = f"{request_token_db[3]}.{hash_mail}"
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return finish_token
