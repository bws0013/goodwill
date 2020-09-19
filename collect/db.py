import mysql.connector

from input import read_global_config

def get_configs():
    local_config = read_global_config("db")


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
