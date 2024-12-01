# // CONFIG // 
# This is the logo. I recommend use an ASCII art from https://patorjk.com/software/taag/
the_logo = """

      ::::::::  :::    ::: ::::::::::: :::::::::   ::::::::  :::::::::  :::        :::::::: ::::::::::: ::::::::::: 
    :+:    :+: :+:   :+:      :+:     :+:    :+: :+:    :+: :+:    :+: :+:       :+:    :+:    :+:         :+:      
   +:+        +:+  +:+       +:+     +:+    +:+ +:+        +:+    +:+ +:+       +:+    +:+    +:+         +:+       
  +#++:++#++ +#++:++        +#+     +#+    +:+ +#++:++#++ +#++:++#+  +#+       +#+    +:+    +#+         +#+        
        +#+ +#+  +#+       +#+     +#+    +#+        +#+ +#+        +#+       +#+    +#+    +#+         +#+         
#+#    #+# #+#   #+#      #+#     #+#    #+# #+#    #+# #+#        #+#       #+#    #+#    #+#         #+#          
########  ###    ### ########### #########   ########  ###        ########## ######## ###########     ###           

"""
zip_file_for_the_download = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-large-zip-file.zip" # change this - this is the zip file url
folder_name_for_ext = "skidsploit" # change this, this is the folder name.
discord = "https://discord.gg/skidsploit" # discord url
executor_name = "skidsploit" # name of your executor

# END OF CONFIG
# DO NOT TOUCH ANYTHING BEYOND THIS POINT
# UNLESS YK WHAT YOU'RE DOING!
# kz0x1 was here

import os
# Check and install required packages
required_packages = ['requests', 'pystyle']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, '--quiet'])
import time
import requests
import zipfile
from pystyle import Colors, Colorate
name = executor_name

os.system(f"title {name} Updater")
os.system("cls")

logo = the_logo
print(Colorate.Diagonal(Colors.blue_to_purple, logo))
txt = f"[!] Our only official download is at {discord}. \nAnyone else claiming to be us is not safe. Please only download from the discord server."
print(Colorate.Diagonal(Colors.yellow_to_red, txt))

def pr(txt):
    print(Colorate.Diagonal(Colors.red_to_blue, f"[LOGS]: {txt}"))

pr("@kz0x1 was here. :)")

def download_and_extract(url, extract_to):
    pr("Downloading...")
    temp_dir = os.path.join(os.getenv('TEMP'), name)
    os.makedirs(temp_dir, exist_ok=True)
    
    local_filename = os.path.join(temp_dir, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    
    time.sleep(2)
    pr("Downloaded.")
    pr("Installing...")
    
    extract_folder = os.path.join(extract_to, folder_name_for_ext)
    os.makedirs(extract_folder, exist_ok=True)
    
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    fls = extract_folder.split("\\")
    flname = fls[-1]
    pr(f"Installed to {flname} on your desktop!")
    os.remove(local_filename)
    pr("Temp files cleaned up")

url = zip_file_for_the_download

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
onedrive_desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

if os.path.exists(onedrive_desktop_path):
    extract_to = onedrive_desktop_path
else:
    extract_to = desktop_path

download_and_extract(url, extract_to)
input("Press ENTER to exit.")
os.system("cls")
