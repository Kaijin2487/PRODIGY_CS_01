# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.


import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if encrypt else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def process_text():
    text = message_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return

    if encrypt_var.get() == 1:
        result = caesar_cipher(text, shift, encrypt=True)
    else:
        result = caesar_cipher(text, shift, encrypt=False)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Encryptor/Decryptor")

# Text input
tk.Label(root, text="Enter your message:").pack()
message_entry = tk.Text(root, height=5, width=50)
message_entry.pack()

# Shift input
tk.Label(root, text="Enter shift value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Encrypt/Decrypt option
encrypt_var = tk.IntVar(value=1)
tk.Radiobutton(root, text="Encrypt", variable=encrypt_var, value=1).pack()
tk.Radiobutton(root, text="Decrypt", variable=encrypt_var, value=0).pack()

# Action button
tk.Button(root, text="Process", command=process_text).pack(pady=10)

# Result display
tk.Label(root, text="Result:").pack()
result_text = tk.Text(root, height=5, width=50)
result_text.pack()

root.mainloop()
