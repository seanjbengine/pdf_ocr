# pdf_ocr
This repository is for testing purposes: to figure out how effective Python's OCR libraries are for parsing image-based PDF files.


convert -density 300 /path/to/my/document.pdf -depth 8 -strip -background white -alpha off file.tiff

tesseract file.tiff output.txt