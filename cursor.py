import tkinter as tk

root = tk.Tk()
root.title("Cursor Demo")
root.geometry("400x300")

# label with different cursor
label1 = tk.Label(root, text="Arrow Cursor", cursor="arrow")
label1.pack(pady=10)

label2 = tk.Label(root, text="Hand Cursor", cursor="hand2")
label2.pack(pady=10)

label3 = tk.Label(root, text="Text Cursor", cursor="xterm")
label3.pack(pady=10)

label4 = tk.Label(root, text="Loading Cursor", cursor="watch")
label4.pack(pady=10)

label5 = tk.Label(root, text="Cross Cursor", cursor="cross")
label5.pack(pady=10)

root.mainloop()
