import os
import git
import uuid
from flask import current_app


def clone_repo_service(repo_url, destination=None):
    try:
        repo_name = os.path.basename(repo_url).replace('.git', '')

        # ✅ Lấy WORKSPACE_PATH từ config
        workspace_path = current_app.config['WORKSPACE_PATH']
        dest = destination or os.path.join(workspace_path, repo_name)

        os.makedirs(dest, exist_ok=True)
        repo = git.Repo.clone_from(repo_url, dest)

        return {
            "success": True,
            "data": {
                "repo_name": repo_name,
                "repo_path": dest,
                "current_branch": repo.active_branch.name
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_branches_service(repo_path):
    try:
        repo = git.Repo(repo_path)
        branches = [{"name": b.name, "is_current": b == repo.active_branch} for b in repo.heads]
        return {"success": True, "data": branches}
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_commits_service(repo_path, branch='main'):
    try:
        repo = git.Repo(repo_path)
        commits = []
        for commit in repo.iter_commits(branch):
            commits.append({
                "hash": commit.hexsha[:7],
                "message": commit.message.strip(),
                "author": commit.author.name,
                "email": commit.author.email,
                "date": commit.committed_datetime.isoformat(),
                "parents": [p.hexsha[:7] for p in commit.parents]
            })
        return {"success": True, "data": commits}
    except Exception as e:
        return {"success": False, "error": str(e)}


def open_repository_service(repo_path):
    try:
        if not os.path.exists(repo_path):
            return {"success": False, "error": "Repository path does not exist"}

        repo = git.Repo(repo_path)

        repo_name = os.path.basename(repo_path.rstrip('/\\'))
        repo_id = str(uuid.uuid4())

        if repo.is_dirty(untracked_files=True):
            status = 'dirty'
        elif repo.untracked_files:
            status = 'untracked'
        else:
            status = 'clean'

        current_branch = repo.active_branch.name
        local_branches = [head.name for head in repo.heads]

        remote_branches = []
        if repo.remotes:
            for remote in repo.remotes:
                for ref in remote.refs:
                    remote_branches.append(ref.name)

        # Danh sách file thay đổi
        changed_files = [item.a_path for item in repo.index.diff(None)]
        changed_files += repo.untracked_files

        # ✅ Map lại thành object, KHÔNG có "selected"
        changes = []
        for idx, file_path in enumerate(changed_files, start=1):
            full_path = os.path.normpath(file_path)
            name = os.path.basename(full_path)
            dir_path = os.path.dirname(full_path)
            ext = os.path.splitext(name)[1].replace('.', '').lower()

            changes.append({
                "id": idx,
                "name": name,
                "path": dir_path,
                "type": ext
            })

        return {
            "success": True,
            "data": {
                "id": repo_id,
                "name": repo_name,
                "path": repo_path,
                "status": status,
                "currentBranch": current_branch,
                "branches": {
                    "local": local_branches,
                    "remote": remote_branches
                },
                "changes": changes
            }
        }

    except Exception as e:
        return {"success": False, "error": str(e)}