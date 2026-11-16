def calculadora_numerica(tipo_calculo, numero1, numero2):
# Define a função calculadora_numerica, que recebe três parâmetros:
# tipo_calculo: a operação escolhida no menu (1 a 4).
# numero1 e numero2: os dois valores da conta.

    if tipo_calculo == 1:
        total = numero1 * numero2
        return f'{numero1} * {numero2} = {total}'
    if tipo_calculo == 2:
        if numero2 == 0:
            return 'Erro: Divisão por zero'
        else:
            total = numero1 / numero2
            return f'{numero1} / {numero2} = {total}'
    if tipo_calculo == 3:
        total = numero1 + numero2
        return f'{numero1} + {numero2} = {total}'
    if tipo_calculo == 4:
        total = numero1 - numero2
        return f'{numero1} - {numero2} = {total}'
