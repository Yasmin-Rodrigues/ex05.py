#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
v =float(input('Digite uma distância em metros:'))
cm =v*100
mm =v*1000
print('Medida em centímetros: {}cm \nMedida em metros: {}mm'.format(cm, mm))