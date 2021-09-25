# Hide any file/program in a JPEG file.

### JPG Signature Format: Documentation.
JPEG (Joint Photographic Experts Group) is a commonly used method of lossy compression for digital images and start with an image marker which always contains the marker code hex values `FF D8 FF`.

![](https://i.ibb.co/dM487yY/2.png)

It does not have a length of the file embedded, thus we need to find JPEG trailer, which is `FF D9`.

![](https://i.ibb.co/hBpPNzn/1.png)

This information helps us so we can know when a JPEG file ends. Looking further, we notice that we can include/write binary content after the end of the file without changing the actual image.

### Hide any file in a JPEG file.
Simply (have a look at `main.py`):
1. Import the file that contains the functions: `import hideExportJpeg as hej`.
2. Start using the functions:
    - `hide(jpeg_file, to_hide_file)`: it is used to hide the wanted file in the jpeg file.
    - `export(jpeg_file, exported_file)`: it is used to export the hidden file.

###### Actual photo (the `photo.jpg`) from [Pexels](https://www.pexels.com).
