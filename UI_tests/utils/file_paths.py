from pathlib import Path

project_root = Path(__file__).resolve().parent

def different_cv_format():
    base_root = project_root / 'test_documents'
    file_paths = {'TXT_file': str(base_root / 'CVExample.txt'),
                  'PDF_file': str(base_root / 'CVExample.pdf'),
                  'HTML_file': str(base_root / 'CVExample.html'),
                  'DOCX_file': str(base_root / 'CVExample.docx'),
                  }
    return file_paths
