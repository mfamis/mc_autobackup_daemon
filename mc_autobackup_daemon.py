import argparse
import datetime
import os
import subprocess
import sys
import time

banner = r"""
                                                      ___  __
 /'\_/`\  __                                        /'___\/\ \__
/\      \/\_\    ___      __    ___   _ __    __   /\ \__/\ \ ,_\
\ \ \__\ \/\ \ /' _ `\  /'__`\ /'___\/\`'__\/'__`\ \ \ ,__\\ \ \/
 \ \ \_/\ \ \ \/\ \/\ \/\  __//\ \__/\ \ \//\ \L\.\_\ \ \_/ \ \ \_
  \ \_\\ \_\ \_\ \_\ \_\ \____\ \____\\ \_\\ \__/.\_\\ \_\   \ \__\
   \/_/ \/_/\/_/\/_/\/_/\/____/\/____/ \/_/ \/__/\/_/ \/_/    \/__/


         ______           __           __                       __
        /\  _  \         /\ \__       /\ \                     /\ \
        \ \ \L\ \  __  __\ \ ,_\   ___\ \ \____     __      ___\ \ \/'\   __  __  _____
         \ \  __ \/\ \/\ \\ \ \/  / __`\ \ '__`\  /'__`\   /'___\ \ , <  /\ \/\ \/\ '__`\
          \ \ \/\ \ \ \_\ \\ \ \_/\ \L\ \ \ \L\ \/\ \L\.\_/\ \__/\ \ \\`\\ \ \_\ \ \ \L\ \
           \ \_\ \_\ \____/ \ \__\ \____/\ \_,__/\ \__/.\_\ \____\\ \_\ \_\ \____/\ \ ,__/
            \/_/\/_/\/___/   \/__/\/___/  \/___/  \/__/\/_/\/____/ \/_/\/_/\/___/  \ \ \/
                                                                                    \ \_\
                                                                                     \/_/
               ____
              /\  _`\
              \ \ \/\ \     __       __    ___ ___     ___     ___
               \ \ \ \ \  /'__`\   /'__`\/' __` __`\  / __`\ /' _ `\
                \ \ \_\ \/\ \L\.\_/\  __//\ \/\ \/\ \/\ \L\ \/\ \/\ \
                 \ \____/\ \__/.\_\ \____\ \_\ \_\ \_\ \____/\ \_\ \_\
                  \/___/  \/__/\/_/\/____/\/_/\/_/\/_/\/___/  \/_/\/_/

                === A tool for reoccurring backups of your Minecraft world! ===
                                (Press Ctrl + C to exit)
"""
print(banner)
parser = argparse.ArgumentParser(description='An application for regularly backing up a Minecraft server world.')
parser.add_argument("--world", default="world", help="Directory of Minecraft world. Defaults to \"world\".")
parser.add_argument("--interval", default=30, type=float, help="Interval of backups (in minutes). Defaults to 30 minutes.")
args = parser.parse_args()

# function for the process of backing up changes and handling the process exceptions
def run_backup(timestamp):
    status = 0
    try:
        subprocess.check_output("git add -A")
        subprocess.check_output("git commit --author=\"MC Autobackup Daemon <>\" -m \"%s: Autobackup\"" % timestamp)
        print("Info: Backup successful.")
    except subprocess.CalledProcessError, error:
        if "nothing to commit" in error.output:
            print("Info: No changes since last backup.")
        else:
            print("Error: Unable to add backup. Check git repository. Error message:")
            print(error.output)
            status = 1
    return status

# check for git install
try:
    print("Info: Checking for git installation.")
    subprocess.check_call("git --version")
except subprocess.CalledProcessError:
    print("Error: This application requires git to be installed. Exiting.")
    sys.exit(1)

# backup current directory, change into Minecraft world directory
cwd = os.getcwd()
os.chdir(args.world)

# check if world directory has a git repo. if not, create repo.
if not os.path.isdir(".git"):
    try:
        print("Info: No git repository found in world directory. Attempting to initialize repository.")
        subprocess.check_call("git init")
    except subprocess.CalledProcessError:
        print("Error: Unable to create git repository in %s directory." % args.world)
        os.chdir(cwd)
        sys.exit(1)

# execute backups until keyboard interrupt occurs (ctrl-c)
status = 0
try:
    while status == 0:
        timestamp = datetime.datetime.now()
        print("Info: Backing up Minecraft world with timestamp %s." % timestamp)
        status = run_backup(timestamp)
        time.sleep(int(args.interval * 60))
except KeyboardInterrupt:
    timestamp = datetime.datetime.now()
    print("Info: Keyboard interrupt caught. Performing one last backup with timestamp %s." % timestamp)
    status = run_backup(timestamp)

# return to previous directory and exit
os.chdir(cwd)
sys.exit(status)