#valor_01 = 3
#valor_02 = 5
#print(valor_01 + valor_02)


def filtrar_acima_de(lista_de_salarios:list[float],salario_max:float) -> list:
    lista_de_salarios_acima: list = []
    for salario in lista_de_salarios:
        if salario > salario_max:
            lista_de_salarios_acima.append(salario)
    return lista_de_salarios_acima

if __name__ == "__main__":
    lista = [3000,4000,150000]
    max = 10000
    #return lista_de_salarios_max = [150000]
    print(filtrar_acima_de(lista_de_salarios=lista,salario_max=max))