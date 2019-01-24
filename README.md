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

 1. <code>cd /usr/local/bin/</code>.
 1. <code>sudo touch tasks</code> to create the file. Enter your password when prompted.
 1. <code>sudo nano tasks</code> to edit the file.
 1. Copy and paste the following into your new file:
<pre># This executable file can be executed from anywhere, including a desktop launcher!
cd ~/Software/task-list*/;
python3 run.py </pre>
 5. Save your changes in <code>nano</code> by pressing \[Ctrl X] to exit, \[Y] to save, then \[Enter] to save the name of the file *as is*.
 1. <code>sudo chmod +x tasks</code> to elevate its privilege.

Voilà, your <code>tasks</code> executable is complete, now let's make that desktop launcher.

 7. Right click any spot on the Desktop.
 1. Select \[Create Launcher...].
<pre>Name: Task-List
Command: tasks
[✓] Run in Terminal</pre>
 9. Click \[Create].
 1. Open the new launcher and click \[Mark Executable] when prompted.

You can follow these steps again to make a <code>ptasks</code> executable, but append ' print' to the end of the <code>python3 run.py </code> line in step 4.<br>
You do not need to continue to the next section, as the executables in **/usr/local/bin/** have elevated privileges.

---

##### Create an Alias #####

Instead of doing the 10 steps listed above, these will achieve the same goal, but be advised that you cannot properly run a desktop launcher from an alias.

1. Copy and paste the following block into a Terminal shell:
<pre>echo $'\n# task-list program aliases' >> ~/.bash_aliases
echo 'alias tasks="cd ~/Software/task-list*/; python3 run.py"' >> ~/.bash_aliases
echo 'alias ptasks="cd ~/Software/task-list*/; python3 run.py print"'  >> ~/.bash_aliases
source ~/.bash_aliases
</pre>
 
 Your aliases, <code>tasks</code> and <code>ptasks</code>, are now able to be called, in Terminal, from any folder!
