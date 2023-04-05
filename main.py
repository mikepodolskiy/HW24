from flask import Flask
from app.views.view import main_blueprint

# starting app
app = Flask(__name__)

# registering blueprints
app.register_blueprint(main_blueprint)

# run app with import check
if __name__ == '__main__':
    app.run(debug=True)
