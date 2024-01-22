"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_passou
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

if velocidade_carro_passou:
    print('Passou da velocidade')


if carro_passou_radar:
    print('Carro passou no radar')


if carro_multado:
    print('Carro multado')
