from docx import Document

# Function to read DOCX file and return its content as a string
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Read the content of the uploaded DOCX file
doc_content = read_docx('C:\Users\ioses\Downloads\ZABALA IA-IFIE.docx')
doc_content[:5000]  # Display the first 500 characters of the document content