#!/usr/bin/env python3
import fitz  # PyMuPDF
import os
import sys

def extract_images(pdf_dir, out_dir):
    if not os.path.exists(pdf_dir):
        print(f"Error: Directory '{pdf_dir}' does not exist.")
        sys.exit(1)
        
    os.makedirs(out_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in '{pdf_dir}'.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            doc = fitz.open(pdf_path)
            print(f"Extracting images from: {pdf_file} ...")
            img_count = 0
            for i in range(len(doc)):
                for img in doc.get_page_images(i):
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    img_name = f"{os.path.splitext(pdf_file)[0]}_p{i}_xref{xref}.png"
                    img_path = os.path.join(out_dir, img_name)
                    
                    if pix.n - pix.alpha < 4:       # GRAY or RGB
                        pix.save(img_path)
                    else:                           # CMYK: convert to RGB
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        pix1.save(img_path)
                        pix1 = None
                    pix = None
                    img_count += 1
            print(f"  -> Extracted {img_count} images.")
        except Exception as e:
            print(f"Failed to process {pdf_file}: {e}")

if __name__ == "__main__":
    pdf_dir = sys.argv[1] if len(sys.argv) > 1 else "_research_pdfs"
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "_extracted_images"
    extract_images(pdf_dir, out_dir)
