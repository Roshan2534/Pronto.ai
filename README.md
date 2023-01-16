<h1>Pronto.ai</h1>


This script is designed to check the status of a local git repository and compare it with the remote repository. It displays the active branch,, local changes, recent commits, last 5 commits, and any differences between the local and remote repository.

<h3> Requirements: </h3>
No special requirements other than python and git, all the libraries used are built-in python libraries, so all that is needed is Python 3.x and git for its commands. But incase any of the libraries are not installed the list of libraries is: tkinter, os, subprocess, sys, socket.
You can install these libraries using pip3 install library_name command in your terminal

<h3>How to use: </h3>
1. Download the script and navigate to it using the terminal and run the command "python3 main.py"<br>
2. Select the git directory you want information on from the dialogue box that appears and you are done!<br>
3. The Script will then display the following information:<br> 
    -Active branch<br> 
    -Local changes<br> 
    -Recent Commits<br> 
    -Last 5 commits<br> 
    -If there are any differences in local and remote repository 

<h3> Notes: </h3>
1. If the script does not detect a valid git repository, it will ask you to select a different folder. <br>
2. If there is no internet connection, the script will not check the remote repository and will display. Message “No Internet connection, skipping the remote repository check!”.<br>

<h3> Screenshots: </h3>

Directory Selection:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/46147522/212614939-2fb8ca87-dcd0-4169-8fb4-97d3ab81a1fd.png">


Final Output: 

<img height = "200" width="600" alt="image" src="https://user-images.githubusercontent.com/46147522/212615200-056af016-8176-4ec5-87e5-d58b9b60da79.png">





