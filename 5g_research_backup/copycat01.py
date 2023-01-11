#!/usr/bin/env python3

# necessary libraries needed
import shutil
import os

def main():
    os.chdir("/home/student/mycode/") # move to mycode directory

    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy") # Make a copy of file

    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/") # Copy directory

if __name__ == "__main__":
    main()
