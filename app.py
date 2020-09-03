from flask import Flask
from app import app
from app import db
from app.models import User



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


app = Flask(__name__)

if __name__ == '__main__':
    app.run()
