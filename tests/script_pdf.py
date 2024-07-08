import os.path

from pypdf import PdfReader

reader = PdfReader('tmp/english_for_everyone_practice_book_level_1_beginner.pdf')
print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

print(os.path.getsize('tmp/english_for_everyone_practice_book_level_1_beginner.pdf'))
assert os.path.getsize('tmp/english_for_everyone_practice_book_level_1_beginner.pdf') == 75635503
