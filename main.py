import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2


class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Camera GUI")
        self.root.geometry("800x600")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2E2E2E')
        self.style.configure('TButton', font=('Helvetica', 14), background='#4CAF50', foreground='#FFFFFF')
        self.style.configure('TLabel', background='#2E2E2E', foreground='#FFFFFF', font=('Helvetica', 12))

        self.main_frame = ttk.Frame(root, style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.video_label = ttk.Label(self.main_frame)
        self.video_label.pack(pady=20)

        self.capture_button = ttk.Button(self.main_frame, text="Capture", command=self.capture_image, style='TButton')
        self.capture_button.pack(pady=20)

        self.quit_button = ttk.Button(self.main_frame, text="Quit", command=root.quit, style='TButton')
        self.quit_button.pack(pady=20)

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("captured_image.png", frame)

    def __del__(self):
        self.cap.release()


if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
