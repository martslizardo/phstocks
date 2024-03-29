from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__,instance_relative_config=True)


redis_store = FlaskRedis(app)

from . import stocksRequest

stocksRequest.insert_stocks()
stocksRequest.retrieve_stocks()
from . import router
