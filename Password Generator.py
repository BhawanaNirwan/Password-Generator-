import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to calculate password strength
def calculate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    return strength

# Function to generate password
def generate_password():
    try:
        # Get user input for password length and complexity
        password_length = int(entry_length.get())
        use_uppercase = var_uppercase.get()
        use_numbers = var_numbers.get()
        use_special = var_special.get()
        exclude_similar = var_exclude_similar.get()

        # Validate password length
        if password_length < 8:
            messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return

        # Define the character sets
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        if exclude_similar:
            # Remove characters that look similar to avoid confusion (e.g., 'O' and '0', 'I' and '1')
            characters = characters.translate(str.maketrans('', '', 'O0Il1'))

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(password_length))

        # Update password label and strength meter
        label_result.config(text="Generated Password: " + password)
        strength = calculate_strength(password)
        update_strength_meter(strength)

        # Store password for clipboard functionality
        global generated_password
        generated_password = password

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number for password length.")

# Function to update the password strength meter
def update_strength_meter(strength):
    if strength == 0:
        strength_label.config(text="Weak", bg="red")
        strength_meter.config(value=0)
    elif strength == 1:
        strength_label.config(text="Fair", bg="yellow")
        strength_meter.config(value=25)
    elif strength == 2:
        strength_label.config(text="Good", bg="orange")
        strength_meter.config(value=50)
    elif strength == 3:
        strength_label.config(text="Strong", bg="green")
        strength_meter.config(value=75)
    elif strength == 4:
        strength_label.config(text="Very Strong", bg="darkgreen")
        strength_meter.config(value=100)

# Function to copy password to clipboard
def copy_to_clipboard():
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password generated yet!")

# Function to clear fields
def clear_fields():
    entry_length.delete(0, tk.END)
    entry_length.insert(0, "12")
    var_uppercase.set(False)
    var_numbers.set(False)
    var_special.set(False)
    var_exclude_similar.set(False)
    label_result.config(text="Generated Password: ")
    strength_label.config(text="Weak", bg="red")
    strength_meter.config(value=0)

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x600")
root.config(bg="#f4f4f9")

# Initialize the generated password variable
generated_password = ""

# Password length input
label_length = tk.Label(root, text="Password Length:", bg="#f4f4f9", font=("Arial", 12))
label_length.pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.insert(0, "12")  # Default length
entry_length.pack(pady=5)

# Checkbox for uppercase letters
var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg="#f4f4f9")
check_uppercase.pack(pady=5)

# Checkbox for numbers
var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#f4f4f9")
check_numbers.pack(pady=5)

# Checkbox for special characters
var_special = tk.BooleanVar()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg="#f4f4f9")
check_special.pack(pady=5)

# Checkbox to exclude similar characters
var_exclude_similar = tk.BooleanVar()
check_exclude_similar = tk.Checkbutton(root, text="Exclude Similar Characters (e.g., O, 0, I, 1)", variable=var_exclude_similar, bg="#f4f4f9")
check_exclude_similar.pack(pady=5)

# Button to generate password
btn_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="lightblue", width=20)
btn_generate.pack(pady=15)

# Label to display generated password
label_result = tk.Label(root, text="Generated Password: ", font=("Arial", 14), bg="#f4f4f9")
label_result.pack(pady=10)

# Password strength meter
strength_label = tk.Label(root, text="Weak", font=("Arial", 12), bg="red", width=15, anchor="w")
strength_label.pack(pady=5)
strength_meter = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, showvalue=False)
strength_meter.pack(pady=5)

# Button to copy password to clipboard
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="lightgreen", width=20)
btn_copy.pack(pady=15)

# Button to clear all fields
btn_clear = tk.Button(root, text="Clear Fields", command=clear_fields, font=("Arial", 12), bg="lightcoral", width=20)
btn_clear.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
