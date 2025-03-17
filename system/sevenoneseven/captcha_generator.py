import random
import string
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

# Carpeta donde se guardarán las imágenes CAPTCHA
CAPTCHA_DIR = os.path.join(settings.BASE_DIR, "sevenoneseven/static/captchas")
os.makedirs(CAPTCHA_DIR, exist_ok=True)

def generate_captcha():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # Generar texto aleatorio

    # Crear imagen en blanco
    image = Image.new('RGB', (150, 60), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Fuente (Debes tener la fuente en static/fonts/)
    font_path = os.path.join(settings.BASE_DIR, "static/fonts/DejaVuSans-Bold.ttf")
    font = ImageFont.truetype(font_path, 40)

    draw.text((20, 10), captcha_text, font=font, fill=(0, 0, 0))

    # Guardar la imagen
    filename = f"{captcha_text}.png"
    image_path = os.path.join(CAPTCHA_DIR, filename)
    image.save(image_path)

    return captcha_text, filename
