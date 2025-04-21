import os

# Clean up stale .pkl files

def clean_up_stale_pkl_files():
    """
    Remove stale .pkl files that are not needed anymore.
    """
    # Define the path to the font file and the corresponding .pkl files
    font_path = "font/SF-Pro-Rounded-Regular.ttf"
    for pkl_file in ["SF-Pro-Rounded-Regular.pkl", "SF-Pro-Rounded-Regular.cw127.pkl"]:
        pkl_path = os.path.join(os.path.dirname(font_path), pkl_file)
        if os.path.exists(pkl_path):
            try:
                os.remove(pkl_path)
                print(f"Removed stale cache: {pkl_path}")
            except Exception as e:
                print(f"Failed to remove {pkl_path}: {e}")

clean_up_stale_pkl_files()