from single_responsibility.Exercise_1.classes.book import Book
from single_responsibility.Exercise_1.classes.save_to_file import SaveToFile

if __name__ == "__main__":
    book = Book("le petit prince","Antoine De Saint Exupery","Quand on veut un mouton c'est la preuve qu'on existe")
    SaveToFile.save_txt(book.content)
