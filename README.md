
# 🔐 File Encrypter & Decrypter (with GUI)

This project provides a user-friendly interface for encrypting and decrypting text using the **Fernet symmetric encryption** system from the `cryptography` module. Built with **Tkinter**, the application supports secure key generation, clipboard operations, and file handling for both encryption and decryption tasks.

---

## 📂 Features

### ✅ Encrypter
- Encrypt plain text from:
  - Manual input
  - Loaded `.txt` files
  - Clipboard
- Generate and save secure encryption keys (`.key`)
- Load existing `.key` files
- Output encrypted content:
  - Display in GUI
  - Copy to clipboard
  - Save to timestamped file

### ✅ Decrypter
- Decrypt encrypted messages from:
  - Manual input
  - Clipboard
- Load `.key` files
- Output decrypted content:
  - Display in GUI
  - Copy to clipboard
  - Save to timestamped file

---

## 🖼 GUI Interface Overview

The application is split into labeled sections using **Tkinter**’s `ttk.LabelFrame`:

- **Input Section**: Accepts raw text or encrypted strings.
- **Key Section**: For loading or generating `.key` files.
- **Output Section**: Shows the result of encryption/decryption.
- **Status Bar**: Shows feedback after each operation (e.g., success, error messages).

---

## 📦 Dependencies

Install the required libraries before running:

```bash
pip install cryptography pyperclip
```

---

## 🚀 Usage

### ▶️ Run the Encrypter
```bash
python encrypter.py
```

### ▶️ Run the Decrypter
```bash
python decrypter.py
```

Each opens its own dedicated GUI window.

---

## 🔐 Encryption Flow

1. **Input Text** → type or load a file
2. **Generate/Load Key** → generates `.key` file or load existing one
3. **Encrypt** → displays the encrypted string in output
4. **Save/Copy** → store encrypted output to a file or clipboard

---

## 🔓 Decryption Flow

1. **Input Encrypted Text** → paste or type
2. **Load Key** → load the `.key` used for encryption
3. **Decrypt** → displays decrypted result
4. **Save/Copy** → export or copy decrypted data

---

## 🛠 File Naming

- Encrypted files: `encrypted_YYYYMMDD_HHMMSS.txt`
- Decrypted files: `decrypted_YYYYMMDD_HHMMSS.txt`
- Keys: `key.key`

---

## 🔒 Security Note

Keep your `key.key` file secure. Anyone with access to the key can decrypt your encrypted content.

---

## 📁 Project Structure

```
├── encrypter.py   # GUI for encryption
├── decrypter.py   # GUI for decryption
└── key.key        # (optional) Generated encryption key
```

---

## 📌 To-Do / Improvements

- Add password-based key generation
- Support file decryption (.txt)
- Add drag-and-drop support for files
- Dark mode toggle for the GUI

---

## 👨‍💻 Author

Built with passion using Python and Tkinter GUI.  
🔐 Empowering beginners to learn encryption securely and visually.
