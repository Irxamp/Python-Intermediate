import random
random_number=random.randint(0, 125)
print(random_number)
from PIL import Image, ImageDraw
 
# Пустой желтый фон.
im = Image.new('RGB', (500, 300), (219, 193, 27))
draw = ImageDraw.Draw(im)
im.show()