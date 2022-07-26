# Explanation

## The (not tragic) Back story
The file-clerk module was initially a few functions in a script called main. It was created for a project designed to process csv files.

I found the functions to be handy enough that when I created a new project that would need to deal with files, I ported over the relevant functions into a script named clerk because it basically was my file-handling clerk.

Two more projects later, I decided that it's time to make the script a library, and every time I use it in a new project and find new ideas for processing files, I will continue to expand on this project.

## Created by a CS and Web Development teacher.
I should point out that some of the functionality was added for automating teaching tasks, which is why you may find some of my functions oddly specific. That's because I'm currently working on projects to help me assess student work: in particular, for my web design classes.

I'll highlight those in the following *Use Case section*.

## Use Case
If you want to manipulate files in a Python project, you may find this useful. Here are the main ways I use this library:

* **Grab a list of all files** - in a project folder.
* **Select just the filetypes I want** - typically, I am processing HTML, CSS, and CSV files)
* **Write contents to files** - this is handy for generating reports
* **My oddly specific tasks** for checking and processing student work, such as...
    - **Split paragraphs into sentences** - so I can check things like word count and sentences per paragraph
    - **remove inline tags from a container tag** - so I could count just words and sentences from a web document

## licensing
Don't even get me started on the complexities of how to choose a license. The bottom line is that I selected to use the MIT license for this library. I selected it for three main reasons:

1. I found that the majority of the OSS (Open Source Software) licenses out there are MIT.
2. MIT is permissive and doesn't force any of my other projects to be of the same license.
3. In my webanalyst project, the majority of the licenses were also MIT, so I decided to do the same.
