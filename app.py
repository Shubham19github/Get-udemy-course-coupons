# required packages
from flask import Flask
from flask_restful import Api
from resources.coupons import Coupons

# defining port no.
PORT = 5500

app = Flask(__name__)

api = Api(app)

# adding coupons resources
api.add_resource(Coupons, '/coupons/<string:keyword>')

if __name__ == '__main__':
	app.run(port = PORT, debug=True)