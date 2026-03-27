# IBM4680 File Utility

Determines 4680 OS file type  

### Why?  
IBM 4680 OS utilizes four types of files.  
- Direct files  
- Keyed files  
- Random files
- Sequential files

When troubleshooting system bugs technicians dont always know what type of files they are dealing with. This utility is meant to help on those situations.

### Execution
```
python2 file.py EAMITEMR.DAT
```
### 4680 OS notes  
When installing on 4680 OS systems make sure to put the files inside the F: drive


### Compatibility
Tested on python 2.7.18 and above
