from  PIL import Image
import numpy as np
if __name__ == '__main__':

    image_file = 'lena.png'
    height = 100
    image = Image.open(image_file)
    image_width, image_height = image.size
    width = int(1.8 * height * image_width // image_height)
    image = image.resize((width, height), Image.ANTIALIAS)
    pixels = np.array(image.convert('L'))
    print('type(pixels) = ', type(pixels))
    print(pixels.shape)
    print(pixels)
    chars = "MNHQOC?&>!:-;."
    N = len(chars)
    step = 256 // N
    print('N:',N)
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j] // step]
        result += '\n'
    with open('text.txt', mode='w') as f:

        f.write(result)

