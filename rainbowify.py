from PIL import Image

img = Image.open('boun_logo.png', 'r').convert('RGBA')
width, height = img.size
print(width, height)
new_img = Image.new('RGBA', (width, height), color='red')
pixel_values = list(img.getdata())


colors = [
    [255, 0, 24, 255],  # Red
    [255, 165, 44, 255],  # Orange
    [255, 255, 65, 255],  # Yellow
    [0, 128, 24, 255],  # Green
    [0, 0, 249, 255],  # Blue
    [134, 0, 125, 255]  # Purple
]

for i in range(0, height):
    color_order = (i * len(colors)) // height
    for j in range(0, width):
        pixel = pixel_values[i * width + j]
        r, g, b, a = pixel
        if r != 0 or g != 0 or b != 0 or a != 0:
            color = colors[color_order]
            pixel_values[i * width + j] = (color[0], color[1], color[2], a)


new_img.putdata(pixel_values)
new_img = new_img.save("new_img_converted.png")
