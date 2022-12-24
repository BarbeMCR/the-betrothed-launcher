import os

"""The 'default' command."""

def default(installation):
    """Set an installation as the default one.
    
    Arguments:
    installation -- the target installation
    """
    if os.path.isdir('./'+installation):
        if os.path.isfile('./'+installation+'/the_betrothed.exe') or os.path.isfile('./'+installation+'/main.py'):
            with open('./.default', 'w') as default_file:
                default_file.write(installation)
            print(f"Successfully updated default installation to {installation}")
        else:
            print("Invalid installation. Please enter a valid BarbeMCR's The Betrothed installation name.")
    else:
        print("Could not find installation.")