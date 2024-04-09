from main import(
    get_book_length,
    get_char_count,
    sort_on,

)

def test_get_book_length():
    assert get_book_length("The quick brown fox") == 4


def git_char_count():
    assert get_char_count("Apple banana") == {"a": 4, "p": 2, "l": 1, "e": 1, "b": 1, "n": 2}


def sort_on():
    assert sort_on({"test": 4, "num": 3}) == 3
