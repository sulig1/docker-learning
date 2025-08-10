from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome():
    return """
    <html>
        <head>
            <title>Flask + Redis App</title>
            <style>
                body {
                    background-color: #f4f6f8;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                    color: #333;
                }
                h1 {
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px 40px;
                    border-radius: 8px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Flask + Redis App!</h1>
        </body>
    </html>
    """

@app.route('/count')
def count():
    count = r.incr('visit_count')
    return f"""
    <html>
        <head>
            <title>Visit Count</title>
            <style>
                body {{
                    background-color: #eef2f3;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                    color: #333;
                }}
                h2 {{
                    background-color: #2196F3;
                    color: white;
                    padding: 20px 40px;
                    border-radius: 8px;
                }}
            </style>
        </head>
        <body>
            <h2>Visit count: {count}</h2>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
