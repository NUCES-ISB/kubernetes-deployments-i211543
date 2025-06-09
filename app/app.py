from flask import Flask, jsonify
import os
import psycopg2
from psycopg2 import pool

app = Flask(__name__)

# Database connection pool
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 10,
    host=os.getenv('POSTGRES_HOST', 'postgres-service'),
    database=os.getenv('POSTGRES_DB', 'postgres'),
    user=os.getenv('POSTGRES_USER', 'postgres'),
    password=os.getenv('POSTGRES_PASSWORD', 'postgres')
)

@app.route('/')
def hello():
    return jsonify({"message": "Welcome to Flask PostgreSQL App!"})

@app.route('/health')
def health():
    try:
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        db_pool.putconn(conn)
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 