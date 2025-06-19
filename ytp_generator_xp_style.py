import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Windows XP color palette
BG_COLOR = "#ece9d8"
BTN_COLOR = "#f1f1f1"
FG_COLOR = "#000000"
TAB_COLOR = "#ece9d8"
FONT = ("Tahoma", 9)

# All effect and style options
EFFECT_CATEGORIES = {
    "Video Effects": [
        "Demonic Effect", "G Major", "Terrifying G Major", "Horror Versions", 
        "Klasky Csupo Logo Effects", "Annoying Goose", "Up To Faster", 
        "Everything'd", "Dance Effect", "Evil Jumpscare", "Gets Grounded"
    ],
    "Audio Effects": [
        "G Major", "Terrifying G Major", "Scream Remix", "Red Zone", "Mashup", "Chaos Remix"
    ],
    "Image Effects": [
        "Logo Editing", "Preview 2", "Style Selections"
    ],
    "Styles": [
        "YTP", "YTPMV", "YTP Tennis", "Collab Entry", "Sparta Remix",
        "Crossover Scream Remix", "Gumball Remix", "Shuric Scan"
    ],
    "Media": [
        "Images", "Videos", "Audios", "Musics"
    ],
    "Other": [
        "Video Render", "Mashup", "Gets Grounded"
    ]
}

class XPStyleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YTP Generator - Windows XP")
        self.geometry("670x420")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.selected_files = {"Images": [], "Videos": [], "Audios": [], "Musics": []}

        self.create_tabs()
        self.create_file_selectors()
        self.create_render_button()

    def create_tabs(self):
        style = ttk.Style(self)
        style.theme_use('default')
        style.configure('TNotebook', background=TAB_COLOR, borderwidth=0)
        style.configure('TNotebook.Tab', background=TAB_COLOR, font=FONT, padding=[10, 2])
        style.map('TNotebook.Tab', background=[('selected', BTN_COLOR)])
        self.notebook = ttk.Notebook(self)
        self.notebook.place(x=10, y=10, width=480, height=330)

        self.tabs = {}
        for category, options in EFFECT_CATEGORIES.items():
            frame = tk.Frame(self.notebook, bg=TAB_COLOR)
            self.tabs[category] = frame
            self.notebook.add(frame, text=category)
            self.create_checkboxes(frame, options)

    def create_checkboxes(self, frame, options):
        self.vars = getattr(self, 'vars', {})
        for i, option in enumerate(options):
            var = tk.BooleanVar(value=False)
            chk = tk.Checkbutton(
                frame, text=option, variable=var, bg=TAB_COLOR, font=FONT, anchor='w'
            )
            chk.grid(row=i, column=0, sticky="w", padx=10, pady=2)
            self.vars[option] = var

    def create_file_selectors(self):
        # File selection buttons for media
        y = 350
        for i, media in enumerate(["Images", "Videos", "Audios", "Musics"]):
            btn = tk.Button(
                self, text=f"Select {media}", bg=BTN_COLOR, font=FONT,
                command=lambda m=media: self.select_files(m), width=14
            )
            btn.place(x=20 + i*160, y=y)

    def select_files(self, media_type):
        filetypes = [("All files", "*.*")]
        if media_type == "Images":
            filetypes = [("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        elif media_type == "Videos":
            filetypes = [("Video Files", "*.mp4 *.avi *.mov *.wmv *.flv *.mkv")]
        elif media_type == "Audios" or media_type == "Musics":
            filetypes = [("Audio Files", "*.mp3 *.wav *.ogg *.flac *.aac")]
        files = filedialog.askopenfilenames(title=f"Select {media_type}", filetypes=filetypes)
        if files:
            self.selected_files[media_type] = files
            messagebox.showinfo("Files Selected", f"{len(files)} {media_type} selected.")

    def create_render_button(self):
        render_btn = tk.Button(
            self, text="Render Video", bg="#5a8fd6", fg="#fff", font=FONT, width=20, height=2,
            command=self.render_video
        )
        render_btn.place(x=500, y=130)

    def render_video(self):
        selected_effects = [k for k, v in self.vars.items() if v.get()]
        selected_media = {k: v for k, v in self.selected_files.items() if v}
        summary = (
            f"You selected the following effects:\n{selected_effects}\n\n"
            f"Selected media:\n{selected_media}\n\n"
            "Rendering functionality is not implemented in this demo script.\n"
            "Integrate with FFmpeg or similar tools for actual rendering."
        )
        messagebox.showinfo("Render Summary", summary)

if __name__ == "__main__":
    app = XPStyleApp()
    app.mainloop()