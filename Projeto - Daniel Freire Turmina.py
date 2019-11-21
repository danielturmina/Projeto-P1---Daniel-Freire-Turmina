"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Daniel Freire Turmina (dft)
Email: dft@cin.ufpe.br
Data: 2019-11-15

Copyright(c) 2019 Daniel Freire Turmina
"""

from datetime import datetime
from funcoes import *

""" O sistema foi desenvolvido para cadastrar os treinamentos realizados pelos empregados de uma empresa."""

print("Programa de Cadastro de Treinamento\n")


if acesso == "analista" or acesso == "estagiario" or acesso == "admin":

    listaInicial = descripto()
    listaGeral = abertura(listaInicial)
    dic = dicionario(listaGeral)

    continuar = True
    while continuar:
        menu = input("O que você deseja fazer?\nDigite 1 - Para Cadastrar um Treinamento\nDigite 2 - Para Alterar um Treinamento Cadastrado\nDigite 3 - Para Realizar uma Busca\nDigite 4 - Para Gerar Relátorio\nDigite 5 - Para Remover um Treinamento Cadastrado\nDigite 6 - Para Ordernar Treinamentos Registrados\nDigite 7 - Para Cadastrar, Alterar ou Remover Usuários\nDigite 8 - Para Sair\n")
        if menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5" and menu != "6" and menu != "7" and menu != "8":
           print("\nOpção Inválida!\n")        
        elif menu == "1":
            if acesso == "analista" or acesso == "admin":
                dic = dicionario(listaGeral)
                listaGeral = cadastroTreinamento(dic)
            elif acesso == "estagiario":
                print("\nVocê não possui acesso para realizar cadastros!!\n")
        elif menu == "2":
            if acesso == "analista" or acesso == "admin":
                dic = dicionario(listaGeral)
                altera(listaGeral,dic)
            elif acesso == "estagiario":
                print("\nVocê não possui acesso para realizar alterações!!\n")
        elif menu == "3":
            buscar(listaGeral,dic)
        elif menu == "4":
            if acesso == "analista" or acesso == "admin":
                relatorio(listaGeral)
            elif acesso == "estagiario":
                print("\nVocê não possui acesso para gerar relatórios!!\n")
        elif menu == "5":
            if acesso == "analista" or acesso == "admin":
                dic = dicionario(listaGeral)
                elimina(listaGeral,dic)
            elif acesso == "estagiario":
                print("\nVocê não possui acesso para remover treinamentos!!\n")
        elif menu == "6":
            if acesso == "analista" or acesso == "admin":
                ordenar(listaGeral)
            elif acesso == "estagiario":
                print("\nVocê não possui acesso para ordenar treinamentos!!\n")
        elif menu == "7":
            if acesso == "admin":
                cadastroUsuario(login)
            elif acesso == "estagiario" or acesso == "analista":
                print("\nVocê não possui acesso para cadastrar, alterar ou remover usuários!!\n")     
        elif menu == "8":
            print("\nPrograma Finalizado!!\n")
            continuar = False
