def area_triangulo(base, altura):
    return base*altura/2

area_a = area_triangulo (5, 4)
area_b = area_triangulo (6, 8)
sum = area_a + area_b

print ("Soma das areas dos tringulos: " + str(sum)) #TypeError float se nao chamar o STR()