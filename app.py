from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "root"),
            database=os.getenv("MYSQL_DB", "flaskdb")
        )
        cursor = conn.cursor()

        if request.method == 'POST':
            msg = request.form['message']
            cursor.execute("INSERT INTO messages (message) VALUES (%s)", (msg,))
            conn.commit()

        cursor.execute("SELECT message FROM messages")
        messages = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('index.html', messages=messages)

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

