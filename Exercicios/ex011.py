# Desafio 011: Pintando a parede. - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Digite a largura da sua parede em metros: '))
altura = float(input('Digite a altura da sua parede em metros: '))
area = largura * altura
tinta = area / 2
print(f'A área da parede é de {area}m² e você precisará de {tinta} litros de tinta para pintá-la.')