# rclean.py
# recursive clean
# Version: 0.2
# Author: Sriram V Iyer
# 
# 0.1 : Starts from the current directory and deletes the files with matching extensions
# 0.2 : Added command line options to specify base dir to search and extensions 


from os.path import *
import getopt
from os import sys
import os
import platform
       
       
def del_file(fname):
    # Each platform may have is own delete command
    # Add an additional entry for a new platform
    del_command_dict = {
        'Windows' : 'del',
        'Darwin' : 'rm',
        'Linux' : 'rm'
    }
    
    os_name = platform.system()
    
    # If the os_name is not in dictionary, then 
    # return - Don't do any thing!
    if os_name not in del_command_dict.keys():
        print 'Unknown Platform - Can\'t delete'
        return
        
    # Create the command to be executed. This can be later
    # used to print out to debug (if required)
    cmd = del_command_dict[os_name] + ' ' + fname    

    # Execute the command - We can later use the return parameters
    # i.e. the i/p and o/p streams later if required
    os.popen2( cmd )

    
def visit( arg, dirname, names):
    # Get only the files in the directory
    k = [x for x in names if not isdir(x)]
    
    # Check if the file has only the desired extension 
    for x in k:
        ext = x.split(".")[len(x.split(".")) - 1]
        if ext != '' and ext in arg[0]:
            del_file(dirname + '\\' + x )
         
    
def usage():
    print "Usage:" 
    print """   rclean.py --basedir=c:\Sriram --ext="c cpp h" """
    print """   rclean.py --basedir=.  --ext="obj exe" """ 


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["help", "basedir=", "ext="])
    except getopt.GetoptError:
        # print help information and exit: 
        usage()
        sys.exit(2)
        
    ext = [ 'exe', 'pdb', 'pdf', 'doc', 'tgz',
            'ncb', 'lib',  'gz', 'tar', 'pch', 'idb',
            'ilk',  'doc', 'bak', 'xls', 'ppt', 'old',
            'rtf', 'zip']
            
    basedir = "."
    default_basedir = True
    
        
    for o, a in opts:
        if o == "--basedir":
            #print "Base Directory", a 
            basedir = a
            default_basedir = False
        if o == "--ext":
            #print "Extenstions = ", a
            ext = a.split()
            default_ext = False 
        if o == "--help":
            usage()
            sys.exit(0)
    
    arg = [ ext  ]
        
    print "Removing files files with extensions: " 
    print ext; print 
    print  "From folder ", basedir , "(including subfolders) ..."
    
    walk( basedir , visit, arg )
    
    print "Done."