from flask import Flask, request
elham = Flask(__name__)
@elham.route('/')
  def index():
    return 'hello world'
if (__name__ == '__main__'):
    elham.run()

