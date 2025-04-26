import os
import shutil
import glob

def clean_up_stale_pkl_files():
    """
    Remove stale .pkl and .cw127.pkl files in the font directory.
    """
    # Define the path to the font file
    font_path = "font/SF-Pro-Rounded-Regular.ttf"
    font_dir = os.path.dirname(font_path)

    # Search for all .pkl and .cw127.pkl files in the font directory
    pkl_files = glob.glob(os.path.join(font_dir, "*.pkl"))
    cw127_pkl_files = glob.glob(os.path.join(font_dir, "*.cw127.pkl"))

    # Combine all matching files
    stale_files = pkl_files + cw127_pkl_files

    # Remove each stale file
    for stale_file in stale_files:
        if os.path.exists(stale_file):
            try:
                os.remove(stale_file)
                print(f"Removed stale cache: {stale_file}")
            except Exception as e:
                print(f"Failed to remove {stale_file}: {e}")

def clean_pycache(root_dir):
    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove __pycache__ directories
        if os.path.basename(dirpath) == "__pycache__":
            shutil.rmtree(dirpath)
            print(f"Deleted: {dirpath}")
        # Remove .pyc files
        for filename in glob.glob(os.path.join(dirpath, "*.pyc")):
            os.remove(filename)
            print(f"Deleted: {filename}")


def clean_up():
    # Define the root directory
    root_dir = "."
    # Clean up __pycache__ directories and .pyc files
    clean_pycache(root_dir)

    # Clean up stale .pkl files
    clean_up_stale_pkl_files()
# Run the cleanup function
clean_up()
if __name__ == "__main__":
    clean_up()