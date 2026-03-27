# IBM4680 File Utility

Determines 4680 OS file type  

### Why?  

IBM 4680 OS utilizes four types of files.  
- Direct files  
- Keyed files  
- Random files
- Sequential files

When troubleshooting system bugs technicians don't always know what type of files they are dealing with. This utility is meant to help in those situations.

## Setup on 4680 OS  

When installing on 4680 OS systems make sure to put the files inside the F: drive.  

In this example we'll create the file_app folder to store the files and using the DEFINE command to make a logical name.

1. Put the files in the folder f:/file_app  
2. Go to the command mode and run the following command  
```
DEFINE FILE=PYTHON2 f:/file_app/file.py
```
Now you can execute the FILE command from any directory.  

## Execution

<img width="678" height="106" alt="file" src="https://github.com/user-attachments/assets/660ab2dd-72b0-4530-980b-f5b6a8fcf798" />

### Compatibility

- Tested on python 2.7.18 and above  
- 4680OS / Linux / MacOS / Windows
