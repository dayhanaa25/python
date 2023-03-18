frutas = {'Plátano':800, 'Manzana':1200, 'Pera':1000, 'Naranja':1100, 'Mango':1400, 'Granadilla':1200, 'Papaya':2500, 'Piña':6000}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")