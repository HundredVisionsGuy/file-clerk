import pytest

from file_clerk import __version__
from file_clerk import clerk as clerk


def test_version():
    assert __version__ == "1.0.5"


# TODO - separate tests based on command-line flag
css_file_path = "tests/test_files/projects/large_project/test.css"
html_file_path = "tests/test_files/sample.html"
html_with_css = "tests/test_files/html_with_css.html"
sample_txt_path = "tests/test_files/sample.txt"
working_dir_txt_path = "README.rst"


@pytest.fixture
def test_code_one():
    test_code = """<!DOCTYPE html>\n<html lang="en">\n\n<head>
    <link rel="stylesheet" href="styles.css">    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>\n
    <style>\n        body {
                    color: #121212 background-fred: #f1f1f1;
                            }\n    </style>
    </head>\n\n<h1>About Me<h1>\n
    <h2>Background</h2>\n
    <p>I was born a young child in Phoenix, Arizona.
    I was the last of five children, but I had a good childhood.</p>
    <h2>Hobbies</h2>
    <p>I love to play <strong>guitar and code. I have both an electric
    and acoustic guitar, but I prefer my acoustic.</p>
    </html>"""
    return test_code


@pytest.fixture
def test_code_two():
    test_code = """<!DOCTYPE html>\n<html lang="en">\n\n<head>
    <link rel="stylesheet" href="styles.css">    <meta charset="UTF-8">
    <link rel="stylesheet" href="mystyles.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>\n
    <style>\n        body {
                    color: #121212 background-fred: #f1f1f1;
                            }\n    </style>
    </head>\n\n<h1>About Me<h1>\n
    <h2>Background</h2>\n
    <p>I was born a young child in Phoenix, Arizona.
    I was the last of five children, but I had a good childhood.</p>
    <h2>Hobbies</h2>
    <p>I love to play <strong>guitar and code. I have both an electric
    and acoustic guitar, but I prefer my acoustic.</p>
    </html>"""
    return test_code


def test_clerk_for_file_exists_for_working_dir_txt_path():
    results = clerk.file_exists(working_dir_txt_path)
    expected = True
    assert results == expected


def test_get_file_type_for_html():
    filetype = clerk.get_file_type(html_file_path)
    assert filetype == "html"


def test_get_file_type_for_css():
    filetype = clerk.get_file_type(css_file_path)
    assert filetype == "css"


def test_file_to_string_with_sample():
    sample_test = clerk.file_to_string(sample_txt_path)
    expected = "Hey!\n"
    assert sample_test == expected


def test_file_to_string_in_working_directory():
    sample_text = clerk.file_to_string(working_dir_txt_path)
    sample_text = sample_text[:10]
    expected = "file-clerk"
    assert sample_text == expected


def test_file_to_string_in_project_directory():
    html_text = clerk.file_to_string(html_file_path)
    expected = "<!DOCTYPE html>"
    assert expected in html_text[:15]


def test_get_all_project_files_from_large_project():
    expected = [
        "tests/test_files/large_project/about.html",
        "tests/test_files/large_project/gallery.html",
        "tests/test_files/large_project/index.html",
        "tests/test_files/large_project/css/general.css",
        "tests/test_files/large_project/css/grid-layout.css",
        "tests/test_files/large_project/css/layout.css",
        "tests/test_files/large_project/css/navigation.css",
        "tests/test_files/large_project/js/scripts.js",
    ]
    results = clerk.get_all_project_files("tests/test_files/large_project")
    assert expected == results


def test_get_all_html_project_files_from_large_project():
    expected = [
        "tests/test_files/large_project/about.html",
        "tests/test_files/large_project/gallery.html",
        "tests/test_files/large_project/index.html",
    ]
    results = clerk.get_all_files_of_type("tests/test_files/large_project", "html")
    assert expected == results


def test_split_into_sentences():
    paragraph = "Hello, you! How are you? i am fine Mr. selenium.\nsee ya later."
    results = len(clerk.split_into_sentences(paragraph))
    expected = 4
    assert results == expected


def test_remove_inline_tags():
    paragraph = (
        '<p>Site designed by <a href="mailto:guy@hundredvisions.com">'
        "Hundred visions Guy</a> &copy; 2019.</p>"
    )
    results = clerk.remove_tags(paragraph)
    expected = "Site designed by Hundred visions Guy &copy; 2019."
    assert results == expected


def test_get_file_name_for_html_filename():
    results = clerk.get_file_name(html_file_path)
    expected = "sample.html"
    assert results == expected


def test_get_file_name_for_css_filename():
    results = clerk.get_file_name(css_file_path)
    expected = "test.css"
    assert results == expected


def test_clear_extra_text():
    sample = "\n             body has something       in here.    "
    expected = "body has something in here."
    results = clerk.clear_extra_text(sample)
    assert results == expected


def test_get_linked_css_for_one_filename(test_code_one):
    results = clerk.get_linked_css(test_code_one)
    assert "styles.css" in results


def test_get_linked_css_for_two_filenames(test_code_two):
    results = clerk.get_linked_css(test_code_two)
    assert "mystyles.css" in results and "styles.css" in results


def test_write_csv_file():
    file_contents = []
    header = ["Name", "Age", "Occupation"]
    file_contents.append(header)
    contents = [
        ["Godfrey Osterbald", "37", "Front-end Developer"],
        ["Naomi Dorrit", "28", "Mercenary"],
        ["Tom Foolery", "42", "Sales Rep"],
        ["Shannon Rutherford", "23", "Dance Instructor"],
    ]
    file_contents += contents
    path = "tests/test_files/test_csv.csv"
    clerk.write_csv_file(path, file_contents)
    assert clerk.file_exists(path)

    # delete file
    clerk.delete_file(path)

    # file should not exist
    assert not clerk.file_exists(path)
