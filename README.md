# mc_autobackup_daemon
A script to backup a Minecraft world with git

This is just a fun script that I made to make snapshots of a Minecraft world. Using git for Minecraft backups is probably a bad idea, so use at your own risk. :)

> python mc_autobackup_daemon.py -h
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

usage: mc_autobackup_daemon.py [-h] [--world WORLD] [--interval INTERVAL]

An application for regularly backing up a Minecraft server world.

optional arguments:
  -h, --help           show this help message and exit
  --world WORLD        Directory of Minecraft world. Defaults to "world".
  --interval INTERVAL  Interval of backups (in minutes). Defaults to 30
                       minutes.
