import os
import shutil
import subprocess

# --- Configuration ---
FILE_NAMES = ["keyboard.mp3", "keyboard script.py"]  # Files to find
TARGET_FOLDER = "Keyboard"               # Folder to create
RUN_FILE = "keyboard script.py"                       # File to execute

def main():
    # 1. Create the named folder if it doesn't exist
    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
        print(f"Created folder: {TARGET_FOLDER}")

    found_paths = []
    
    # 2. Find the paths of the specific files recursively
    print("Searching for files...")
    for root, dirs, files in os.walk("."): # Starts search from current directory
        for file in files:
            if file in FILE_NAMES:
                full_path = os.path.join(root, file)
                found_paths.append(full_path)
                print(f"Found: {full_path}")

    # 3. Copy found files into the named folder
    for path in found_paths:
        shutil.copy(path, TARGET_FOLDER)
        print(f"Copied {os.path.basename(path)} to {TARGET_FOLDER}")

    # 4. Run the specific file in that folder
    exec_path = os.path.join(TARGET_FOLDER, RUN_FILE)
    if os.path.exists(exec_path):
        print(f"Executing: {RUN_FILE}")
        # Use 'python' for scripts or just the path for executables
        subprocess.run(["python", exec_path]) 
    else:
        print(f"Error: {RUN_FILE} not found in {TARGET_FOLDER}")

if __name__ == "__main__":
    main()
