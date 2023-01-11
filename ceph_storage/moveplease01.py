#!/usr/bin/env python3

# Bringing in the required libraries
import shutil
import os

def main():
    os.chdir('/home/student/mycode/')

    """Makes an attempt to move a raynor.obj file to the ceph_storage"""
    try:
        shutil.move('raynor.obj','ceph_storage/')
    except Exception as err:
        print(f"Error: {err}")
    
    xname = input('What is the new name for kerrigan.obj? ') # Gets a user input for file name

    """ Makes an attempt to rename the kerrigan.obj"""
    try:        
        shutil.move('ceph_storage/kerrigan.obj','ceph_storage/'+xname)
    except Exception as err:
        print(f"Error: {err}")


# Runs the program if it is executed directly and not imported to another file
if __name__ == '__main__':
    main()