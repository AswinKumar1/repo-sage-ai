from git import Repo
import tempfile
import shutil


def get_remote_branches(repo_url):
    temp_dir = tempfile.mkdtemp()

    try:
        repo = Repo.clone_from(
            repo_url,
            temp_dir,
            no_checkout=True
        )

        branches = []

        for ref in repo.remote().refs:
            branch_name = ref.name.replace("origin/", "")

            if branch_name != "HEAD":
                branches.append(branch_name)

        return sorted(branches)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
