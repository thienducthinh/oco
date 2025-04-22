import os
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

# Run the cleanup function
clean_up_stale_pkl_files()