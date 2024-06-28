from pathlib import Path

project_root = Path(__file__).resolve().parent


def test_cv():
    file_path = project_root / 'utils' / 'test_file.jpeg'
    return file_path
