import subprocess, os

def check_git_status():
    directory = input("Please enter the local git directory path: ")

    while not os.path.isdir(directory) or not os.path.exists(os.path.join(directory, ".git")):
        print("Invalid git repository directory. Please try again.")
        directory = input("Please enter the local git directory path: ")

    git_status = subprocess.run(['git','status','--porcelain'], cwd=directory, capture_output=True)
    git_branch = subprocess.run(['git','rev-parse','--abbrev-ref','HEAD'], cwd=directory,capture_output=True)
    git_log = subprocess.run(['git','log','-1','--pretty=format:"%an"','--since="1 week ago"'], cwd=directory, capture_output=True)

    print(f"Active branch: {git_branch.stdout.decode().strip()}")

    file_status = False
    if git_status.stdout:
        file_status = True
    print(f"local changes: {file_status}")

    git_log_output = git_log.stdout.decode()

    isRufus = False
    if git_log_output.strip() == "Rufus":
        isRufus = True
    print(f"blame Rufus: {isRufus}")

    isRecent = False
    if git_log_output:
        isRecent = True
    print(f"Recent Commit: {isRecent}")

    #git_fetch = subprocess.run(['git','fetch'],cwd = directory,capture_output=True)
    git_diff = subprocess.run(['git','diff'], cwd=directory, capture_output=True)
    remote_diff = git_diff.stdout.decode()

    if remote_diff:
        print("There are differences between the local and remote repositoy")
    else:
        print("The local and remote repository are in sync")

    git_remote_status = subprocess.run(['git','remote','-v'],cwd=directory, capture_output=True)
    remote_status = git_remote_status.stdout.decode()
    print(f"Remote repository status:")
    print(remote_status)

    git_week_commits = subprocess.run(['git','log','--pretty=format: "%h %s"', '--since="1 week ago"'], cwd=directory, capture_output=True)
    week_commits = git_week_commits.stdout.decode()
    if not week_commits:
        week_commits = "0"
    print(f"Commits made in the last week:")
    print(week_commits)


if __name__ == '__main__':
    check_git_status()

