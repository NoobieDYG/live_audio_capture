import tkinter as tk
def subtitle_display(subtitle_label):

    root=tk.Tk()
    root.title("Live subtitles")
    root.geometry("800x100")
    subtitle_label = tk.Label(root, text='',font=("Arial",24),wraplength=700)
    subtitle_label.pack()
    root.update()
    root.mainloop()