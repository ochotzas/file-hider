# Hide any file/program in a JPEG file.

### JPG Signature Format: Documentation.
JPEG (Joint Photographic Experts Group) is a commonly used method of lossy compression for digital images and start with an image marker which always contains the marker code hex values `FF D8 FF`.

![](https://i.ibb.co/dM487yY/2.png)

It does not have a length of the file embedded, thus we need to find JPEG trailer, which is `FF D9`.

![](https://i.ibb.co/hBpPNzn/1.png)

This information helps us so we can know when a JPEG file ends. Looking further, we notice that we can include/write binary content after the end of the file without changing the actual image.

### Hiding Files in JPEGs

This code provides two functions that can be used to hide a file within a JPEG file and export a hidden file from a JPEG file.

`hide(jpeg_file, to_hide_file)`

This function takes in two parameters:

- `jpeg_file`: the path to the JPEG file that will contain the hidden file
- `to_hide_file`: the path to the file that will be hidden within the JPEG file

The function opens the JPEG file in binary append mode and appends the contents of the `to_hide_file` to the end of the JPEG file.

`export(jpeg_file, exported_file)`

This function takes in two parameters:

- `jpeg_file`: the path to the JPEG file that contains the hidden file
- `exported_file`: the path to the file where the hidden file will be exported

The function opens the JPEG file in binary read mode, seeks to the end of the file, and writes the hidden file to the `exported_file`.

**Note:** This technique of hiding files within JPEG files is not very secure, as it is relatively easy to detect the presence of a hidden file in a JPEG file using basic image editing tools.
