#

### file_exists
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L35">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.file_exists(
   file_path: str
)
```

---
Returns True or False: whether file in path exists.


**Args**

* **file_path** (str) : The file location


**Returns**

* **bool**  : True or False: True if file exists False if not



----

### delete_file
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L48">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.delete_file(
   filepath: str
)
```

---
deletes file in path but only if it exists


**Args**

* **file_path** (str) : The file location


**Returns**

None


----

### get_path_list
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L64">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_path_list(
   path: str
)
```

---
Returns a list of each path part using slash as separator.


**Args**

* **file_path** (str) : The file location using the Posix format
    (forward/slashes)


**Returns**

* **path_list** (list) : A path of each folder in a path, with the
    file at the end.


**Example**

["path", "to", "file.ext"]


----

### get_full_path_string
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L81">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_full_path_string(
   path: str
)
```

---
returns absolute path to file in relative path.


**Args**

* **file_path** (str) : The file location using the Posix format
    (forward/slashes)


**Returns**

* **full_path** (Path Object) : will be a WindowsPath (if Windows) or
    PosixPath (if Mac or Linux)



----

### file_to_string
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L99">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.file_to_string(
   path: str
)
```

---
Returns contents of file as a string.


**Args**

* **path** (str) : The path to a file using Posix format (forward
    slashes e.g. path/to/file.ext)


**Returns**

* **file_text** (str) : The contents of the file in utf-8 string
    format.



----

### get_file_type
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L115">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_file_type(
   path: str
)
```

---
returns the extension of the file in the path.


**Args**

* **path** (str) : The path to a file using Posix format (forward
    slashes e.g. path/to/file.ext)


**Returns**

* **extension** (str) : The extension of the file type (without)
the dot (eg. html, js, css, pdx, png)


----

### get_file_name
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L132">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_file_name(
   path: str
)
```

---
returns the name of the file in the path.


**Args**

* **path** (str) : The path to a file using Posix format (forward
    slashes e.g. path/to/file.ext)


**Returns**

* **filename** (str) : The name of the file (with extension)



----

### get_linked_css
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L146">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_linked_css(
   contents_str: str
)
```

---
returns a list of linked CSS files.


**Args**

* **contents_str** (str) : HTML code from a file in string format.


**Returns**

* **filenames** (list) : A list of all filenames extracted from CSS
    link tags.


**Note**

local files).


----

### get_all_project_files
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L178">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_all_project_files(
   dir_path: str
)
```

---
returns a list of all files from the directory in the path.


**Args**

* **dir_path** (str) : The path to a directory using Posix format
    (forward slashes e.g. path/to/file.ext)


**Returns**

* **files** (list) : A list of all html, css, and javascript files



----

### get_all_files_of_type
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L195">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.get_all_files_of_type(
   dir_path: str, filetype: str
)
```

---
returns all files of a particular type from a directory.


**Args**

* **dir_path** (str) : The path to a directory using Posix format
    (forward slashes e.g. path/to/file.ext)
* **file_type** (str) : An extension in the form of a string (without
    the dot (html, css, js, etc.))


**Returns**

* **files** (list) : A list of all html, css, and javascript files



----

### split_into_sentences
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L214">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.split_into_sentences(
   contents: str
)
```

---
Returns a list of each sentence from the text.


**Args**

* **contents** (str) : A string of text (typically from a tag) that
    most likely has punctuation.


**Returns**

* **sentences** (list) : A list of each sentence from the text
    each in string format



----

### remove_tags
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L230">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.remove_tags(
   element: str
)
```

---
Removes all HTML tags from another tag's contents


**Args**

* **element** (str) : the contents of a tag as a string form which might or
might not have extra tags (in particular inline tags, such as <em>
or <a>, etc.)


**Returns**

* **tagless_content** (str) : the contents of the tag minus any inner tags.



----

### clear_extra_text
<a href="https://github.com/HundredVisionsGuy/file-clerk\blob\main\file_clerk/clerk.py\#L245">
<img height="16px" width="16px" src="/img/GitHub-Mark-32px.png">
source
</a>
```python
.clear_extra_text(
   my_text: str
)
```

---
Removes line returns and extra spaces from my_text.


**Args**

* **my_text** (str) : text which may include line returns or extra space.


**Returns**

* **stripped_text** (str) : text without any line returns or additional spaces.


