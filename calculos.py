import os

os.system('cls')

#Calcula o salário por hora sem periculosidade.
def salario_por_hora(salario:float) -> float:    
    horas_trab = 220
    return salario / horas_trab

#Calcula o valor da periculosidade em cima do salário base.
def periculosidade(salario:float, porcentagem: float) -> float:
    return salario * (porcentagem / 100)

#Calcula o salário total incluindo periculosidade.
def salario_total(salario:float, porcentagem_periculosidade:float) -> float:
    valor_periculosidade = periculosidade(salario, porcentagem_periculosidade)
    return salario + valor_periculosidade

#Calcula o salário por hora incluindo periculosidade.
def salario_hora_com_peric(salario:float, porcentagem_periculosidade:float) -> float:
    salario_total_com_peric = salario_total(salario, porcentagem_periculosidade)
    horas_trab = 220
    return salario_total_com_peric / horas_trab

#Calcula o valor da hora extra a 50%.
def hora_extra_cinq(salariohora:float) -> float:
    return salariohora * 1.5

#Calcula o valor da hora extra a 100%.
def hora_extra_cem(salariohora:float) -> float:
    return salariohora * 2

#CALCULA O VALOR DE RECEBER EM CIMA DAS SUAS HORAS FEITAS
def total_horas_cinq(quantidade_horas:float, hora_extra_cinq:float) -> float:
    return quantidade_horas * hora_extra_cinq

#CALCULA O VALOR DE RECEBER EM CIMA DAS SUAS HORAS FEITAS
def total_horas_cinq(quantidade_horas:float, hora_extra_cinq:float) -> float:
    return quantidade_horas * hora_extra_cinq

#CALCULA O VALOR DE RECEBER EM CIMA DAS SUAS HORAS FEITAS
def total_horas_cem(quantidade_horas:float, hora_extra_cem:float) -> float:
    return quantidade_horas * hora_extra_cem

