from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome():
    return "Welcome to the Flask + Redis App!"

@app.route('/count')
def count():
    count = r.incr('visit_count')
    return f'Visit count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
