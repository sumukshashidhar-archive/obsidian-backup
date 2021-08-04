"""
A simple script to backup stuff
"""


# IMPORTS
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

# load env vars
load_dotenv()

class Encryptions:

    def __init__(self) -> None:
        pass


    def write_key():
        """
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    
    def load_key():
        return open("key.key", "rb").read()

    def encrypt():
        """
        In order to avoid messing with the main file system, we will not directly modify the files. Instead, we will make a copy of those files elsewhere, and start to modify those files. 

        Hence, the first process will be to copy the files to a backup path.
        """
        pass

    def folder_backup():
        """
        Copies all the files in the source directory to a specified backup directory
        """
        doc_path = os.getenv("OBSIDIAN_FOLDER")
        bck_path = os.getenv("TMP_PATH")
        os.system(f"cp -R {doc_path} {bck_path}/")
        return

    def folder_delete():
        """
        Deletes the tmp folder after completion
        """
        bck_path = os.getenv("TMP_PATH")
        os.system(f"rm -rf {bck_path}")
        return 

        




