from flask import Flask
from flasgger import Swagger
import routes
app = Flask(__name__)
swagger = Swagger(app)




if __name__ == '__main__':
    app.run()
