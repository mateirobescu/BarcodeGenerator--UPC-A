# Barcode Generator for UPC-A

A simple Python script that generates barcodes of **UPC-A** type and saves them as PNG images.  
If you provide 11 digits, the checksum is automatically calculated. If you provide 12 digits, the script validates and uses them directly.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/mateirobescu/BarcodeGenerator--UPC-A.git
cd barcode-gen-upc-a
pip install -r requirements.txt
```

## Usage
python barcode-gen-UPC-A.py <barcode> <img_location>

- `<barcode>`:  
  An 11 or 12 digit UPC-A code.  
  - If 11 digits are provided → checksum is calculated automatically.  
  - If 12 digits are provided → the last digit is validated as the checksum.  

- `<img_location>`:  
  The folder path where the PNG will be saved.

## Example 

```bash
python barcode-gen-UPC-A.py 03600029145 ./output
```
This generates the file:
  `output/barcode-036000291452.png`

## Requirements
- numpy~=2.3.3
- matplotlib~=3.10.6
