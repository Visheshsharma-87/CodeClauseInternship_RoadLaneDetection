import tkinter as tk
from tkinter import filedialog, messagebox
import os
from video_processor import process_video

def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        input_path.set(file_path)

def start_detection():
    input_file = input_path.get()
    output_file = "output/result_output.avi"

    if not os.path.exists(input_file):
        messagebox.showerror("Error", "Input video file not found.")
        return

    success = process_video(input_file, output_file)

    if success:
        messagebox.showinfo("Success", f"Lane Detection Completed!\nSaved to:\n{output_file}")
    else:
        messagebox.showerror("Error", "Lane Detection Failed.")

# GUI Setup
root = tk.Tk()
root.title("🚗 Road Lane Detection System")
root.geometry("520x230")
root.resizable(False, False)

input_path = tk.StringVar()

tk.Label(root, text="Select Road Video for Lane Detection", font=("Arial", 13)).pack(pady=10)
tk.Entry(root, textvariable=input_path, width=55).pack()
tk.Button(root, text="Browse", command=select_video, width=20).pack(pady=5)
tk.Button(root, text="Start Lane Detection", command=start_detection, bg="green", fg="white", width=25, height=2).pack(pady=10)

tk.Label(root, text="Developed by Vishesh Sharma", font=("Arial", 9), fg="gray").pack(side="bottom", pady=5)

root.mainloop()
