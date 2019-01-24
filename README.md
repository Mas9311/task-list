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
I know it looks like a lot to read, but it's a step-by-step walkthrough.

*Note: only one version of this program can be in* <code>\~/Software/</code> *at a time.*<br>
*If you've downloaded two versions of this program, move the preexisting* <code>my_lists/</code> *folder to the newer version, then delete the older version entirely.*

#### Linux users ####

First, you have to decide if you want to
[create a desktop launcher](https://github.com/Mas9311/task-list#create-a-desktop-launcher) 
or you can choose to 
[just create an alias](https://github.com/Mas9311/task-list/blob/master/README.md#create-an-alias).<br>
Both tutorials will allow you type the given name into Terminal to run the program.

##### Create a Desktop Launcher #####

Follow the following steps to create a launcher for <code>tasks</code>.<br>
*Note: You can follow this same recipe for* <code>ptasks</code> *as well by appending* <code> print</code> *after the <code>run.py</code>*.

 1. <code>cd /usr/local/bin</code>.
 1. <code>sudo touch tasks</code> to create the file. Enter your password when prompted.
 1. <code>sudo nano tasks</code> to edit the file.
 1. Copy and paste the following into your new file:
<pre># This executable file can be executed from anywhere, including a desktop launcher!
cd ~/Software/task-list*/;
python3 run.py </pre>
 5. <code>sudo chmod +x tasks</code> to elevate its privileges.

Voilà, your executable is complete, now let's make that desktop launcher.
*Note: You can create* <code>ptasks</code> *as well by changing the* Name *to* Print Tasks *and* Command *to* ptasks.

 1. Right click an open spot on the Desktop.
 1. Select \[Create Launcher...].
<pre>Name: Task-List
Command: tasks
[✓] Run in Terminal</pre>
 3. Click \[Create].
 1. Open the new launcher and click \[Mark Executable] when prompted.

You do not need to continue to the next section, as the executables in <code>/usr/local/bin</code> have elevated privileges.

---

##### Create an Alias #####

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
