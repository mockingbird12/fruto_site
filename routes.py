from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return 'Hello world'

@app.route('/api_post', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
