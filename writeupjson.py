import os
import json

WRITEUPS_DIR = "writeups"
OUTPUT_FILE = "writeups.json"

writeups = []

for folder_name in sorted(os.listdir(WRITEUPS_DIR)):
    folder_path = os.path.join(WRITEUPS_DIR, folder_name)
    if os.path.isdir(folder_path):
        for writeup_name in sorted(os.listdir(folder_path)):
            writeup_path = os.path.join(folder_path, writeup_name)
            if os.path.isdir(writeup_path):
                date_file = os.path.join(writeup_path, "date.txt")
                date = ""
                if os.path.exists(date_file):
                    with open(date_file, "r", encoding="utf-8") as f:
                        date = f.read().strip()
                writeups.append({
                    "folder": folder_name,
                    "name": writeup_name,
                    "date": date
                })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(writeups, f, indent=4)

print(f"{len(writeups)} writeups saved to {OUTPUT_FILE}")

