
from flask import Flask, make_response, jsonify, request, Blueprint
app = Flask(__name__)

api = Blueprint('api', __name__, url_prefix='/api/v1')

politicalparties_list = []

@api.route('/politicalparties', methods = ["POST"])
def add_politicalparties():
    """
        Create a new political party  - POST request
    """
    data = request.get_json()
    name = data ['name']
    abbreviation = data ['abbreviation']
    members = data ['members']
    headquarters = data ['headquarters']
    chairperson = data ['chairperson']

    new_politicalparty = { 
            "name" : name ,
            "abbreviation" : abbreviation ,
            "members" : members ,
            "headquarters": headquarters,
            "chairperson": chairperson
            }
    
    politicalparties_list.append(new_politicalparty)
    return make_response(jsonify({
        "Message": "New Political Party Created",
        "party name": new_politicalparty['name']
    }), 201)
