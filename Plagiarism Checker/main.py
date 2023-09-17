import tkinter as tk
from tkinter import scrolledtext
import tkinter.messagebox as messagebox
import re
import math
from collections import Counter

# Function to calculate cosine similarity
def cosine_similarity(text1, text2):
    # Tokenize and create a set of unique words for each text
    words1 = set(re.findall(r'\w+', text1.lower()))
    words2 = set(re.findall(r'\w+', text2.lower()))

    # Calculate the term frequency (TF) for each word in both texts
    tf1 = Counter(words1)
    tf2 = Counter(words2)

    # Create a set of all unique words in both texts
    all_words = words1.union(words2)

    # Calculate the dot product of TF vectors for both texts
    dot_product = sum(tf1[word] * tf2[word] for word in all_words)

    # Calculate the magnitude of TF vectors for both texts
    magnitude1 = math.sqrt(sum(tf1[word] ** 2 for word in all_words))
    magnitude2 = math.sqrt(sum(tf2[word] ** 2 for word in all_words))

    # Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity

# Function to check plagiarism
def check_plagiarism():
    text1 = text1_entry.get("1.0", "end-1c")
    text2 = text2_entry.get("1.0", "end-1c")

    if not text1 or not text2:
        messagebox.showinfo("Plagiarism Checker", "Please enter text in both fields.")
        return

    similarity = cosine_similarity(text1, text2)
    messagebox.showinfo("Plagiarism Checker", f"Cosine Similarity: {similarity:.2f}")

# Create the main window
window = tk.Tk()
window.title("Plagiarism Checker")

# Create text entry fields
label1 = tk.Label(window, text="Text 1:")
label1.pack()
text1_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text1_entry.pack()

label2 = tk.Label(window, text="Text 2:")
label2.pack()
text2_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text2_entry.pack()

# Create the Check Plagiarism button
check_button = tk.Button(window, text="Check Plagiarism", command=check_plagiarism)
check_button.pack()

# Start the Tkinter main loop
window.mainloop()
