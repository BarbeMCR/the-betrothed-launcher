import os
import sys
import zipfile
import urllib.request
import json
import configparser
import io
import string

"""The 'install' command."""

def install(version, target=None):
    """Download and install BarbeMCR's The Betrothed.
    
    Arguments:
    version -- the version tag
    target -- the installation directory
    """
    error_occured = False
    try:
        print("Gathering version information...")
        if version == 'latest':
            print("Resolving latest version...")
            with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/latest.ini') as latest:
                latest = latest.read().decode(latest.info().get_param('charset', 'utf-8'))
            config = configparser.ConfigParser()
            config.read_string(latest)
            version = config['latest']['version']
            with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/versions.json') as versions:
                versions = versions.read().decode(versions.info().get_param('charset', 'utf-8'))
            versions = json.loads(versions)
            if sys.platform.startswith('win32'):
                import platform
                if platform.version().startswith(('10.0', '6.3')):
                    if version in versions['versions_win32']:
                        download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32'][version]}"
                    else:
                        print("Invalid version tag.")
                        error_occured = True
                elif platform.version().startswith(('6.0', '6.1', '6.2')):
                    if version in versions['versions_win32_py38']:
                        download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32_py38'][version]}"
                    else:  # Check if just win32_py38 is missing or also regular win32
                        if version in versions['versions_win32']:
                            print(f"Version {version} does not have a Python 3.8 archive.")
                            print(f"BarbeMCR's The Betrothed {version} requires Windows 8.1 or later.")
                        else:
                            print("Invalid version tag.")
                            error_occured = True
                else:
                    print("Unsupported win32 configuration.")
                    print("BarbeMCR's The Betrothed Launcher requires Windows Vista or later.")
            else:
                if version in versions['versions_source']:
                    download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_source'][version]}"
                else:
                    print("Invalid version tag.")
                    error_occured = True
        else:
            with urllib.request.urlopen('https://raw.githubusercontent.com/BarbeMCR/the-betrothed/main/versions.json') as versions:
                versions = versions.read().decode(versions.info().get_param('charset', 'utf-8'))
            versions = json.loads(versions)
            if sys.platform.startswith('win32'):
                import platform
                if platform.version().startswith(('10.0', '6.3')):
                    if version in versions['versions_win32']:
                        download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32'][version]}"
                    else:
                        print("Invalid version tag.")
                        error_occured = True
                elif platform.version().startswith(('6.0', '6.1', '6.2')):
                    if version in versions['versions_win32_py38']:
                        download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_win32_py38'][version]}"
                    else:  # Check if just win32_py38 is missing or also regular win32
                        if version in versions['versions_win32']:
                            print(f"Version {version} does not have a Python 3.8 archive.")
                            print(f"BarbeMCR's The Betrothed {version} requires Windows 8.1 or later.")
                        else:
                            print("Invalid version tag.")
                            error_occured = True
                else:
                    print("Unsupported win32 configuration.")
                    print("BarbeMCR's The Betrothed Launcher requires Windows Vista or later.")
            else:
                if version in versions['versions_source']:
                    download_url = f"https://github.com/BarbeMCR/the-betrothed/releases/download/{version}/{versions['versions_source'][version]}"
                else:
                    print("Invalid version tag.")
                    error_occured = True
    except urllib.error.HTTPError as error:
        print(f"A network error occured. Code {error.code} was returned.")
        error_occured = True
    except urllib.error.URLError:
        print("Network error. Check your Internet connection and retry.")
        error_occured = True
    if not error_occured:
        print("Downloading installation package...")
        try:
            with urllib.request.urlopen(download_url) as download_file:
                archive_file = zipfile.ZipFile(io.BytesIO(download_file.read()))
            print("Installing...")
            if target is None:
                try:
                    os.mkdir(f'./{version}')
                    archive_file.extractall(f'./{version}')
                    print(f"Successfully installed version {version}")
                except OSError as error:
                    print("The installation could not be created. More details below.")
                    print(error)
            else:
                if not any([whitespace in target for whitespace in string.whitespace]):
                    try:
                        os.mkdir(f'./{target}')
                        archive_file.extractall(f'./{target}')
                        print(f"Successfully installed version {version}")
                    except OSError as error:
                        print("The installation could not be created. More details below.")
                        print(error)
                else:
                    print("Target contains whitespace and is not a valid installation name.")
        except urllib.error.HTTPError as error:
            print(f"A network error occured. Code {error.code} was returned.")
        except urllib.error.URLError:
            print("Network error. Check your Internet connection and retry.")