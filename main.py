#!/usr/bin/env python3

# BarbeMCR's The Betrothed Launcher, an easy-to-use installation manager for BarbeMCR's The Betrothed
# Copyright (C) 2022  BarbeMCR
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import traceback
import datetime
import time
import ctypes
import os
import urllib.request
import configparser
import random
from list import list
from play import play
from install import install
from download import download
from extract import extract
from update import update
from uninstall import uninstall
from rename import rename
from duplicate import duplicate
from default import default
from transfer import transfer
from sync import sync
from clean import clean
from reset import reset
from modernize import modernize, unmodernize
from help import display_help

def main():
    version = "1.0.0"
    build = 100
    print_splash(version)
    check_game_updates()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW(f"BarbeMCR's The Betrothed Launcher {version}")
    try:
        while True:
            parse()
    except EOFError:
        print("EOF hit. Now exiting...")
        time.sleep(2.5)
        sys.exit()
    except Exception:
        display_traceback(traceback.format_exc())

def print_splash(version):
    """Print the splash text that appears on startup.
    
    Arguments:
    version -- the launcher version
    """
    print(f"BarbeMCR's The Betrothed Launcher {version}")
    print("Copyright (C) 2022  BarbeMCR")
    print()
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions. Read 'license.txt' for details.")
    print()
    print(choose_random_splash())
    print("If you don't know where to start, type 'help' for more information.")
    print()

def check_game_updates():
    """Check whether the default installation can be updated."""
    if os.path.isfile('./.default'):
        with open('./.default') as default:
            target = default.readline()
        if os.path.isdir('./'+target):
            if os.path.isfile('./'+target+'/.version'):
                try:
                    with open('./'+target+'/.version') as ver_info:
                        old_build = ver_info.readlines()[1]
                    with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/latest.ini') as latest:
                        latest = latest.read().decode(latest.info().get_param('charset', 'utf-8'))
                    config = configparser.ConfigParser()
                    config.read_string(latest)
                    if int(config['latest']['id']) > int(old_build):
                        print(f"Installation {target} can be updated to version {config['latest']['version']}.")
                        will_update = input("Do you want to do that now (y/n)? ")
                        if will_update.lower() == 'y':
                            update(target)
                        print()
                except urllib.error.HTTPError:
                    pass
                except urllib.error.URLError:
                    pass

def parse():
    """Parse and run commands."""
    try:
        command = input(" ? ")
        command = command.split()
        opcode = command[0] if len(command)>=1 else None
        args = command[1:] if len(command)>=2 else [None]
        if opcode == 'list':
            list(args[0])
        elif opcode == 'play':
            play(args[0])
        elif opcode == 'install':
            if len(args) == 1 and args[0] is not None:
                install(args[0])
            elif len(args) == 2:
                install(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'download':
            if len(args) == 1 and args[0] is not None:
                download(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'extract':
            if len(args) == 2:
                extract(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'update':
            if len(args) == 1 and args[0] is not None:
                update(args[0])
            elif len(args) == 2:
                update(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'uninstall':
            if len(args) == 1 and args[0] is not None:
                uninstall(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'rename':
            if len(args) == 2:
                rename(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'duplicate':
            if len(args) == 2:
                duplicate(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'default':
            if len(args) == 1 and args[0] is not None:
                default(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'transfer':
            if len(args) == 2:
                transfer(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'sync':
            if len(args) == 1 and args[0] is not None:
                sync(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'clean':
            if len(args) == 1 and args[0] is not None:
                clean(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'reset':
            if len(args) == 1 and args[0] is None:
                reset()
            else:
                print("Wrong arguments.")
        elif opcode == 'modernize':
            if len(args) == 2:
                modernize(args[0], args[1])
            else:
                print("Wrong arguments.")
        elif opcode == 'unmodernize':
            if len(args) == 1 and args[0] is not None:
                unmodernize(args[0])
            else:
                print("Wrong arguments.")
        elif opcode == 'help':
            display_help(args[0])
        elif opcode == 'exit':
            sys.exit()
        elif opcode is None:
            pass
        else:
            print("Invalid command.")
    except KeyboardInterrupt:
        print("Operation cancelled.")

def choose_random_splash():
    """Return a random splash."""
    splashes = [
        "Also try BarbeMCR's The Betrothed!",
        "Easy installation management here!",
        "Easy savefile management here!",
        "Easy *insert something* management here!",
        "Also try mlmcr!",
        "Want even more customization? Nope!",
        "Updating has never been easier!",
        "What was BarbeMCR thinking?",
        "The best way to experience BarbeMCR's The Betrothed yet!",
        "Always report bugs! (plz)",
        "More info at https://github.com/BarbeMCR/the-betrothed-launcher",
        "Since 2022!",
        "Easier than ever!",
        "This is what you're gettin'!",
        "Why is this text-based?!?",
        "Can you get enough of me?"
    ]
    return random.choice(splashes)

def display_traceback(tb):
    """Display crash information and generate a report.
    
    Arguments:
    tb - The traceback string
    """
    tb = tb.split("\n")
    print()
    print("A launcher crash occured! Keep calm and report this crash")
    print("with its traceback after generating a crash report.")
    print()
    for line in tb:
        print(line)
    print("What do you want to do?")
    print("report -- Get report and quit")
    print("quit   -- Quit without reporting")
    while True:  # Do-while loop equivalent
        choice = input(" ? ")
        if choice.lower() in ['report', 'quit']:
            break
        else:
            print("Invalid choice.")
    if choice.lower() == 'report':
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        with open(f'./crash_{timestamp}.txt', 'w') as report:
            report.write("-- BarbeMCR's The Betrothed Launcher Crash Report --\n")
            report.write(f"Timestamp: {timestamp}\n")
            for line in tb:
                report.write(line + "\n")
        print(f"Crash report 'crash_{timestamp}.txt' saved.")
        print("Now exiting...")
        time.sleep(5)
        sys.exit()
    elif choice.lower() == 'quit':
        print("Now exiting...")
        time.sleep(2.5)
        sys.exit()

if __name__ == '__main__':
    main()