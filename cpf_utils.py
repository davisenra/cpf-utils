#!/usr/bin/env python3

import argparse
import random
import re
from sys import argv
from typing import List


def main():
    parser = argparse.ArgumentParser(description="Gerador/validador de CPFs")
    parser.add_argument("-g", help="Gera (n) CPFs válidos",
                        type=int, nargs="?", const=1, action="store", dest="qtd")
    parser.add_argument("-c", help="Checa se o CPF informado é válido",
                        type=str, action="store", dest="checker")
    args = parser.parse_args()

    parse_arguments(args, parser)
    return


def parse_arguments(args: str, parser):
    "Parseia argumentos fornecidos pelo usuário"
    if (len(argv) == 3):
        if (argv[1] == "-g"):
            for i in gerador(args.qtd):
                print(formatar_cpf(i))
        elif (argv[1] == "-c"):
            if (validador(args.checker)):
                print("CPF válido")
            else:
                print("CPF inválido")
    else:
        parser.print_help()


def validador(cpf: str) -> str:
    "Verifica se CPF informado pelo usuario é válido"
    digito = verifica_digitos(verifica_digitos(limpa(cpf[:-2]), 10), 11)
    if (digito == limpa(cpf)):
        return True
    else:
        return False


def gerador(n: int) -> List:
    "Gera [n] CPFs válidos"
    cpfs = []
    for i in range(n):
        base = str(random.randint(100000000, 999999999))
        digito = verifica_digitos(verifica_digitos(base, 10), 11)
        cpfs.append(digito)
    return cpfs


def verifica_digitos(cpf: str, k: int) -> str:
    """Algoritmo para obter dígitos verificadores válidos 
    com base nos primeiros 9 dígitos informados"""
    summ = 0
    for i in cpf:
        summ += int(i) * k
        k -= 1
    if ((summ % 11) < 2):
        return cpf + "0"
    else:
        return cpf + str(11-(summ % 11))


def formatar_cpf(cpf: str) -> str:
    "Formata CPF com pontos e héfem"
    return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]


def limpa(cpf: str) -> str:
    "Limpa CPF caso usuário insira pontos e/ou hífem"
    return re.sub(r"\D", "", cpf)


if __name__ == "__main__":
    main()
