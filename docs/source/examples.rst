Examples
========

Installation (Quick Start):
***************************
To begin using `file-clerk` in your Python project, you may install with:
:code:`pip install file-clerk`

Getting Started
***************

.. code-block:: python

    import file_clerk.clerk as clerk

    # get the path to your project files (you want to manipulate)
    # use posix path format (forward slashes)
    project_path = "path/to/project"

    # get all files as strings from project folder
    all_project_files = clerk.get_all_project_files(project_path)

    # get only the HTML files
    html_only_files = clerk.get_all_files_of_type(project_path, "html")

    # get extension to file (without the dot)
    file_extension = get_file_type("path/to/file.ext")

    # extract a list of sentences from a paragraph:
    paragraph = "No, I'll fix it. I'm good at fixing rot. Call me the Rotmeister. "
    paragraph += "No, I'm the Doctor. Don't call me the Rotmeister."
    sentences = clerk.split_into_sentences(paragraph)
    number_sentences = len(sentences) # equals 5

    # Make sure a file exists - helps to avoid file not found errors
    exists = clerk.file_exists(possible_file_path)

    # Get the contents of a file as a string (but only if it exists)
    if exists:
        file_contents = clerk.file_to_string(possible_file_path)