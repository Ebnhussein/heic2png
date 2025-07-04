
# HEIC2PNG - Image Converter

A modern GUI application to convert HEIC images to PNG or JPEG formats with batch processing support.

## Features

- 🔄 Convert HEIC images to PNG or JPEG formats
- 📁 Batch processing (multiple files at once)
- 🎯 Progress bar with current image preview
- 🖼️ Thumbnail preview during conversion
- 💾 Save and restore user settings
- 🔔 System notifications on completion
- 🎨 Modern UI with CustomTkinter
- 🌍 Cross-platform support (Windows, Linux, macOS)

## Installation

### Method 1: Run from source

1. Install Python 3.7 or higher
2. Install required packages:
=======
# 🖼️ HEIC2PNG - Image Converter

A modern GUI application to convert `.HEIC` images to `.PNG` or `.JPEG` with batch processing, preview, and system notifications.

[![Download for Windows](https://img.shields.io/badge/⬇️%20Download-Windows%20EXE-blue?style=for-the-badge&logo=windows)](https://github.com/ElJoker1/heic2png/releases/latest/download/HEIC2PNG.exe)

---

## ✨ Features

- 🔄 Convert HEIC to PNG or JPEG
- 🧺 Batch conversion (multi-file support)
- 🖼️ Image preview & thumbnail
- 📊 Progress bar & status updates
- 💾 Remembers last settings
- 🔔 System notification on completion
- 🎨 Beautiful modern UI using CustomTkinter
- 🧲 Drag & Drop support
- 🌍 Works on Windows / Linux / macOS

---

## 🛠️ Installation

### 📦 Method 1: Run from Source

1. Install Python 3.7 or higher
2. Install dependencies:

>>>>>>> 0cdd1d25b7f3e0f05d2453190761bed65d65e373
```bash
pip install -r requirements.txt
```


3. Run the application:
```bash
python3 heic_converter_gui.py
```

### Method 2: Create executable

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Build executable:
```bash
python3 build_exe.py
```

3. Find the executable in the `dist` folder:
   - **Windows**: `dist/HEIC2PNG.exe`
   - **Linux/Mac**: `dist/HEIC2PNG`

4. Test the executable:
```bash
python3 test_executable.py
```

## Usage

1. **Select Images**: Click "Select Images" to choose HEIC files
2. **Choose Output Folder**: Click "Output Folder" to select where to save converted images
3. **Select Format**: Choose PNG or JPEG output format
4. **Start Conversion**: Click "Start Conversion" to begin processing
5. **Monitor Progress**: Watch the progress bar and current image preview
6. **Get Notified**: System notification when conversion is complete

## File Structure

```
HEIC2PNG/
├── heic_converter_gui.py    # Main application
├── requirements.txt         # Python dependencies
├── build_exe.py            # Build script for executable
├── test_executable.py      # Test script for executable
├── pngegg.png             # Application icon
├── README.md              # This file
└── dist/                  # Generated executable (after build)
    ├── HEIC2PNG          # Linux/Mac executable
    └── HEIC2PNG.exe      # Windows executable
```

## Dependencies

- **Pillow**: Image processing
- **pyheif**: HEIC file support
- **customtkinter**: Modern UI framework
- **PyInstaller**: For creating executables

## Building for Distribution

### Windows
```bash
python build_exe.py
```

### Linux
```bash
python3 build_exe.py
```

### macOS
```bash
python3 build_exe.py
```

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Run `pip install -r requirements.txt`
2. **Icon not loading**: Ensure `pngegg.png` is in the same directory
3. **HEIC files not detected**: Make sure you have `pyheif` installed

### Build Issues

1. **PyInstaller not found**: Install with `pip install pyinstaller`
2. **Large executable**: This is normal for GUI applications with image processing libraries

## License

This project is open source and available under the MIT License.

## Developer

Developed by Ahmed Hussein
Contact: https://www.facebook.com/Ebnhusssein 
=======
3. Run:

```bash
python HEIC2PNG.py
```

---

### 💻 Method 2: Download Executable (Windows)

1. Go to the [Releases](https://github.com/ElJoker1/heic2png/releases/latest)
2. Download `HEIC2PNG.exe`
3. Run directly without installation!

---

## 🚀 Usage

1. 📤 Click **Select Images**
2. 📁 Choose **Output Folder**
3. 🖼️ Select **PNG** or **JPEG**
4. ▶️ Press **Start Conversion**
5. ⏳ Watch progress & thumbnail preview
6. 🔔 Get a system notification when done

---

## 📁 File Structure

```
HEIC2PNG/
├── HEIC2PNG.py             # Main script
├── requirements.txt        # Python dependencies
├── build_exe.py            # Optional build script
├── pngegg.png / icon.ico   # App icon
└── dist/                   # Generated executables
```

---

## 📦 Dependencies

- [`Pillow`](https://pypi.org/project/Pillow/)
- [`pyheif`](https://pypi.org/project/pyheif/)
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)
- [`tkinterdnd2`](https://pypi.org/project/tkinterdnd2/)
- [`pyinstaller`](https://pypi.org/project/pyinstaller/)

---

## 🧪 Building Executable (Optional)

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --icon=icon.ico HEIC2PNG.py
```

> Output will be in the `dist/` folder

---

## 🧰 Troubleshooting

- ❌ **No HEIC images found?** → Ensure files end with `.heic`
- ❌ **Icon not loading?** → Confirm `icon.ico` is next to the `.py` file
- ❌ **PyInstaller not working?** → Run: `pip install pyinstaller`

---

## 🧑‍💻 Developer

Made with ❤️ by [Ahmed Hussein](https://www.facebook.com/Ebnhusssein)

> For suggestions or contributions, feel free to contact me.

---

## 🕊️ Palestine is free 🇵🇸
>>>>>>> 0cdd1d25b7f3e0f05d2453190761bed65d65e373
