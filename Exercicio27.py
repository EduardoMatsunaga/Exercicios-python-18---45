#definição de variaveis
voltas: float = 0.0
extensao: float = 0.0
tempo: float = 0.0
velocidade: float = 0.0
distancia: float = 0.0
#inicio
voltas = float(input('Digite a quantidade de voltas:'))
extensao = float(input('Digite a extensão do circuito (metros):'))
tempo = float(input('Digite o tempo de duração (minutos):'))
distancia = (voltas * extensao) / 1000
tempo = tempo / 60
velocidade = distancia  / tempo
print('A velocidade media foi:', velocidade, 'km/h')
#fim 