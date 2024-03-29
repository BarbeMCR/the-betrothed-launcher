# BarbeMCR's The Betrothed Launcher
An easy-to-use installation manager for BarbeMCR's The Betrothed.

## How do I install the launcher?

**On Windows**
1. Go to the `Releases` page and check for the latest stable version (or any other one, if you want)
2. Download the `.zip` file named like this: `launcher_<version>.zip`
   Requirements:
   - Windows 10 or higher
   - Windows Vista or higher (with Microsoft Visual C++ 2015 installed from [here](https://www.microsoft.com/en-us/download/details.aspx?id=52685))
3. Extract the `.zip` file
4. Start `launcher.exe`

**On macOS or Linux**
1. Download and install Python 3.8 or higher from [python.org](https://python.org), if you haven't already
2. Go to the `Releases` page and check for the latest stable version (or any other one, if you want)
3. Download the `.zip` file named like this: `launcher_<version>_source.zip`
4. Extract the `.zip` file
5. Start `main.py`

**If you want the source code, it works like installing in UNIX**

For compilation instructions on Windows, follow the guide in [the-betrothed](https://github.com/BarbeMCR/the-betrothed) with the following modifications:
 - At step 1, download and extract `launcher_<version>_source.zip` instead of `the_betrothed_<version>_source.zip`;
 - Skip step 6 where Pygame is installed;
 - After following step 9, modify the command in step 8 as follows (keep the `^` symbols unless stated otherwise):
   - change `--specpath <out>` to `--specpath <out>\spec`
   - change `--name "the_betrothed"` to `--name "launcher"`
   - change `--windowed` to `--console`
   - remove `--icon <path_to_icon.ico> ^`
 - Make sure to point `<path_to_main.py>` to the path to the launcher's `main.py` instead of the game's.

## FAQs for BarbeMCR's The Betrothed players

### What is this all about?
BarbeMCR's The Betrothed Launcher is an easy-to-use installation manager for BarbeMCR's The Betrothed.

Which means, it allows you to create, customize, play, update and delete installations very easily. Just type in a few commands into the interpreter and you're off to go.

This is a text-based tool. So, you'll need to learn how to use the commands. It is very easy to do so, though: just type `help` at the interpreter.

The launcher also allows you to easily do the most common savefile management operations.

Finally, it allows you to set a default installation that gets automatically checked for updates on startup and will start if you don't specify an installation.

### Is this mandatory for playing BarbeMCR's The Betrothed?
Absolutely not. Many aspects of the launcher are much more basic than what you get by doing everything yourself (manually).

If you like doing everything manually, this launcher will probably be pretty useless to you.

Instead, this launcher is aimed to assist people who just want to play, without having the hassle of manually installing, updating and maintaining the game.

In conclusion, if you want to, you can play BarbeMCR's The Betrothed like you always did.

### Will the in-game update service stop working?
No. While originally I thought of changing the way updates were fetched, later I decided it would be best to leave that untouched.

So, I extended that system. It now uses a combo of `latest.ini` and `versions.json`.

However, to be honest, I have not completely scrapped the idea of integrating everything into `versions.json`. If I ever switch to that system, it will be far in the future.

You are probably interested in whether you will be forced to using the launcher for automatic updates.

The answer is, again, no. While it is easier to just use the launcher's `update` command (or set your favourite installation as the default one), you will still be able to use the in-game update service to update your game automatically.

### Will the launcher update itself?
Yes, altough you can choose whether to update to the latest version.
Whenever you start the launcher up, if a newer version is available, you will be notified and will be able to accept or deny the update.
If you choose to update, the launcher will do everything automatically.
In order to apply the update, you will need to manually reopen the launcher.

You won't need to update if you don't want to.

### Have any other question?
Post that by going in the `Discussions` tab.
