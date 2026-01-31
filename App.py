import os
import shutil
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Smart File Organizer", layout="centered")

# st.title("📂SA Hive Automations Smart File Organizer", layout="centered")
st.markdown(
    """
    <h1 style='text-align: center;'>
        📂 SA Hive Automations Smart File Organizer
    </h1>
    """,
    unsafe_allow_html=True
)
st.write("Organize files into date folders and file-type subfolders automatically.")

# Folder path input
folder_path = st.text_input("Enter Folder Path to Organize (Example: C:/Users/Administrator/Downloads)")

def get_file_date(file_path):
    """Get file date (creation on Windows, modified on others)."""
    if os.name == 'nt':  # Windows
        timestamp = os.path.getctime(file_path)
    else:  # Mac/Linux
        timestamp = os.path.getmtime(file_path)

    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

def organize_files_by_date_and_type(folder):
    moved_files = 0

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Skip directories (like already created date folders)
        if os.path.isdir(file_path):
            continue

        try:
            # Get date folder
            file_date = get_file_date(file_path)
            date_folder = os.path.join(folder, file_date)

            # Get extension safely
            name, ext = os.path.splitext(filename)
            ext = ext[1:].lower() if ext else "no_extension"
            type_folder = os.path.join(date_folder, ext)

            # Create folders if not exist
            os.makedirs(type_folder, exist_ok=True)

            # Prevent overwrite if same file name exists
            new_path = os.path.join(type_folder, filename)
            counter = 1
            base_name, extension = os.path.splitext(filename)

            while os.path.exists(new_path):
                new_filename = f"{base_name}_{counter}{extension}"
                new_path = os.path.join(type_folder, new_filename)
                counter += 1

            # Move file
            shutil.move(file_path, new_path)
            moved_files += 1

        except Exception as e:
            st.error(f"Error moving {filename}: {e}")

    return moved_files

if st.button("🚀 Organize Files"):
    if os.path.exists(folder_path):
        with st.spinner("Organizing files..."):
            total = organize_files_by_date_and_type(folder_path)
        st.success(f"✅ Done! {total} files organized successfully.")
    else:
        st.error("❌ Invalid folder path. Please check and try again.")
