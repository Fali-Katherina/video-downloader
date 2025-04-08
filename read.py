
from docx import Document

# Open the .docx file
doc = Document("Hello world.docx")

# Iterate through paragraphs and print their text
for para in doc.paragraphs:
    print(para.text)

#OR

with open('Hello.txt', 'r')as file:
    content = file.read()
    print(content)