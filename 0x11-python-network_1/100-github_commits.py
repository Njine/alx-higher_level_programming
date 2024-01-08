#!/usr/bin/python3
"""
Script that lists the 10 most recent commits (from the most recent to oldest)
of the specified repository by the given owner. Prints each commit as
`<sha>: <author name>` using only the packages requests and sys.

Usage: ./100-github_commits.py <repository name> <owner name>
  - The first argument is the repository name.
  - The second argument is the owner name.
"""

import sys
import requests

if __name__ == "__main__":
    repo_name, owner_name = sys.argv[1], sys.argv[2]
    commits_url = (
        f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    )

    try:
        response = requests.get(commits_url)
        commits_data = response.json()

        for commit in commits_data[:10]:
            sha = commit.get('sha')
            author_name = (
                commit.get('commit', {}).get('author', {}).get('name')
            )
            print(f"{sha}: {author_name}")
    except ValueError as invalid_json:
        pass
