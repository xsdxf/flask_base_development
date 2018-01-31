from flask import Blueprint
blue=Blueprint('blue',__name__)
@blue.route('/')
def index():
    return "<h1>hello</h1>"