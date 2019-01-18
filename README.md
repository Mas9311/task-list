# List of Tasks #

Consolidate your todo lists.<br>
Note: the **my_lists/** folder will be created to store all of your lists.

## Usage ##

 1. [Download this repo](https://github.com/Mas9311/task-list/archive/v1.0.zip), and open a Terminal window.
 1. <code>unzip</code> the <code>task-list-1.0.zip</code> file from your downloads.
 1. <code>cd</code> into the <code>task-list-1.0</code> folder
   - To run the menu-driven program, type <code>python3 run.py</code>
   - To *just* print all of your lists, type <code>python3 run.py print</code>

---

### Create an Executable ###

If you want to create a global executable, you will need root privilege.<br>
I called mine <code>ptasks</code>, short for *print tasks*.

#### Linux users ####

 1. <code>mv</code> the <code>task-list</code> folder to it's final destination
 1. <code>cd /usr/local/bin/</code>
 1. <code>sudo touch ptasks</code> and enter the password when prompted
 1. <code>sudo chmod +x ptasks</code>
 1. <code>sudo gedit ptasks</code> or whatever text editor you're comfortable with, such as {vim/vi, nano, gedit} and type:
     - <code>cd ~/path/to/task-list/;</code>
     - <code>python3 run.py print</code>
     - save the changes (in gedit, \[ctrl + s\])
