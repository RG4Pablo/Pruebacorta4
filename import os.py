import os
import shutil
import sys

def move_files_to_desktop(source_folder):
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    
    try: