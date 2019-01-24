# List of Tasks #

[![image](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

Consolidate your todo lists.<br>

## Usage ##

 1. [Download this repo](https://github.com/Mas9311/task-list/archive/v1.0.1.zip), and open a Terminal window.
 1. Extract or <code>unzip</code> the <code>task-list-1.0.1.zip</code> file, then delete the zip.
    - I recommend creating a <code>\~/Software/</code> folder so your applications/software don't accumulate in <code>\~/Downloads</code> or <code>\~/Desktop</code>.
    - Move the <code>task-list-1.0.1/</code> folder into <code>\~/Software/</code>.
 3. <code>cd</code> into the <code>task-list-1.0.1/</code> folder.
 1. To run the menu-driven program, type <code>python3 run.py</code>
 1. Or to *just* print all of your lists, type <code>python3 run.py print</code>


## Want to Make an Executable? ##

Personally, I don't want to <code>cd</code> into the <code>\~/Software/task-list-1.0.1</code> folder and type <code>python3 run.py</code> every time to run the menu program, so follow these steps to either create executables or commands.<br>
I named mine <code>tasks</code> and <code>ptasks</code>, short for *print tasks*.<br>

*Note: only one version of this program can be in* <code>\~/Software/</code> *at a time.*<br>
*If you've downloaded two versions of this program, move the preexisting* <code>my_lists/</code> *folder to the newer version, then delete the older version entirely.*

#### Linux users ####

First, you have to decide if you want to<br>
A: make a Desktop launcher<br>
or<br>
B: make an alias to be able to type into Terminal<br>

##### A: Create a Desktop Launcher #####

Follow the following steps to create a launcher for <code>tasks</code>.<br>
*Note: You can follow this same recipe for <code>ptasks</code> as well*.

 1. <code>cd /usr/local/bin</code>.
 1. <code>sudo touch tasks</code> followed by your password.
 1. <code>sudo nano tasks</code>
 1. Copy and paste the following into your new file:
<pre># This script will be able to be executed from anywhere, including a desktop launcher
cd ~/Software/task-list*/;
python3 run.py</pre>
 5. <code>sudo chmod +x tasks</code>

Voilà, your executable is complete, now let's make that desktop launcher.

 1. Right click an open spot on the Desktop.
 1. Select \[Create Launcher...].
<pre>Name: Task-List
Command: tasks
[✓] Run in Terminal</pre>
 2. Click \[Create].
 1. Open the new launcher and click \[Mark Executable] when prompted.

You do not need to continue to the next section, as the executables in /usr/local/bin have an evelated privldge.

##### B: Create an Alias #####

If you did not move the <code>task-list-1.0.1/</code> folder into <code>\~/Software/</code>, then replace the <code>\~/Software/</code> path with the actual path in the block of text found below.

 1. <code>nano \~/.profile</code> to see and edit your current aliases.
 1. Copy the following block:
<pre># task-list program aliases
alias tasks="cd ~/Software/task-list*/; python3 run.py"
alias ptasks="cd ~/Software/task-list*/; python3 run.py print"</pre>
 3. Paste the text into the file. I recommend grouping your custom aliases together at the bottom of the file.
 1. Save your changes. If you're using the <code>nano</code> editor, press \[Ctrl X] to exit, \[Y] to save, then \[Enter] to save the name of the file as is.
 1. <code>source \~/.profile</code> to make your new aliases visible.
 1. Now you can type, in Terminal, the name of your new aliases from any folder to execute the corresponding commands.

