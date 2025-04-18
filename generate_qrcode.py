import qrcode
from PIL import Image, ImageDraw

def generate_qr_code(data, id):
    # Create QR code instance
    qr = qrcode.QRCode(
        # version can be an integer from 1 to 40, or a string like 'L', 'M', 'Q', 'H'
        # 'L' is the lowest error correction level, 'H' is the highest
        # Here, we use version 3 for a medium-sized QR code
        version=5,
        #  error_correction can be one of the following:
        # qrcode.constants.ERROR_CORRECT_L (7% error correction)
        # qrcode.constants.ERROR_CORRECT_M (15% error correction)
        # qrcode.constants.ERROR_CORRECT_Q (25% error correction)
        # qrcode.constants.ERROR_CORRECT_H (30% error correction)

        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # box_size is the size of each box in the QR code grid
        # It can go from 1 to 10, where 1 is the smallest size
        # Here, we use 10 for a larger QR code
        box_size=10,
        # border is the thickness of the border (minimum is 4, maximum is 10)
        border=4,
    )

    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Load logo
    logo = Image.open("logo.jpg").convert("RGBA")  # Replace with your logo file

    # Make logo square
    logo_width, logo_height = logo.size
    if logo_width > logo_height:
        left = (logo_width - logo_height) / 2
        top = 0
        right = (logo_width + logo_height) / 2
        bottom = logo_height
        logo = logo.crop((left, top, right, bottom))
    elif logo_height > logo_width:
        left = 0
        top = (logo_height - logo_width) / 2
        right = logo_width
        bottom = (logo_height + logo_width) / 2
        logo = logo.crop((left, top, right, bottom))

    # Resize logo to 58x58 (adjust size as needed)
    logo = logo.resize((58, 58), Image.LANCZOS)

    # Make logo circular
    mask = Image.new("L", logo.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + logo.size, fill=255)
    logo.putalpha(mask)

    # Paste logo onto QR code
    qr_width, qr_height = img.size
    paste_position = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)
    img.paste(logo, paste_position, mask=logo)

    # img = qr.make_image(
    #     image_factory=StyledPilImage,
    #     embeded_image_path="logo.jpg"  # Replace with your logo file
    # )

    img.save(f"qrcode_{id}.png")


# Data to encode in the QR code
data = "https://example.com"

generate_qr_code(data, 40)