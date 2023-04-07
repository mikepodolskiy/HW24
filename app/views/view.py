# import required libraries and modules
from flask import request, Blueprint, jsonify, Response
from marshmallow import ValidationError
from typing import Union


from app.builder import build_query
from app.model.model import BatchRequestSchema

# creating blueprint
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Response, tuple[Response, int]]:
    # getting data from request
    if not request.json:
        raise Exception('Invalid request format')
    req_data: dict = request.json
    # checking data correctness using marshmallow
    try:
        BatchRequestSchema().load(req_data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in req_data['queries']:
        result = build_query(cmd=query['cmd'],
                             value=query['value'],
                             file_name=req_data['file_name'],
                             data=result)

    return jsonify(result)
