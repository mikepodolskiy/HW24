# import required libraries and modules
from flask import request, Blueprint, jsonify
from marshmallow import ValidationError

from app.funcs.functions import filter_data, map_data, read_file, sort_data, limit_data, unique_data
from app.builder import build_query
from app.model.model import RequestSchema, BatchRequestSchema

# creating blueprint
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    # getting data from request
    req_data = request.json
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


    # below skypro solution for bad api

    # first_result = build_query(cmd=req_data['cmd1'],
    #                            value=req_data['value1'],
    #                            file_name=req_data['file_name'],
    #                            data=None)
    #
    # result = build_query(cmd=req_data['cmd2'],
    #                      value=req_data['value2'],
    #                      file_name=req_data['file_name'],
    #                      data=first_result)

    # below my code, which i sent to check

    # check received data, applying relative function, forming data
    # if req_data['cmd1'] == 'filter':
    #     output_data = filter_data(data, req_data['value1'])
    #
    # elif req_data['cmd1'] == 'map':
    #     output_data = map_data(data, req_data['value1'])
    #
    # elif req_data['cmd1'] == 'sort':
    #     output_data = sort_data(data, req_data['value1'])
    #
    # elif req_data['cmd1'] == 'limit':
    #     output_data = limit_data(data, req_data['value1'])
    #
    # elif req_data['cmd1'] == 'unique':
    #     output_data = unique_data(data)
    #
    # # check second pair of received data, applying relative function to the previously formed data
    # if req_data['cmd2'] == 'filter':
    #     output_data = filter_data(output_data, req_data['value2'])
    #
    # elif req_data['cmd2'] == 'map':
    #     output_data = map_data(output_data, req_data['value2'])
    #
    # elif req_data['cmd2'] == 'sort':
    #     output_data = sort_data(output_data, req_data['value2'])
    #
    # elif req_data['cmd2'] == 'limit':
    #     output_data = limit_data(output_data, req_data['value2'])
    #
    # elif req_data['cmd2'] == 'unique':
    #     output_data = unique_data(output_data)

    # return result of function applying
    # return jsonify(list(result)), 200
