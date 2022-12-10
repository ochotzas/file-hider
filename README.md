# File-Hider

File-Hider is a library for hiding files in jpeg files. It provides two functions: hide and export.

## Installation

file-hider can be installed using pip:

````
pip install file-hider
````

## Usage

Here is an example of how to use file-hider in your Python code:

````python
import file_hider

# Import the wanted file to the jpeg file
file_hider.hide('jpeg_file.jpg', 'to_hide_file.txt')

# Export the hidden file from the jpeg file to our local directory
file_hider.export('jpeg_file.jpg', 'exported_file.txt')
````

The hide function takes two arguments: the path to the jpeg file and the path to the file to be hidden in the jpeg file. It appends the content of the file to the end of the jpeg file.

The export function takes two arguments: the path to the jpeg file and the path to the exported file. It exports the hidden file from the jpeg file to the specified path.