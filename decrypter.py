from cryptography.fernet import Fernet, InvalidToken
from datetime import datetime
import pyperclip
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class DecrypterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Decrypter")
        self.window.geometry("600x500")
        self.fernet = None
        
        self.setup_gui()

    def setup_gui(self):
        # Key input section
        key_frame = ttk.LabelFrame(self.window, text="Encryption Key", padding=10)
        key_frame.pack(fill="x", padx=10, pady=5)

        self.key_text = tk.Text(key_frame, height=3)
        self.key_text.pack(side="left", fill="x", expand=True)
        
        key_btn_frame = ttk.Frame(key_frame)
        key_btn_frame.pack(side="right")
        
        ttk.Button(key_btn_frame, text="Load Key File", command=self.load_key_file).pack(pady=2)
        ttk.Button(key_btn_frame, text="Set Key", command=self.set_key).pack(pady=2)

        # Encrypted input section
        input_frame = ttk.LabelFrame(self.window, text="Encrypted Input", padding=10)
        input_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.input_text = tk.Text(input_frame, height=8)
        self.input_text.pack(fill="both", expand=True)

        input_btn_frame = ttk.Frame(input_frame)
        input_btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(input_btn_frame, text="Load File", command=self.load_encrypted_file).pack(side="left", padx=5)
        ttk.Button(input_btn_frame, text="Paste", command=self.paste_encrypted).pack(side="left", padx=5)
        ttk.Button(input_btn_frame, text="Decrypt", command=self.decrypt_data).pack(side="left", padx=5)

        # Output section
        output_frame = ttk.LabelFrame(self.window, text="Decrypted Output", padding=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output_text = tk.Text(output_frame, height=8)
        self.output_text.pack(fill="both", expand=True)
        
        ttk.Button(output_frame, text="Copy to Clipboard", command=self.copy_output).pack(pady=5)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_label = ttk.Label(self.window, textvariable=self.status_var)
        status_label.pack(pady=5)

    def load_key_file(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("Key files", "*.key"), ("All files", "*.*")])
            if filename:
                with open(filename, "rb") as file:
                    key = file.read()
                self.key_text.delete(1.0, tk.END)
                self.key_text.insert(1.0, key.decode())
                self.status_var.set("Key file loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key file: {str(e)}")
            self.status_var.set("Failed to load key file")

    def set_key(self):
        try:
            key = self.key_text.get(1.0, tk.END).strip().encode()
            self.fernet = Fernet(key)
            self.status_var.set("Key set successfully")
        except Exception as e:
            messagebox.showerror("Error", "Invalid key format")
            self.status_var.set("Failed to set key")

    def load_encrypted_file(self):
        try:
            filename = filedialog.askopenfilename()
            if filename:
                with open(filename, "rb") as file:
                    data = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(1.0, data.decode())
                self.status_var.set("Encrypted file loaded")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
            self.status_var.set("Failed to load encrypted file")

    def paste_encrypted(self):
        text = pyperclip.paste()
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(1.0, text)
        self.status_var.set("Text pasted from clipboard")

    def decrypt_data(self):
        if not self.fernet:
            messagebox.showerror("Error", "Please set a valid key first")
            return

        try:
            encrypted_data = self.input_text.get(1.0, tk.END).strip().encode()
            decrypted_data = self.fernet.decrypt(encrypted_data)
            
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, decrypted_data.decode())
            
            self.log_action("Data decrypted successfully")
            self.status_var.set("Decryption successful")
        except InvalidToken:
            messagebox.showerror("Error", "Invalid key or corrupted data")
            self.status_var.set("Decryption failed - Invalid token")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
            self.status_var.set("Decryption failed")

    def copy_output(self):
        decrypted_text = self.output_text.get(1.0, tk.END).strip()
        if decrypted_text:
            pyperclip.copy(decrypted_text)
            self.status_var.set("Output copied to clipboard")
        else:
            self.status_var.set("No output to copy")

    def log_action(self, action):
        with open("decrypted_file.txt", "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] {action}\n")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = DecrypterGUI()
    app.run()