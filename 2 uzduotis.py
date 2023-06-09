# Susikurti klasę “Figūra”, kuri saugoja ilgį ir plotį. Klasė turi turėti metodus plotui ir perimetrui apskaičiuoti ir grąžinti
#
# Susikurti klasę “Stačiakampis”, kuris paveldi iš “Figūra”. Stačiakampio klasėje turi būti įgyvendinti stačiakampio ploto ir perimetro skaičiavimo metodai.
#
# Susikurti klasę “StatusisTrikampis”, kuris paveldi iš “Figūra”. Trikampio klasėje turi būti įgyvendinti stačiojo trikampio ploto ir perimetro skaičiavimo metodai.
#
# Susikurti bent po vieną stačiakampį ir trikampį, atspausdinti jų plotus ir perimetrus
#
# # Testing the classes
# rectangle = Rectangle(5, 10)
# triangle = RightTriangle(3, 4)
#
# print("Rectangle Information:")
# print("Area:", rectangle.calculate_area())
# print("Perimeter:", rectangle.calculate_perimeter())
# print()
#
# print("Right Triangle Information:")
# print("Area:", triangle.calculate_area())
# print("Perimeter:", triangle.calculate_perimeter())

class Figura:
    def plotas(self):
           pass
    def perimetras(self):
           pass

class staciakampis(Figura):
    def plotas(self, plotas, aukstis):
        self.plotas = plotas
        self.aukstis = aukstis
        return self.plotas * self.aukstis

    def perimetras(self, plotas, aukstis):
        self.plotas = plotas
        self.aukstis = aukstis
        return 2 * (plotas + aukstis)

print(f'Staciakampio plotas:',staciakampis().plotas(6, 10))
print(f'Staciakampio perimetras:',staciakampis().perimetras(6, 10))


class statusistrikampis(Figura):
    def plotas(self,krastine1, krastine2):
        self.krastine1 = krastine1
        self.krastine2 = krastine2
        return (self.krastine1 * self.krastine2)/2

    def perimetras(self, krastine1, krastine2, krastine3):
        self.krastine1 = krastine1
        self.krastine2 = krastine2
        self.krastine3 = krastine3
        return self.krastine1 + self.krastine2 + self.krastine3

print(f'Staciojo trikampio plotas:',statusistrikampis().plotas(6, 10))
print(f'Staciojo trikampio perimetras:',statusistrikampis().perimetras(5, 6, 10))