# 🖼️ HEIC2PNG - Image Converter

A modern GUI tool to convert `.HEIC` images to `.PNG` or `.JPEG` with preview, batch conversion, and beautiful UI.

[![Download for Windows](https://img.shields.io/badge/⬇️%20Download-Windows%20EXE-blue?style=for-the-badge&logo=windows)](https://github.com/Ebnhussein/heic2png/releases/latest/download/HEIC2PNG.exe)

---

## 💻 Download for Windows

1. Go to the [latest release](https://github.com/Ebnhussein/heic2png/releases/latest)
2. Download `HEIC2PNG.exe`
3. Run directly – no installation needed!

> ⚠️ You may see a Windows warning since the app is unsigned. Just click “Run Anyway”.

---

## ✨ Features

- 🔄 Convert HEIC → PNG or JPEG
- 📂 Batch conversion (multiple files)
- 🖼️ Preview with thumbnail
- 📊 Progress bar & image tracking
- 💾 Saves last used settings
- 🔔 System notifications
- 🎨 CustomTkinter-based modern UI
- 🧲 Drag & Drop support
- 🌐 Works on Windows / Linux / macOS

---

## 🛠️ Run from Source

> Requires Python 3.7+

```bash
git clone https://github.com/Ebnhussein/heic2png.git
cd heic2png
pip install -r requirements.txt
python3 HEIC2PNG.py
```

---

## 🧪 Build Executable (Nuitka)

### 🔨 Windows / Linux / macOS

```bash
pip install -r requirements.txt
pip install -U nuitka
nuitka --onefile --windows-icon-from-ico=icon.ico HEIC2PNG.py

```

✅ Output file will be in the `dist/` folder

---

## 🚀 How to Use

1. 🖱️ Click **Select Images**
2. 📁 Choose **Output Folder**
3. 🎯 Choose format (PNG or JPEG)
4. ▶️ Click **Start Conversion**
5. 🔍 Watch preview & progress
6. 🔔 Get notified when done

---

## 📁 File Structure

```
HEIC2PNG/
├── HEIC2PNG.py             # Main app script
├── requirements.txt        # Dependencies
├── icon.ico                # App icon
└── README.md               # Documentation
```

---

## 📦 Dependencies

- [Pillow](https://pypi.org/project/Pillow/)
- [pyheif](https://pypi.org/project/pyheif/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [tkinterdnd2](https://pypi.org/project/tkinterdnd2/)
- [nuitka](https://pypi.org/project/nuitka/)

---

## 🧰 Troubleshooting

- ❌ No HEIC images found? → Make sure the file extensions are .heic
- ❌ Icon not loading? → Confirm icon.ico is in the same directory
- ❌ Build fails with Nuitka? → Ensure Python is 3.10+ and all dependencies are installed



---

## 👨‍💻 Developer

Made with ❤️ by [Ahmed Hussein](https://www.facebook.com/Ebnhusssein)

> 💡 Got an idea or feature request? Reach out anytime.

---

## 🕊️ 🇵🇸 Palestine is free
