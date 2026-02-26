import requests
import json

def create_repo(token, repo_name):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "auto_init": False,
        "private": False,
        "description": "TechStack Global - B2B Automation Insights"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print(f"✅ Successfully created repository: {repo_name}")
    elif response.status_code == 422:
        print(f"ℹ️ Repository {repo_name} already exists or name is taken.")
    else:
        print(f"❌ Failed to create repository. Status: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    import os
    TOKEN = os.getenv("GITHUB_TOKEN", "YOUR_TOKEN_HERE")
    create_repo(TOKEN, "techstackglobal.github.io")
