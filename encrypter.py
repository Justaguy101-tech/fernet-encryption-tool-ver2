from cryptography.fernet import Fernet
import os
from datetime import datetime
import pyperclip
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class EncrypterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Encrypter")
        self.window.geometry("600x500")
        self.fernet = None
        
        self.setup_gui()

    def setup_gui(self):
        # Input section
        input_frame = ttk.LabelFrame(self.window, text="Data to Encrypt", padding=10)
        input_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.input_text = tk.Text(input_frame, height=8)
        self.input_text.pack(fill="both", expand=True)

        input_btn_frame = ttk.Frame(input_frame)
        input_btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(input_btn_frame, text="Load File", command=self.load_file).pack(side="left", padx=5)
        ttk.Button(input_btn_frame, text="Paste", command=self.paste_text).pack(side="left", padx=5)

        # Key management section
        key_frame = ttk.LabelFrame(self.window, text="Encryption Key", padding=10)
        key_frame.pack(fill="x", padx=10, pady=5)

        self.key_text = tk.Text(key_frame, height=3)
        self.key_text.pack(side="left", fill="x", expand=True)
        
        key_btn_frame = ttk.Frame(key_frame)
        key_btn_frame.pack(side="right")
        
        ttk.Button(key_btn_frame, text="Generate New Key", command=self.generate_key).pack(pady=2)
        ttk.Button(key_btn_frame, text="Load Key File", command=self.load_key_file).pack(pady=2)

        # Output section
        output_frame = ttk.LabelFrame(self.window, text="Encrypted Output", padding=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=8)
        self.output_text.pack(fill="both", expand=True)

        output_btn_frame = ttk.Frame(output_frame)
        output_btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(output_btn_frame, text="Encrypt", command=self.encrypt_data).pack(side="left", padx=5)
        ttk.Button(output_btn_frame, text="Copy to Clipboard", command=self.copy_output).pack(side="left", padx=5)
        ttk.Button(output_btn_frame, text="Save to File", command=self.save_to_file).pack(side="left", padx=5)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_label = ttk.Label(self.window, textvariable=self.status_var)
        status_label.pack(pady=5)

    def generate_key(self):
        try:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
            self.key_text.delete(1.0, tk.END)
            self.key_text.insert(1.0, key.decode())
            self.fernet = Fernet(key)
            self.status_var.set("New key generated and saved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate key: {str(e)}")
            self.status_var.set("Failed to generate key")

    def load_key_file(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("Key files", "*.key"), ("All files", "*.*")])
            if filename:
                with open(filename, "rb") as file:
                    key = file.read()
                self.key_text.delete(1.0, tk.END)
                self.key_text.insert(1.0, key.decode())
                self.fernet = Fernet(key)
                self.status_var.set("Key loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key: {str(e)}")
            self.status_var.set("Failed to load key")

    def load_file(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if filename:
                with open(filename, "r") as file:
                    data = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(1.0, data)
                self.status_var.set("File loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
            self.status_var.set("Failed to load file")

    def paste_text(self):
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, pyperclip.paste())
        self.status_var.set("Text pasted from clipboard")

    def encrypt_data(self):
        if not self.fernet:
            messagebox.showerror("Error", "Please load or generate a key first")
            return
            
        data = self.input_text.get(1.0, tk.END).strip()
        if not data:
            messagebox.showerror("Error", "Please enter data to encrypt")
            return

        try:
            encrypted = self.fernet.encrypt(data.encode())
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, encrypted.decode())
            self.status_var.set("Data encrypted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
            self.status_var.set("Encryption failed")

    def copy_output(self):
        encrypted_data = self.output_text.get(1.0, tk.END).strip()
        if encrypted_data:
            pyperclip.copy(encrypted_data)
            self.status_var.set("Encrypted data copied to clipboard")
        else:
            messagebox.showwarning("Warning", "No encrypted data to copy")

    def save_to_file(self):
        encrypted_data = self.output_text.get(1.0, tk.END).strip()
        if not encrypted_data:
            messagebox.showwarning("Warning", "No encrypted data to save")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"encrypted_{timestamp}.txt"
        
        try:
            with open(filename, "wb") as file:
                file.write(encrypted_data.encode())
            self.status_var.set(f"Data saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
            self.status_var.set("Failed to save file")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = EncrypterGUI()
    app.run()