# Import the wanted file to the jpeg file
def hide(jpeg_file, to_hide_file):
    with open(str(jpeg_file), 'ab') as photo, open(str(to_hide_file), 'rb') as file:
        photo.write(file.read())


# Export the hidden file from the jpeg file to our local directory
def export(jpeg_file, exported_file):
    with open(str(jpeg_file), 'rb') as photo:
        photo.seek(photo.read().index(bytes.fromhex('FFD9')) + 2)

        with open(str(exported_file), 'wb') as file:
            file.write(photo.read())
