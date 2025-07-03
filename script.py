import os
import shutil
import time

def backup_files(source_dir, backup_dir):
    #creating timestamp for teh backup folder
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_folder=os.path.join(backup_dir,f"backup_{timestamp}")

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    for filename in os.listdir(source_dir):
        source_file=os.path.join(source_dir, filename)
        backup_file=os.path.join(backup_folder,filename)

        if os.path.isfile(source_file):
            shutile.copy2(source_file,backup_file)
