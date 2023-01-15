import subprocess

def check_git_status():
    directory = input("Please enter the local git directory path: ")
    git_check = subprocess.run(['git','rev-parse','--is-inside-work-tree'], cwd = directory, capture_output=True)

    if git_check.returncode != 0:
        while git_check.returncode != 0:
            print("You have entered a Invalid git repository directory! Please try again.")
            directory = input("Please enter the local git directory path: ")
            git_check = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'],  cwd = directory, capture_output=True)

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


if __name__ == '__main__':
    check_git_status()

