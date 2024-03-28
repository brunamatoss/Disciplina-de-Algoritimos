
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor no mês: "))

# calcula a comissao (15%)
comissao = total_vendas * 0.15

salario_total = salario_fixo + comissao

print("Salário total do vendedor:", salario_total)