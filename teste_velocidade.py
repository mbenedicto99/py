vel = 60
local_carro = 90

radar_1 = 60
local_1 = 100
radar_range = 1

vel_carro_pass_radar1 = vel > radar_1
multado_radar1 = local_carro >= (local_1 - radar_range) and \
          local_carro <= (local_1 + radar_range)

print (multado_radar1)
print (vel_carro_pass_radar1)

'''
Operadores de atribuição
==, +=, -=, *=, /= (float), //= (int), **= (potencia), %= (modulo)
'''
cont = 0
print (f'{cont=}')

while cont <= 10:
    cont += 1
    print(f"estou na linha {cont=}")