from PIL import Image
from io import BytesIO

def resizeImage(image, target_width):
    image_stream = BytesIO(image)
    image = Image.open(image_stream)
    original_width, original_height = image.size
    target_height = int((original_height / original_width) * target_width)
    image.thumbnail((target_width, target_height))
    resized_image_stream = BytesIO()
    image.save(resized_image_stream, format="JPEG")
    return resized_image_stream.getvalue()