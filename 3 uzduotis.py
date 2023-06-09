# Trečia užduotis - Logging
#
#
# Sukurti programa, kuri paprašytų įvesti stačiakampio ilgį ir plotį.
# Sukurti funkcija, kuri priimtų ilgį ir plotį, apskaičiuotų plotą bei perimetrą ir juos grąžintų. Gautą rezultatą
# išspausdinti į terminalą. Taip pat, reikia į programą pridėti loggerį ir išlogginti rezultatą (plotą ir perimetrą) į failą.



import logging

logging.basicConfig(filename="rezultatas.log", encoding="UTF-8", level=logging.DEBUG)

def skaiciuoti_staciakampio_plota_ir_perimetra(ilgis, plotis):
    plotas = ilgis * plotis
    perimetras = 2 * (ilgis + plotis)
    return plotas, perimetras

def ivedimas():
    ilgis = int(input("Įveskite staciakampio ilgi: "))
    plotis = int(input("Įveskite staciakampio ploti: "))
    plotas, perimetras = skaiciuoti_staciakampio_plota_ir_perimetra(ilgis, plotis)


    print(f'Staciakampio plotas: {plotas}')
    print(f'Staciakampio perimetras: {perimetras}')


    logging.info(f'Staciakampio plotas: {plotas}')
    logging.info(f'Staciakampio perimetras: {perimetras}')



ivedimas()