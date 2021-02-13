
# USER GUIDE

## Using Version Control in VS Code

### SCM Providers
```
Source Control view (⌃⇧G)
```

### Commit
```
If you commit your change to the wrong branch, undo your commit using the Git: Undo Last Commit command in the Command Palette (⇧⌘P).
```

### Cloning a repository
```
clone a Git repository with the Git: Clone command in the Command Palette (⇧⌘P)
```

### Branches and Tags
```
Git: Create Branch and Git: Checkout to commands in the Command Palette (⇧⌘P).
```

---
# PYTHON

## Tutorial

### Verify the Python installation
```
python3 --version
```

### Start VS Code in a project (workspace) folder
```
mkdir hello
cd hello
code .

By starting VS Code in a folder, that folder becomes your "workspace". VS Code stores settings that are specific to that workspace in .vscode/settings.json, which are separate from user settings that are stored globally.
```

### Select a Python interpreter
```
Command Palette (⇧⌘P)
    Python: Select Interpreter

    File > Preferences > Settings (Code > Preferences > Settings on macOS), then select the Workspace Settings tab.
```

### Create a Python Hello World source code file

### Run Hello World
- Right-click anywhere in the editor window and select Run Python File in Terminal (which saves the file automatically):
- Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. This command is convenient for testing just a part of a file.
- From the Command Palette (⇧⌘P), select the Python: Start REPL command to open a REPL terminal for the currently selected Python interpreter. In the REPL, you can then enter and run lines of code one at a time.

### Configure and run the debugger
```
F5
```

### Install and use packages
- Create and activate the virtual environment
```
For macOS/Linux

python3 -m venv .venv
source .venv/bin/activate
```
- Select your new environment by using the Python: Select Interpreter command from the Command Palette.
- Install the packages
```
# macOS
python3 -m pip install matplotlib
```
