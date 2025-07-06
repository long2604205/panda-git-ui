from flask import request, jsonify
from app.services.git_service import clone_repo_service, get_branches_service, get_commits_service, open_repository_service
from app.utils.response_builder import build_response


def clone_repo():
    data = request.get_json()
    result = clone_repo_service(data['repo_url'], data.get('destination'))
    return jsonify(build_response(result))

def get_branches():
    data = request.get_json()
    result = get_branches_service(data['repo_path'])
    return jsonify(build_response(result))

def get_commits():
    data = request.get_json()
    result = get_commits_service(data['repo_path'], data.get('branch', 'main'))
    return jsonify(build_response(result))

def open_repository():
    data = request.get_json()
    result = open_repository_service(data['repo_path'])
    return jsonify(build_response(result))