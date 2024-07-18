import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'qwerty',
    'db': 'perpustakaan',
}

# Create a connection to the database``
conn = MySQLdb.connect(**db_config)
