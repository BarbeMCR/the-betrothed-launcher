import os

"""The 'modernize' and 'unmodernize' commands."""

def modernize(installation, version):
    """Add version information to old installations.
    
    Arguments:
    installation -- the target installation
    version -- the version name
    """
    if os.path.isdir('./'+installation):
        if not os.path.isfile('./'+installation+'/.version'):
            if version in versions_db:
                with open('./'+installation+'/.version', 'w') as ver_info:
                    ver_info.write(version)
                    ver_info.write('\n')
                    ver_info.write(versions_db[version])
                print(f"Successfully added version information to {installation}")
            else:
                print("Version name is not valid (not pre-0.20).")
        else:
            print("Installation has already been modernized.")
    else:
        print("Could not find installation.")

def unmodernize(installation):
    """Remove version information from old installations.
    
    Arguments:
    installation -- the target installation
    """
    if os.path.isdir('./'+installation):
        if os.path.isfile('./'+installation+'/.version'):
            old = False
            with open('./'+installation+'./.version') as ver_info:
                if ver_info.readlines()[0].rstrip() in versions_db:
                    old = True
            if old:
                os.remove('./'+installation+'/.version')
                print(f"Successfully removed version information from {installation}")
                print("You should now add version information again by using 'modernize'.")
            else:
                print("Installation is not pre-0.20!")
    else:
        print("Could not find installation.")

versions_db = {  # Some of these build IDs were recreated after the respective version was released
    "0.01": "1010",
    "0.02": "2050",
    "0.03": "2120",
    "0.04": "3060",
    "0.05": "5060",
    "0.05a": "5061",
    "0.06": "5150",
    "0.07": "6020",
    "0.07a": "6030",
    "0.07b": "6031",
    "0.08": "6040",
    "0.08a": "6050",
    "0.09": "6110",
    "0.09a": "6111",
    "0.10": "6170",
    "0.11": "6230",
    "0.11a": "7050",
    "0.12": "7130",
    "0.13": "8050",
    "0.14": "8070",
    "0.14a": "8080",
    "0.14b": "8081",
    "0.15": "8290",
    "0.16": "11060",
    "0.17": "11130",
    "0.18": "11200",
    "0.18a": "11210",
    "0.19": "11270"
}