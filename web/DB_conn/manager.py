from application import app, db
from www import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # from common.models.user import  User
    # db.create_all()
