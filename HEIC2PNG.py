import os
import pyheif
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor
import platform
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), 'settings.json')
MEDIA_DIR = os.path.expanduser('~/Desktop')

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Settings load error: {e}")
    return {}

def save_settings(settings):
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f)
    except Exception as e:
        print(f"Settings save error: {e}")

def convert_single_image(heic_path, output_folder, out_format, jpeg_quality=90):
    filename = os.path.basename(heic_path)
    base_name = os.path.splitext(filename)[0]
    ext = out_format.lower()
    out_name = base_name + (".jpg" if ext == "jpeg" else ".png")
    out_path = os.path.join(output_folder, out_name)
    try:
        heif_file = pyheif.read(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode
        )
        if ext == "jpeg":
            image = image.convert("RGB")
            image.save(out_path, "JPEG", quality=jpeg_quality)
        else:
            image.save(out_path, "PNG", compress_level=0)
        return f"✅ {filename} → {out_name}"
    except Exception as e:
        return f"❌ {filename} failed: {str(e)}"

def collect_heic_files(paths):
    heic_files = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                heic_files.extend([
                    os.path.join(root, f)
                    for f in files
                    if f.lower().endswith('.heic')
                ])
        elif os.path.isfile(path) and path.lower().endswith('.heic'):
            heic_files.append(path)
    return heic_files

class HEICConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC2PNG")
        self.root.geometry("800x550")
        self.root.resizable(False, False)
        
        # Set application icon
        try:
            from PIL import Image
            icon_path = os.path.join(os.path.dirname(__file__), "pngegg.png")
            if os.path.exists(icon_path):
                icon_image = Image.open(icon_path)
                icon_image = icon_image.convert("RGBA")
                tk_icon = ImageTk.PhotoImage(icon_image)
                self.root.iconphoto(True, tk_icon)
        except Exception as e:
            print(f"Icon load failed: {e}")
        self.selected_paths = []
        self.output_folder = ""
        self.heic_files = []
        self.settings = load_settings()
        self.out_format = ctk.StringVar(value=self.settings.get('last_format', 'PNG'))
        self.progress = ctk.DoubleVar(value=0)
        self.create_widgets()

    def save_format_setting(self):
        self.settings['last_format'] = self.out_format.get()
        save_settings(self.settings)

    def create_widgets(self):
        frame = ctk.CTkFrame(self.root, corner_radius=10)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="Select HEIC images (multiple selection supported)", font=("Arial", 16))
        label.pack(pady=10)

        btn_frame = ctk.CTkFrame(frame)
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Select Images", command=self.select_files).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Output Folder", command=self.select_output_folder).pack(side="left", padx=10)

        tip_label = ctk.CTkLabel(frame, text="Tip: To select all images in a folder, open the folder and press Ctrl+A.", text_color="gray")
        tip_label.pack()

        format_frame = ctk.CTkFrame(frame)
        format_frame.pack(pady=10)
        ctk.CTkLabel(format_frame, text="Select format:").pack(side="left", padx=5)
        ctk.CTkRadioButton(format_frame, text="PNG", variable=self.out_format, value="PNG", command=self.save_format_setting).pack(side="left")
        ctk.CTkRadioButton(format_frame, text="JPEG", variable=self.out_format, value="JPEG", command=self.save_format_setting).pack(side="left")

        progress_frame = ctk.CTkFrame(frame)
        progress_frame.pack(pady=15, fill="x")
        self.progressbar = ctk.CTkProgressBar(progress_frame)
        self.progressbar.set(0)
        self.progressbar.pack(fill="x", padx=20, pady=5)
        self.progress_label = ctk.CTkLabel(progress_frame, text="0/0")
        self.progress_label.pack()
        self.current_image_label = ctk.CTkLabel(progress_frame, text="")
        self.current_image_label.pack(pady=2)
        self.thumbnail_label = ctk.CTkLabel(progress_frame, text="", width=120, height=120)
        self.thumbnail_label.pack(pady=2)
        self.thumbnail_imgtk = None

        self.status_label = ctk.CTkLabel(frame, text="")
        self.status_label.pack(pady=5)

        button_row = ctk.CTkFrame(frame)
        button_row.pack(pady=10)
        ctk.CTkButton(button_row, text="Start Conversion", command=self.start_conversion, width=150).pack(side="left", padx=10)
        ctk.CTkButton(button_row, text="Cancel", command=self.cancel_conversion, width=150).pack(side="left", padx=10)
        ctk.CTkButton(button_row, text="Open Output Folder", command=self.open_output_folder, width=180).pack(side="left", padx=10)
        ctk.CTkButton(button_row, text="About", command=self.show_about, width=120).pack(side="left", padx=10)

    def select_files(self):
        filetypes = [("HEIC images", "*.heic *.HEIC *.HeIc *.hEiC *.HEic *.heiC"), ("All files", "*.*")]
        initialdir = self.settings.get('last_input_folder', MEDIA_DIR)
        paths = filedialog.askopenfilenames(title="Select HEIC images", filetypes=filetypes, initialdir=initialdir)
        if not paths:
            return
        self.selected_paths = list(paths)
        self.heic_files = collect_heic_files(self.selected_paths)
        count = len(self.heic_files)
        if not self.heic_files:
            self.status_label.configure(text="No HEIC images found in selection.")
        else:
            self.status_label.configure(text=f"Found {count} HEIC image(s)")
        if self.selected_paths:
            self.settings['last_input_folder'] = os.path.dirname(self.selected_paths[0])
            save_settings(self.settings)

    def select_output_folder(self):
        initialdir = self.settings.get('last_output_folder', MEDIA_DIR)
        folder = filedialog.askdirectory(title="Select output folder", initialdir=initialdir)
        if folder:
            self.output_folder = folder
            self.status_label.configure(text=f"Output folder: {folder}")
            self.settings['last_output_folder'] = folder
            save_settings(self.settings)

    def open_output_folder(self):
        if self.output_folder and os.path.exists(self.output_folder):
            try:
                if platform.system() == "Windows":
                    os.startfile(self.output_folder)
                elif platform.system() == "Darwin":
                    os.system(f'open "{self.output_folder}"')
                else:
                    os.system(f'xdg-open "{self.output_folder}"')
            except Exception as e:
                messagebox.showerror("Error", f"Could not open folder:\n{e}")

    def cancel_conversion(self):
        self.cancel_requested = True
        self.status_label.configure(text="Cancelling...")
        self.root.after(300, self.reset_ui)

    def reset_ui(self):
        self.progress.set(0)
        self.progressbar.set(0)
        self.progress_label.configure(text="0/0")
        self.current_image_label.configure(text="")
        self.thumbnail_label.configure(image=None, text="")
        self.status_label.configure(text="")
        self.heic_files = []
        self.selected_paths = []

    def start_conversion(self):
        if not self.heic_files:
            messagebox.showwarning("Warning", "Please select HEIC files first.")
            return
        if not self.output_folder:
            messagebox.showwarning("Warning", "Please select output folder.")
            return
        self.progress.set(0)
        self.progressbar.set(0)
        self.status_label.configure(text=f"Starting conversion for {len(self.heic_files)} image(s)...")
        self.cancel_requested = False
        self.root.after(100, self.convert_images_threaded)

    def update_thumbnail(self, image_path):
        try:
            heif_file = pyheif.read(image_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode
            )
            image.thumbnail((120, 120))
            self.thumbnail_imgtk = ImageTk.PhotoImage(image)
            self.thumbnail_label.configure(image=self.thumbnail_imgtk, text="")
        except Exception:
            self.thumbnail_label.configure(image=None, text="No preview")

    def clear_thumbnail(self):
        self.thumbnail_label.configure(image=None, text="")
        self.thumbnail_imgtk = None

    def convert_images_threaded(self):
        results = []
        total = len(self.heic_files)
        out_format = self.out_format.get()
        jpeg_quality = 100

        def worker():
            for i, f in enumerate(self.heic_files):
                if self.cancel_requested:
                    break
                res = convert_single_image(f, self.output_folder, out_format, jpeg_quality)
                self.progress.set((i + 1) / total)
                self.progressbar.set((i + 1) / total)
                self.progress_label.configure(text=f"{i + 1}/{total} ({total - i - 1} left)")
                self.current_image_label.configure(text=os.path.basename(f))
                self.status_label.configure(text=f"Processing {i + 1} of {total}: {os.path.basename(f)}")
                self.update_thumbnail(f)
                results.append(res)
                self.root.update_idletasks()

            if self.cancel_requested:
                self.root.after(0, self.status_label.configure, {"text": "Conversion cancelled!"})
                self.root.after(0, messagebox.showinfo, "Cancelled", "Conversion was cancelled.")
                self.root.after(0, self.reset_ui)
            else:
                self.root.after(0, self.show_results, results)

            self.root.after(0, self.current_image_label.configure, {"text": ""})
            self.root.after(0, self.clear_thumbnail)
            self.root.after(0, self.progress_label.configure, {"text": "0/0"})

        import threading
        threading.Thread(target=worker, daemon=True).start()

    def show_about(self):
        import webbrowser
        about_window = ctk.CTkToplevel(self.root)
        about_window.title("About HEIC2PNG")
        about_window.geometry("450x350")
        about_window.resizable(False, False)

        text = """HEIC2PNG - Image Converter

🔹 Convert .HEIC images to PNG or JPEG formats.

🔹 Supports batch processing (multiple files at once).

🔹 Shows progress bar, current image name, and thumbnail.

🔹 Works cross-platform (Windows, Linux, macOS).

🔹 Output images are saved with high quality.

💡 Developed by:"""

        label = ctk.CTkLabel(about_window, text=text, justify="left", wraplength=400)
        label.pack(pady=10, padx=20)

        fb_link = ctk.CTkLabel(about_window, text="Ahmed Hussein (Contact)", text_color="blue", cursor="hand2")
        fb_link.pack()
        fb_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.facebook.com/Ebnhusssein"))

        close_btn = ctk.CTkButton(about_window, text="Close", command=about_window.destroy)
        close_btn.pack(pady=15)

    def show_results(self, results):
        self.status_label.configure(text="Conversion complete!")
        try:
            if platform.system() == "Windows":
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("HEIC2PNG", "Conversion complete!", duration=5)
            elif platform.system() == "Linux":
                os.system('notify-send "HEIC2PNG" "Conversion complete!"')
                os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
        except Exception as e:
            print(f"Notification error: {e}")
        messagebox.showinfo("Conversion Results", "\n".join(results))
        self.progress.set(0)
        self.progressbar.set(0)
        self.heic_files = []
        self.clear_thumbnail()

if __name__ == "__main__":
    app = ctk.CTk()
    HEICConverterApp(app)
    app.mainloop()

