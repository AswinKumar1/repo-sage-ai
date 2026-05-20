from git import Repo
import tempfile
import shutil
import os


def clone_repository(repo_url, branch):

    temp_dir = tempfile.mkdtemp()

    try:

        Repo.clone_from(
            repo_url,
            temp_dir,
            branch=branch
        )

        return temp_dir

    except Exception as e:

        shutil.rmtree(temp_dir, ignore_errors=True)

        raise Exception(f"Repository clone failed: {str(e)}")


def validate_local_repository(local_path):

    if not os.path.exists(local_path):
        raise Exception("Provided path does not exist")

    if not os.path.isdir(local_path):
        raise Exception("Provided path is not a directory")

    return local_path