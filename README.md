# 🖼️ HEIC2PNG - Image Converter

A modern GUI tool to convert `.HEIC` images to `.PNG` or `.JPEG` with preview, batch conversion, and beautiful UI.

[![Download for Windows](https://img.shields.io/badge/⬇️%20Download-Windows%20EXE-blue?style=for-the-badge&logo=windows)](https://github.com/ElJoker1/heic2png/releases/latest/download/HEIC2PNG.exe)

---

## 💻 Download for Windows

1. Go to the [latest release](https://github.com/ElJoker1/heic2png/releases/latest)
2. Download `HEIC2PNG.exe`
3. Run directly – no installation needed!

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
- 🌐 Cross-platform (Windows, Linux, macOS)

---

## 🛠️ Run from Source

> Requires Python 3.7+

```bash
git clone https://github.com/ElJoker1/heic2png.git
cd heic2png
pip install -r requirements.txt
python3 HEIC2PNG.py
```

---

## 🧪 Build Executable

### 🔨 Windows / Linux / macOS

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --icon=icon.ico HEIC2PNG.py
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
├── icon.ico / pngegg.png   # App icon
└── dist/                   # Generated executables
```

---

## 📦 Dependencies

- [Pillow](https://pypi.org/project/Pillow/)
- [pyheif](https://pypi.org/project/pyheif/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [tkinterdnd2](https://pypi.org/project/tkinterdnd2/)
- [pyinstaller](https://pypi.org/project/pyinstaller/)

---

## 🧰 Troubleshooting

- ❌ **No HEIC images found?** → Check `.heic` extension is correct
- ❌ **Icon not loading?** → Confirm `icon.ico` is in the same folder
- ❌ **PyInstaller fails?** → Run `pip install pyinstaller` first

---

## 👨‍💻 Developer

Made with ❤️ by [Ahmed Hussein](https://www.facebook.com/Ebnhusssein)

> 💡 Got an idea or feature request? Reach out anytime.

---

## 🕊️ 🇵🇸 Palestine is free
