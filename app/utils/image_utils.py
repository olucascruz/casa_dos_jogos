from PIL import Image
import base64
import io

def prepare_image_for_save(image, width, height):
    image_buffer = io.BytesIO()
    porcent_quality_image = 80
    image.save(image_buffer, format="JPEG", quality=porcent_quality_image)
    resized_image = resize_image(image_buffer, width, height)
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

def convert_binary_to_image(games):
    for game in games:
        image_binary = game.image
        image = Image.open(io.BytesIO(image_binary))
        image_format = image.format
        image_buffer = io.BytesIO()
        # Salve a imagem no buffer usando o formato correto
        image.save(image_buffer, format=image_format)

        game.image = image
    
    return games 
