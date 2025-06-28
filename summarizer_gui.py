# summarizer_gui.py

import tkinter as tk
from tkinter import scrolledtext, messagebox
from summarizer_backend import extractive_summarizer  # Make sure this file is in the same folder

def summarize_text():
    input_text = input_box.get("1.0", tk.END).strip()
    try:
        num = int(sentence_entry.get())
    except:
        messagebox.showerror("Input Error", "Please enter a valid number of sentences.")
        return

    if not input_text:
        messagebox.showwarning("No Text", "Please paste or type some text to summarize.")
        return

    summary = extractive_summarizer(input_text, num)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary)


# --- GUI Setup ---
root = tk.Tk()
root.title("Text Summarization Tool")
root.geometry("800x600")

# --- Input Text Box ---
tk.Label(root, text="Paste your article text below:", font=("Arial", 12)).pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=15, font=("Arial", 10))
input_box.pack(padx=10, pady=5)

# --- Summary Controls ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Number of sentences in summary:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
sentence_entry = tk.Entry(control_frame, width=5)
sentence_entry.insert(0, "3")
sentence_entry.pack(side=tk.LEFT, padx=5)

tk.Button(control_frame, text="Summarize", command=summarize_text, bg="blue", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)

# --- Output Box ---
tk.Label(root, text="Generated Summary:", font=("Arial", 12)).pack(pady=5)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=10, font=("Arial", 10), fg="black")
output_box.pack(padx=10, pady=5)

# --- Run App ---
root.mainloop()