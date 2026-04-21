import re
import pdfplumber
from abc import ABC, abstractmethod

class DocumentParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        pass

class PDFParser(DocumentParser):
    def parse(self, file_path: str) -> str:
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            return ""
            
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
        return re.sub(r'\s+', ' ', text).strip()

class ParserEngine:
    def __init__(self):
        self._strategies = {".pdf": PDFParser()}

    def extract_text(self, file_path: str, extension: str) -> str:
        parser = self._strategies.get(extension.lower())
        if not parser:
            raise ValueError(f"Unsupported format: {extension}")
        return parser.parse(file_path)