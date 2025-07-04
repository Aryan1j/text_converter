# 📝 Text to Image, Word, and PDF Converter

This Python project converts a given text input (`input.txt`) into:

- 🖼️ A beautifully rendered **image (`output.png`)**
- 📝 A formatted **Word document (`output.docx`)**
- 📄 A clean **PDF file (`output.pdf`)**
- 💾 A simple **text output file (`output.txt`)**

## 🚀 Features

- Centered text rendering on a cream-colored background image
- Custom font and spacing
- Word document with styling
- PDF output with safe ASCII encoding
- Graceful handling of missing fonts and Unicode issues

## 📁 Input File

- Ensure your `input.txt` file exists in the same directory.
- Example:

## 🧪 How to Run

1. 🔧 **Install Dependencies**:
 ```bash
 pip install pillow python-docx fpdf
python convert_text.py
