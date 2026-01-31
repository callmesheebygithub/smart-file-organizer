# 📂 SA Hive Automations Smart File Organizer

Smart File Organizer is a simple **Python + Streamlit** app that helps you automatically organize files in any folder by **date** and **file type**.  

Files are moved into **date-based folders** and then sorted into **subfolders by file extension**, preventing clutter in your directories.

---

## 🔹 Features

- Automatically creates folders based on file **creation date** (Windows) or **modification date** (Mac/Linux).  
- Subfolders for **file types** (e.g., `.pdf`, `.jpg`, `.txt`).  
- Handles files with **duplicate names** safely by appending a counter.  
- Easy-to-use **Streamlit interface**.  
- Supports **any folder** on your system.  

 ```
 ```
## 🔹 Installation

1. Clone the repository:
  bash
   git clone https://github.com/callmesheebygithub/smart-file-organizer.git

2. Navigate into the project folder:

   ```bash
   cd smart-file-organizer
   ```
3. Install dependencies:

   ```bash
   pip install streamlit
   ```

---

## 🔹 Usage

1. Run the Streamlit app:

   ```bash
   streamlit run App.py
   ```
2. Enter the **folder path** you want to organize.
   Example: `C:/Users/Administrator/Downloads`
3. Click the **"🚀 Organize Files"** button.
4. The app will create **date folders** and **file-type subfolders** and move your files accordingly.

---

## 🔹 How It Works

* **Get file date:** Uses **creation date** on Windows, **modification date** on other OS.
* **Organize files:** Creates folders for each date and then subfolders by file extension.
* **Safe move:** Prevents overwriting files by appending a counter to duplicate filenames.

---

## 🔹 Example Folder Structure After Organizing

```
Downloads/
│
├── 2026-02-01/
│   ├── pdf/
│   │   └── file1.pdf
│   ├── jpg/
│   │   └── image1.jpg
│   └── no_extension/
│       └── README
│
├── 2026-02-02/
│   └── txt/
│       └── notes.txt
```

---

## 🔹 Screenshots

!Screenshot 2026-02-01 010315.png

---

## 🔹 License

This project is **open-source**. Feel free to modify and use it freely.
---

Made with ❤️ by **SA Hive Automations**

```
