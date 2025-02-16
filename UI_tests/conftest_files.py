from pathlib import Path

import pytest

project_root = Path(__file__).resolve().parent


@pytest.fixture
def test_cv_path():
    file_path = project_root / 'utils' / 'test_documents' / 'CVExample.pdf'
    return file_path
