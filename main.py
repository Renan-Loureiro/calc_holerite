import calculos

salario_base = 2382.85
porcentagem_periculosidade = 30



salario_hora = calculos.salario_por_hora(salario_base)
valor_periculosidade = calculos.periculosidade(salario_base, porcentagem_periculosidade)
salario_total_com_peric = calculos.salario_total(salario_base, porcentagem_periculosidade)
salario_hora_com_peric = calculos.salario_hora_com_peric(salario_base, porcentagem_periculosidade)
hora_extra_50 = calculos.hora_extra_cinq(salario_hora_com_peric)
hora_extra_100 = calculos.hora_extra_cem(salario_hora_com_peric)
total_horas_50 = calculos.total_horas_cinq(16.22, hora_extra_50)
total_horas_100 = calculos.total_horas_cem(25.17, hora_extra_100)

print(f'Salário por hora: R${salario_hora:.2f}')
print(f'Valor da periculosidade: R${valor_periculosidade:.2f}')
print(f'Salário total com periculosidade: R${salario_total_com_peric:.2f}')
print(f'Salário por hora com periculosidade: R${salario_hora_com_peric:.2f}')
print(f'Hora extra a 50%: R${hora_extra_50:.2f}')
print(f'Hora extra a 100%: R${hora_extra_100:.2f}')
print(f'Hora extra a receber a 50%: {total_horas_50:.2f}')
print(f'Hora extra a receber a 100%: {total_horas_100:.2f}')