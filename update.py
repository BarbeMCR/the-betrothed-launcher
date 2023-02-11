import os
import platform
import urllib.request
import zipfile
import io
import configparser
import json

"""The 'update' command."""

def update(installation, version='latest'):
    """Update BarbeMCR's The Betrothed.
    
    Arguments:
    installation -- the target installation
    version -- the version tag
    """
    if os.path.isdir('./'+installation):
        try:
            print("Gathering version information...")
            if version == 'latest':
                if os.path.isfile('./'+installation+'/.version'):
                    with open('./'+installation+'/.version') as ver_info:
                        version_content = ver_info.readlines()
                        old_build = version_content[1]
                else:
                    old_build = '0'
                print("Checking latest version...")
                with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/latest.ini') as latest:
                    latest = latest.read().decode(latest.info().get_param('charset', 'utf-8'))
                config = configparser.ConfigParser()
                config.read_string(latest)
                if int(config['latest']['id']) > int(old_build):
                    needs_updating = True
                else:
                    needs_updating = False
                if needs_updating:
                    if os.path.isfile('./'+installation+'/the_betrothed.exe'):
                        if platform.version().startswith(('10.0', '6.3')):
                            _download('win32', config['latest']['version'], installation)
                        elif platform.version().startswith(('6.0', '6.1', '6.2')):
                            _download('win32_py38', config['latest']['version'], installation)
                        else:
                            print("Unsupported win32 configuration.")
                            print("BarbeMCR's The Betrothed Launcher requires Windows Vista or later.")
                    elif os.path.isfile('./'+installation+'/main.py'):
                        _download('source', config['latest']['version'], installation)
                    else:
                        print("Invalid installation. Please enter a valid BarbeMCR's The Betrothed installation name.")
                else:
                    print(f"Installation {installation} is already updated to the latest version.")
            else:
                if os.path.isfile('./'+installation+'/the_betrothed.exe'):
                    if platform.version().startswith(('10.0', '6.3')):
                        _download('win32', version, installation)
                    elif platform.version().startswith(('6.0', '6.1', '6.2')):
                        _download('win32_py38', version, installation)
                    else:
                        print("Unsupported win32 configuration.")
                        print("BarbeMCR's The Betrothed Launcher requires Windows Vista or later.")
                elif os.path.isfile('./'+installation+'/main.py'):
                    _download('source', version, installation)
                else:
                    print("Invalid installation. Please enter a valid BarbeMCR's The Betrothed installation name.")
        except urllib.error.HTTPError as error:
            print(f"A network error occured. Code {error.code} was returned.")
        except urllib.error.URLError:
            print("Network error. Check your Internet connection and retry.")
    else:
        print("Could not find installation.")

def _download(type, version, installation):
    """Download and update BarbeMCR's The Betrothed.
    
    Arguments:
    type -- the installation type
    version -- the version tag
    installation -- the target installation
    """
    version_exists = True
    with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/versions.json') as versions:
        versions = versions.read().decode(versions.info().get_param('charset', 'utf-8'))
    versions = json.loads(versions)
    if type == 'win32':
        if version in versions['versions_win32']:
            download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32'][version]}"
        else:
            print("Invalid version tag.")
            version_exists = False
    elif type == 'win32_py38':
        if version in versions['versions_win32_py38']:
            download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32_py38'][version]}"
        else:  # Check if just win32_py38 is missing or also regular win32
            if version in versions['versions_win32']:
                print(f"Version {version} does not have a Python 3.8 archive.")
                print(f"BarbeMCR's The Betrothed {version} requires Windows 8.1 or later.")
            else:
                print("Invalid version tag.")
            version_exists = False
    elif type == 'source':
        if version in versions['versions_source']:
            download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_source'][version]}"
        else:
            print("Invalid version tag.")
            version_exists = False
    else:
        print("You should never see this text. In fact, if you do, it means BarbeMCR probably did some kind of error. Please report this bug.")
        version_exists = False
    if version_exists:
        print("Downloading update package...")
        try:
            with urllib.request.urlopen(download_url) as download_file:
                archive_file = zipfile.ZipFile(io.BytesIO(download_file.read()))
            print("Updating...")
            try:
                archive_file.extractall('./'+installation)
                print(f"Successfully updated to version {version}")
            except OSError as error:
                print("The installation could not be updated. More details below.")
                print(error)
        except urllib.error.HTTPError as error:
            print(f"A network error occured. Code {error.code} was returned.")
        except urllib.error.URLError:
            print("Network error. Check your Internet connection and retry.")