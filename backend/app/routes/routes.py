from flask import Blueprint
from app.controllers.git_controller import clone_repo, get_branches, get_commits

from app.controllers.git_controller import open_repository

git_bp = Blueprint('git_v1', __name__, url_prefix='/api/v1/git')

git_bp.route('/clone', methods=['POST'])(clone_repo)
git_bp.route('/branches', methods=['POST'])(get_branches)
git_bp.route('/commits', methods=['POST'])(get_commits)
git_bp.route('/open-repository', methods=['POST'])(open_repository)