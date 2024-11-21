import pg8000

import os
from dotenv import load_dotenv

load_dotenv()


connection = pg8000.connect(database =os.getenv('PGDATABASE'),
                              user = os.getenv('PGUSER'),
                              password = os.getenv('PGPASSWORD'),
                              host=os.getenv('PGHOST'),
                              port='5432')

cursor = connection.cursor()

query = 'SELECT * FROM test'
cursor.execute(query)
connection.commit()
results = cursor.fetchall()

print(results)