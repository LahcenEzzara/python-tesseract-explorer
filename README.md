# Python Tesseract Explorer

This repository demonstrates the use of Tesseract OCR in Python for text extraction from various image formats. It processes multiple images and extracts their textual content using the `pytesseract` library.

## Features

- Extract text from multiple image formats such as `.png`, `.jpg`, `.bmp`, `.gif`, `.webp`, and more.
- Supports language-based OCR, including Arabic and other languages installed in Tesseract.
- Organized directory structure for managing images and code.

---

## Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/LahcenEzzara/python-tesseract-explorer.git
cd python-tesseract-explorer
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

Ensure Tesseract OCR is installed on your system. For Ubuntu, you can use:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

### 5. Install Additional Language Support

To process Arabic or other languages, install their respective Tesseract language data. For example:

```bash
sudo apt install tesseract-ocr-ara
```

---

## Usage

The main script processes images in the `images/` folder and extracts text from each. To run the script:

```bash
python main.py
```

The extracted text for each image will be printed in the terminal.

---

## Directory Structure

```
python-tesseract-explorer/
├── images/                 # Folder containing test images
│   ├── test_ar.png
│   ├── test_la.png
│   ├── test-european.jpg
│   ├── test-small.jpg
│   ├── test.bmp
│   ├── test.gif
│   ├── test.jpg
│   ├── test.png
│   ├── test.webp
│   └── ...
├── main.py                 # Python script for OCR
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── LICENSE                 # License file
```

---

## Example Output

When running the script, you will see output similar to this:

```
Processing: images/test_ar.png
Extracted Text from test_ar.png:
السلام عليكم

----------------------------------------
Processing: images/test_la.png
Extracted Text from test_la.png:
Hello World!

----------------------------------------
...
```

---

## Dependencies

- **Python 3.8+**
- **Tesseract OCR**
- **Pytesseract**: Python wrapper for Tesseract OCR
- **Pillow**: Python Imaging Library for image processing

Install them using:

```bash
pip install pytesseract pillow
```

---

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes

- Make sure your `tesseract` binary is properly installed and accessible from the command line.
- If a language is missing, download the `.traineddata` file from the [Tesseract tessdata repository](https://github.com/tesseract-ocr/tessdata) and place it in your Tesseract `tessdata` folder.
