valor_capa = 24.95
desconto = 40
transporte1 = 3.00
transporte_resto = 0.75
resultado1 = desconto * valor_capa / 100
resultado2 = resultado1 + transporte1
resultadoresto = resultado1 + transporte_resto
resultadofinal1 = resultadoresto * 59
resultado_total = resultadofinal1 + resultado2

print(resultado_total)