import getpass
import snowflake.connector

password = getpass.getpass("Snowflake password: ")
passcode = input("Google Authenticator code: ")

conn = snowflake.connector.connect(
    account="CUFVCDW-XY43396",
    user="ABIOLA",
    password="9f7XDeFvtPmN6hh",
    authenticator="username_password_mfa",
    passcode="462011",
    role="DBT_ROLE",
    warehouse="ZOMATO_WH",
    database="ZOMATO",
    schema="STAGING"
)

cursor = conn.cursor()

print("\nConnection successful:")
print(cursor.execute("""
    SELECT
        CURRENT_USER(),
        CURRENT_ROLE(),
        CURRENT_DATABASE(),
        CURRENT_SCHEMA()
""").fetchone())

cursor.close()
conn.close()