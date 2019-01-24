# List of Tasks #

[![image](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

Consolidate your todo lists.<br>

## Usage ##

 1. [Download this repo](https://github.com/Mas9311/task-list/archive/v1.0.1.zip), and open a Terminal window.
 1. Extract or <code>unzip</code> the <code>task-list-1.0.1.zip</code> file, then delete the zip.
    - I recommend creating a general Software folder, <code>mkdir \~/Software/</code>, so your applications/software don't accumulate in **\~/Downloads/** or **\~/Desktop/**.
    - Move the new <code>task-list-1.0.1/</code> folder into the **\~/Software/** folder.
 3. <code>cd</code> into <code>task-list-1.0.1/</code>.
 1. To run the menu-driven program, type <code>python3 run.py</code>
 1. Or to *just* print all of your lists, type <code>python3 run.py print</code>


## Want to Make an Executable? ##

Personally, I don't want to <code>cd</code> into <code>\~/Software/task-list-1.0.1/</code>, and type <code>python3 run.py</code> to run the menu program every time, so follow these steps to either create an executable or an alias.<br>
I named mine <code>tasks</code> and <code>ptasks</code>, short for *print tasks*.<br>
I know it looks like a lot to read, but it's a step-by-step walkthrough, so bear with me.<br>

*Note: only one version of this program can be in* **\~/Software/** *at a time.*<br>
*If you've downloaded two versions of this program, move the preexisting* **my_lists/** *folder to the newer version, then delete the older version entirely.*

#### Linux users ####

First, you have to decide if you want to
[create a desktop launcher](https://github.com/Mas9311/task-list#create-a-desktop-launcher) 
or just 
[create an alias](https://github.com/Mas9311/task-list/blob/master/README.md#create-an-alias).<br>
Both will allow you type the given name into Terminal to run the commands we're about to create.<br>

*Note: If you did not move the* **task-list-1.0.1/** *folder into* **\~/Software/** *, then replace the* '\~/Software/' *path with the actual path in the text found below.*

##### Create a Desktop Launcher #####

This guide you in making an executable then a desktop launcher for <code>tasks</code>.<br>
 1. <code>sudo -s</code> and type your password to elevate privileges to root until you type<code>exit</code> or close the Terminal window.
 1. Copy and paste the following into Terminal:
    - Create <code>tasks</code>
<pre>echo $"\n# tasks can be executed from anywhere, including a desktop launcher!\n" >> /usr/bin/tasks
echo "cd ~/Software/task-list*/;" >> /usr/bin/tasks
echo "python3 run.py" >> /usr/bin/tasks
chmod +x tasks
</pre>
    - Create <code>ptasks</code>
<pre>echo $"\n# ptasks can be executed from anywhere, including a desktop launcher!\n" >> /usr/bin/ptasks
echo "cd ~/Software/task-list*/;" >> /usr/bin/ptasks
echo "python3 run.py print" >> /usr/bin/ptasks
chmod +x ptasks
</pre>

Voilà, your <code>tasks</code> and <code>ptasks</code> executables are now complete, so let's go make that desktop launcher.

 3. Right click any spot on the Desktop.
 1. Select \[Create Launcher...] and do the following:
    - Name: Task-List
    - Command: tasks
    - \[✓] Run in Terminal
 5. Click \[Create].
 1. Open the new launcher and click \[Mark Executable] when prompted.
 1. Repeat step 3-6 for <code>ptasks</code>, but change the Name: Print Tasks and Command: ptasks
 
You do not need to continue to the next section, as the executables in **/usr/local/bin/** have elevated privileges.
If you end up hating this program, you can remove the executables with <code>sudo rm /usr/local/bin/tasks /usr/local/bin/ptasks</code>.

---

##### Create an Alias #####

Instead of doing the 7 steps listed above, these will achieve the same goal.<br>
BUT you cannot properly run a desktop launcher via an alias.

1. Copy and paste the following block into Terminal:
<pre>echo $'\n# task-list program aliases' >> ~/.bash_aliases
echo 'alias tasks="cd ~/Software/task-list*/; python3 run.py"' >> ~/.bash_aliases
echo 'alias ptasks="cd ~/Software/task-list*/; python3 run.py print"'  >> ~/.bash_aliases
source ~/.bash_aliases
</pre>
 
Your aliases, <code>tasks</code> and <code>ptasks</code>, are now able to be called, in Terminal, from any folder!

If you end up hating this program, you will have to manually remove the aliases with:

 1. <code>nano ~/.bash_aliases</code>.
 1. Delete the task-list entires found at the bottom.
 1. Press \[Ctrl X] to exit.
 1. Press \[Y] to save your changes.
 1. Press \[Enter] to save the name of the file *as is*.
 1. <code>source ~/.bash_aliases</code>
