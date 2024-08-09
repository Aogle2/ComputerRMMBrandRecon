Hello, this little project is a demostration on how to present data from a Database.
Just a small idea on how presenting data can be done and should give an idea the diversity of Operating Systems, Vendors and Manufacturers.

## Tools and items used in this

Python 3
Virtual enviroment (venv)
Git

## Modules used

Matplotlib
Pandas
Sqlite3

## Databases Used

sqlite


## Summary of what each part does

Python 3, the main engine of getting this to work.

venv is a built in module in Python 3 that allows the programmer to isolate what packages are needed and a way to easily install them. Prevents the "It worked on my computer" situation.

Git, You're reading this now...on Github, However Git is used as source control to keep track and blame people properly.

Matplotlib, this is used to show data visualy can do a lot for a person that wants to go above excel sheets and presentations.

Pandas, this is data cleaning and anayalist and a lot more but for here I am useing it to pull data from sqlite into a dataframe I can mess with.

Sqlite3, this is a bultin module in python 3 this is used to interact with Sqlite databases. This is also very much cross platform..something that this project strives for.

Sqlite is a database that is used for local databases but is extreamly fast for reading, this is what is hosting all my data for this project.



## Getting Started On Windows Based Systems

What you will need for this application to work on your system:

1. Download and Install Git from this link: https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe

2. Download and install Python 3 from this link: https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe


Once steps 1 and 2 are completed in any order:
1. Click on Start
2. Type "CMD"
3. If you are not at ``` C:\Users\Your_Profile_Name> ```
	Type ``` cd ~ ``` to get to that location.

Then Type/copy and paste:

4. ``` git glone https://github.com/Aogle2/Computer_RMM_Brand_Recon.git ``` 

Wait for the clone to finish

5. ``` cd Computer_RMM_Brand_Recon ```

6. ``` python -m venv venv ```

7. ``` source venv\scripts\activate ```

8. ``` pip install -r requirements.txt ```

Wait for pip to install all the requirements.

9. ```python userinteraction.py```

10. Enjoy the little demo and click around? It's fairly easy to break but shows a bit of what is possible and what could be inspired by it.

When done type in ``` deactivate ``` to leave the virtual enviroment.


## Getting Started On MacOS Based Systems

Git is already installed on MacOS Systems, nothing is neededing to be done on that part.

###This is assuming you are using the MacOS Sonoma. Older versions will have a simular process, just a diffrent version of Python.

1. Download an install Python 3 from: https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg

2. Open up Terminal from LaunchPad.

3. Type or Copy and Paste: ```git clone https://github.com/Aogle2/Computer_RMM_Brand_Recon.git```

4. ``` cd Computer_RMM_Brand_Recon ```

5. ``` python3 -m venv venv ```

7. ``` pip install -r requirements.txt ```

8. ``` source venv/bin/activate ```

This part will take some time to complete.

9. ``` python3 userinteraction.py ```

10. Enjoy and explore around?...there are some bugs for this and is easy to break.

When done, type in ```deactivate``` to leave the virtual enviroment.
