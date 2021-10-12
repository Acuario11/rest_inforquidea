from flask import Flask
#from flask_pymongo import pymongo
from flask_mongoengine import MongoEngine
import datetime

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db":"bdazqhkgwcvflne"
}
app.config["USER_ENABLE_EMAIL"]=False
app.config["SECRET_KEY"]="super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=60)
#app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=7)
app.config["JWT_AUTH_URL_RULE"]="/api/auth"
app.debug=True


#app.config['MONGO_URI']="mongodb://localhost:27017/dataapp"
db = MongoEngine(app)
#db=PyMongo(app)

from flask_user import UserManager
from app.user.models import User, UserBase
user_manager=UserManager(app,db,User)


from flask_pymongo import PyMongo
appx = Flask(__name__)
#appx.config["MONGO_URI"] = "mongodb://localhost:27017/dataapp"

#appx.config["MONGO_URI"] = "mongodb://usuario:password@host:port/database"
appx.config["MONGO_URI"] = "mongodb://u2gr1kpnfvanjepbebqi:F4NhusuXLrj2sEI4NdAB@bdazqhkgwcvflne-mongodb.services.clever-cloud.com:27017/bdazqhkgwcvflne"
mongo = PyMongo(appx)
    

#JWT
from flask_jwt import JWT
from app.user.jwt import authenticate, identity
jwt=JWT(app,authenticate, identity)

#controlador de User
from app.user.controllers import userBp
app.register_blueprint(userBp)
from flask_restful import Api

# Restfull api
from app.rest import controller
api=Api(app)

