from PIL import Image
import base64

def prepare_image_for_save(image, width, height):
    resized_image = resize_image(image, width, height)
    binary_image = convert_image_to_binary(resized_image)

    return binary_image

def resize_image(image_file, width, height):
    image = Image.open(image_file)
    resized_image = image.resize((width, height))
    return resized_image

def convert_image_to_binary(image):
    image_data = image.read()
    image_binary = base64.b64encode(image_data)
    return image_binary