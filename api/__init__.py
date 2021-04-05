# Third party
from flask import request

# Local
from config import app, db
from api.models import FirstName


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/name/id', methods=['GET'])
def retrieve_name():
    id = request.args.get('id')
    if id:
        return FirstName.query.get(id).to_dict()
    else:
        return {
                'data': [
                    name.to_dict()
                    for name in FirstName.query.all()
            ]
        }


@app.route('/name', methods=['POST'])
def create_name():
    details = request.json
    new_name = FirstName(
        name=details['name'],
        is_active=details['is_active']
    )
    db.session.add(new_name)
    db.session.commit()
    return new_name.to_dict()
