from library_system import Book, EBook, PrintBook, Library

def run_tests():
    
    b = Book("Pride and Prejudice", "Jane Austen")
    assert b.title == "Pride and Prejudice", "Book title initialization failed"
    assert b.author == "Jane Austen", "Book author initialization failed"

    e = EBook("Snow Crash", "Neal Stephenson", 500)
    assert e.title == "Snow Crash", "EBook title initialization failed"
    assert e.author == "Neal Stephenson", "EBook author initialization failed"
    assert e.file_size == 500, "EBook file_size initialization failed"

    p = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    assert p.title == "The Catcher in the Rye", "PrintBook title initialization failed"
    assert p.author == "J.D. Salinger", "PrintBook author initialization failed"
    assert p.page_count == 234, "PrintBook page_count initialization failed"

    # Test Library methods
    library = Library()
    library.add_book(b)
    library.add_book(e)
    library.add_book(p)

    # Capture output of list_books()
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    library.list_books()
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip().split("\n")

    expected_output = [
        "Book: Pride and Prejudice by Jane Austen",
        "EBook: Snow Crash by Neal Stephenson, File Size: 500KB",
        "PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234"
    ]

    assert output == expected_output, f"Output mismatch.\nExpected:\n{expected_output}\nGot:\n{output}"

    print(" All checks passed for Book, EBook, PrintBook, and Library!")

if __name__ == "__main__":
    run_tests()
