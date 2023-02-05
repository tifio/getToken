import csv
import module.func as func
from module.bd import create_connection


def main():
    with open('test.csv') as f:
        reader = csv.DictReader(f)
        cursor = create_connection().cursor()
        for row in reader:
            email_csv = row['email']  # get email
            print(email_csv)
            func.RequestTokenPassword(email_csv)  # request token
            token_password = func.Token(email_csv, cursor)  # get token from DB
            func.CheckTokenValid(token_password)  # check token
            func.WriteTokenToCSV(row, token_password)  # write to csv
            print("_" * 42)

if __name__ == '__main__':
    main()