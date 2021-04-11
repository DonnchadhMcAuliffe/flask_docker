# Local
from api import app
from config import db

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
