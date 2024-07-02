import pdfplumber


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
            print(page.extract_text())
    return text


def save_text_to_txt(text, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


def main():
    pdf_path = 'NIST.SP.800-53r5.pdf'
    txt_path = 'extracted_text.txt'

    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_txt(extracted_text, txt_path)

    print(f"Extracted text saved to {txt_path}")


if __name__ == '__main__':
    main()
