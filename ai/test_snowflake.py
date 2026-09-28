import os
from dotenv import load_dotenv
import snowflake.connector
from cryptography.hazmat.primitives import serialization

load_dotenv()

private_key_path = os.getenv("SNOWFLAKE_PRIVATE_KEY_FILE")
passphrase = os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE")

with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=passphrase.encode(),
    )

private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    private_key=private_key_bytes,
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE"),
)

print("Connection object created")
print("Connection closed:", conn.is_closed())

cursor = conn.cursor()
cursor.execute("SELECT CURRENT_USER(), CURRENT_DATABASE(), CURRENT_SCHEMA()")

print(cursor.fetchone())

cursor.close()
conn.close()