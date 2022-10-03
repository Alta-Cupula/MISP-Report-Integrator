import docx

document = docx.Document("test.docx")
text = ""
for table in document.tables:
    for row in table.rows:
        for cell in row.cells:
            text += cell.text

print(text)
