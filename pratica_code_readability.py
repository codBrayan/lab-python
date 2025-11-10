
velocidade_carro = 61
local_carro_km = 99

RADAR_1 = 60 #Valocidade máx do radar 1 (Não se altera)
LOCAL_RADAR = 100
RADAR_RANGE = (LOCAL_RADAR - 1) and (LOCAL_RADAR + 1)

print(RADAR_RANGE)
passou_radar = local_carro_km == RADAR_RANGE
vel_carro_passou_limite = velocidade_carro >= RADAR_1

if passou_radar and vel_carro_passou_limite:
    print('Multado"!')