import subprocess, os, sys, socket, tkinter as tk
from tkinter import filedialog

def check_internet_connection():
    try:
        socket.getaddrinfo("8.8.8.8", 80)
        return True
    except socket.error:
        return False

def run_git_command(command, directory):
    git_output = subprocess.run(command, cwd = directory, capture_output= True)
    return git_output.stdout.decode().strip()

def check_git_status():
    root = tk.Tk()
    root.withdraw()

    #Get the Directory
    directory = filedialog.askdirectory(initialdir = '/', title = "Select Git Repository Folder")
    if not directory:
        sys.exit()

    #Check if the entered Directory is a valid directry path and a valid Git Directory
    while not os.path.isdir(directory) or not os.path.exists(os.path.join(directory, ".git")):
        print("Invalid git repository directory. Please try again.")
        directory = filedialog.askdirectory(initialdir='/', title="Select Git Repository Folder")
        if not directory:
            sys.exit()

    # Get the Status of the local repository
    git_status = run_git_command(['git','status','--porcelain'], directory)

    # Get the Active Branch
    git_branch = run_git_command(['git','rev-parse','--abbrev-ref','HEAD'], directory)

    #Get the recent commit logs
    git_log = run_git_command(['git','log','-1','--pretty=format:"%an"','--since="1 week ago"'], directory)

    #Print the Active Branch
    print(f"Active branch: {git_branch}")

    #Print if there are any local changes
    file_status = False
    if git_status:
        file_status = True
    print(f"Local Changes: {file_status}")

    # check if the latest HEAD commit was done by Rufus
    isRufus = False
    if git_log == "Rufus":
        isRufus = True
    print(f"Blame Rufus: {isRufus}")

    #check if the latest HEAD commit was done in the last week
    isRecent = False
    if git_log:
        isRecent = True
    print(f"Recent Commit: {isRecent}")

    if check_internet_connection():
        #Check if the local and remote repositories have any differences
        git_remote = run_git_command(['git','diff'], directory)

        if git_remote:
            print("There are differences between the local and remote repositoy")
        else:
            print("The local and remote repository are in sync")

        # Check remote repository status
        git_remote_status = run_git_command(['git','remote','-v'],directory)
        print(f"Remote repository status:")
        print(git_remote_status)
    else:
        print("No Internet Connection skipping he remote repository check!")

    # get summary of last five commits
    git_commits = run_git_command(['git','log', '-n', '5', '--pretty=format: "%h %s"'], directory)
    if not git_commits:
        git_commits = "No commits found"
    print(f"Last 5 commits:")
    print(git_commits)


if __name__ == '__main__':
    check_git_status()

