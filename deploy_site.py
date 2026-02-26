import os
import subprocess

def run_git_commands(token):
    repo_url = f"https://techstackglobal:{token}@github.com/techstackglobal/techstackglobal.github.io.git"
    blog_path = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog"
    
    os.chdir(blog_path)
    
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "config", "user.email", "techstackglobal.mgmt@gmail.com"],
        ["git", "config", "user.name", "TechStack Global"],
        ["git", "commit", "-m", "Initial B2B Blog Launch by Antigravity Autopilot"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "add", "origin", repo_url],
        ["git", "push", "-u", "origin", "main", "--force"]
    ]
    
    for cmd in commands:
        try:
            print(f"Running: {' '.join(cmd[:3])}...")
            # Use shell=True for Windows compatibility with certain git versions if needed, 
            # but list of args is generally safer.
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error: {result.stderr}")
            else:
                print(f"Success: {result.stdout.strip()}")
        except Exception as e:
            print(f"Failed to run command: {e}")

if __name__ == "__main__":
    TOKEN = os.getenv("GITHUB_TOKEN", "YOUR_TOKEN_HERE")
    run_git_commands(TOKEN)
