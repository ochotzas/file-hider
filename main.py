import hideExportJpeg as hej

# Hide the wanted file. Ex. { hide main.c in the JPEG file }
hej.hide('photo.jpg', 'pascalsTriangle.c')
# Export the hidden file
hej.export('photo.jpg', 'newPascalsTriangle.c')
