# Penkta užduotis - Pillow
# Sukurti programa, kuri uždėtų nuotraukai kontrastą ir išsaugotų atnaujintą nuotrauką

#kazko nedave irasyti terminale pip install Pillow, vis rase (command not found) tai uzbaigti uzduoties nepavyko.

from PIL import Image, ImageEnhance
dog = Image.open('Teide.jpeg')
enh = ImageEnhance.Contrast(dog)
enh.enhance(1.3).show()

#jišsaugoti:
enh.enhance(1.3).save('test.png')
