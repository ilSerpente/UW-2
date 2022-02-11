from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("fonts/jetbrains-mono/JetBrainsMono-Regular.ttf", 54)

def image_with_number(imageHeight, imageWidth, number):
    # (nw, nh) = font.getsize(str(number))
    img = Image.new('RGB', (imageWidth, imageHeight), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text(xy=(imageWidth / 2, (imageHeight / 2)), text=str(number), fill=(0, 0, 0), anchor="mm", font=font)
    img.save('cool_image_{}.png'.format(number))

def create_image_range(fromNumb, toNumb, height, width):
    for i in range(fromNumb, toNumb + 1):
        image_with_number(height, width, i)

create_image_range(1, 100, 100, 100)