from pathlib import Path
from pypdf import PdfReader

p = Path(r'C:\Users\Aluno\Documents\firemap\Trabalho final.pdf')
print('exists', p.exists())
reader = PdfReader(str(p))
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
print(text[:8000])
