# mock-test
Instructions (Windows 10x64):
Some commands may differ depending on OS. Just google it.

:~$Install latest version of Python3 (64 bit).

:~$Install MySQL and MySQL Workbench.

:~$Install  mysql.connector.

:~$Install PIL.

Install virtual environment:

Open cmd 
:~$ pip install virtualenv

Choose destination: 
:~$ cd Desktop> virtualenv YourEnvironmentName
Clone this GitHub repository into local machine.

Go to project directory (GitHub repository) where 'manage.py' file exist.

Copy 'YourEnvironmentName' folder to the 'GitHub repository'.

Active virtual environment:

:~$ cd YourEnvironmentName\Scripts>

:~$ activate

(YourEnvironmentName) :~$ This '(YourEnvironmentName)' sign will be shown up if virtual environment activated successfully.

:~$ cd../.. (exit from Scripts)

Install all the requirements using previously opened CMD where the virtual environment was activated:

(YourEnvironmentName):~$ pip install -r requirements.txt

