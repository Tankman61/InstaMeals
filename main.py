import customtkinter as ctk
from tkinter import Menu, messagebox
import cv2
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")  # Set the theme to dark mode
ctk.set_default_color_theme("blue")  # Set the color theme


class InstaMealsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("InstaMeals")
        self.geometry("1920x1080")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_menus()
        self.create_main_frame()

        self.camera_frame = None
        self.cap = None

    def create_menus(self):
        menu_bar = Menu(self)

        # About menu directly opens the about page
        menu_bar.add_command(label="About", command=self.show_about)
        menu_bar.add_command(label="Generate", command=self.take_picture)


        self.config(menu=menu_bar)

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self.main_frame, text="InstaMeals", font=("Roboto", 28, "bold"))
        self.title_label.grid(row=0, column=0, pady=(0, 20))

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.grid(row=1, column=0, sticky="nsew")

        self.show_welcome_message()

    def show_welcome_message(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        welcome_label = ctk.CTkLabel(self.content_frame,
                                     text="Welcome to InstaMeals!\nTake a picture of your ingredients to get started.",
                                     font=("Roboto", 16))
        welcome_label.pack(expand=True)

    def show_about(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        about_frame = ctk.CTkFrame(self.content_frame)
        about_frame.pack(fill="both", expand=True, padx=20, pady=20)

        about_title = ctk.CTkLabel(about_frame, text="About InstaMeals", font=("Roboto", 24, "bold"))
        about_title.pack(pady=(0, 20))

        about_text = """InstaMeals is a revolutionary app that helps you create delicious meals based on the ingredients you have.

Key Features:
- Ingredient recognition
- Recipe generation
- Meal planning assistance
- Cuisine style suggestions

Version: 1.0
© 2024 InstaMeals Inc."""

        about_label = ctk.CTkLabel(about_frame, text=about_text, font=("Roboto", 14), justify="left")
        about_label.pack(pady=10)

        ok_button = ctk.CTkButton(about_frame, text="Back", command=self.show_welcome_message)
        ok_button.pack(pady=(20, 0))

    def take_picture(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Camera Error",
                                     "Unable to access the camera. Please check your camera connection.")
                return

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if self.camera_frame is None:
            self.camera_frame = ctk.CTkLabel(self.content_frame, text="")
            self.camera_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.update_camera()

        capture_button = ctk.CTkButton(self.content_frame, text="Capture", command=self.capture_image)
        capture_button.pack(pady=(0, 20))

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            img = img.resize((800, 600), Image.LANCZOS)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_frame.imgtk = imgtk
            self.camera_frame.configure(image=imgtk)
            self.after(10, self.update_camera)

    def capture_image(self):
        # Here you would add code to capture and process the image
        messagebox.showinfo("Image Captured", "Image captured successfully! Processing...")
        # Add your image processing and meal suggestion logic here

    def on_closing(self):
        if self.cap is not None:
            self.cap.release()
        self.destroy()


if __name__ == "__main__":
    app = InstaMealsApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
