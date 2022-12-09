import logging

# Set the log level and format
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


# Import the wanted file to the jpeg file
def hide(jpeg_file, to_hide_file):
    try:
        with open(jpeg_file, 'ab') as photo, open(to_hide_file, 'rb') as file:
            photo.write(file.read())
    except FileNotFoundError:
        logging.error(f"{jpeg_file} or {to_hide_file} not found.")
    finally:
        if logging.lastResort:
            logging.raiseExceptions = True
        else:
            logging.info("File imported successfully.")


# Export the hidden file from the jpeg file to our local directory
def export(jpeg_file, exported_file):
    try:
        with open(jpeg_file, 'rb') as photo:
            try:
                photo.seek(photo.read().index(bytes.fromhex('FFD9')) + 2)
            except ValueError:
                logging.error("'FFD9' value not found in jpeg file.")
                return

            with open(exported_file, 'wb') as file:
                file.write(photo.read())
    except FileNotFoundError:
        logging.error(f"{jpeg_file} or {exported_file} not found.")
    finally:
        if logging.lastResort:
            logging.raiseExceptions = True
        else:
            logging.info("File exported successfully.")
