from datetime import datetime

def chavePriv():
    """Função para importar os valores salvos como Chave Privada e possibilitar a descriptografia."""
    arq = open("chavePrivada.txt","r")
    linha = arq.readlines()
    arq.close()
    listaF = []
    string = ""
    for t in linha:
        string = ""
        for x in t:
            if x!= " ":
                string = string + x    
            if x == " ":
                listaF.append(string)
                string = ""
    if string != "":
        listaF.append(string)
    return listaF
    
def chavePub():
    """Função para importar os valores salvos como Chave Pública e possibilitar a criptografia."""
    arq = open("chavePublica.txt","r")
    linha = arq.readlines()
    arq.close()
    listaG = []
    string = ""
    for t in linha:
        string = ""
        for x in t:
            if x!= " ":
                string = string + x    
            if x == " ":
                listaG.append(string)
                string = ""
    if string != "":
        listaG.append(string)
    return listaG

def descripto():
    """Função para descriptografar as informações armazenadas no arquivo elementos.txt"""
    listaF = chavePriv()
    d = int(listaF[0])
    m = int(listaF[1])
    arq = open("elementos.txt","r")
    listaLinhas = arq.readlines()
    arq.close()
    listaGeral = []
    for t in listaLinhas:
        string = ""
        stringFinal =  ""
        for r in t:
            if r != " " and r != "\n":
                string = string+r
            if r == " ":
                valor = int(string)
                string = ""
                x = chr(valor**d % m)
                stringFinal = stringFinal + x
            if r == "\n":
                listaGeral.append(stringFinal)
    return listaGeral

def cripto(dic):
    """Função para criptografar as informações e armazenar no arquivo elementos.txt"""
    listaG = chavePub()
    e = int(listaG[0])
    n = int(listaG[1])
    chaves = dic.keys()
    listaCripto =  []
    for a in chaves:
        tupla = dic[a]
        chaveCripto = ""
        for b in a:
           y = (((ord(b))**e) % n)
           x = str(y)
           chaveCripto = chaveCripto + x + " "
        listaCripto.append(chaveCripto)
        for c in tupla:
            itemCripto = ""
            for d in c:
                f = (((ord(d))**e) % n)
                z = str(f)
                itemCripto = itemCripto + z + " "
            listaCripto.append(itemCripto)
    total = len(listaCripto)
    arq = open("elementos.txt","w")
    for h in range(total):
        arq.write(listaCripto[h])
        arq.write("\n")
    arq.close()
    
def dicionarioLogins():
    """Função para importar todos os usuários registrados (Retorna um Dicionário de Usuários: {login:(senha,nível de acesso)})."""
    arq = open("usuarios.csv","r")
    listaInicial = arq.readlines()
    dicLogins = {}
    for t in listaInicial:
        a = t.split(";")
        if a != ["Login","Senha","Nível de Acesso\n"] and a!= ["Login","Senha","Nível de Acesso","\n"] and a!= ["","",""] and a != ["","","\n"] and a!= ["","","","\n"]:
            chave = a[0]
            string = ""
            for i  in a[2]:
               if i != "\n":
                   string = string+i
            a[2] = string
            tupla = (a[1],a[2])
            dicLogins[chave] = tupla
    arq.close()
    return dicLogins

def login():
    """Função que solicita login e senha do usuário e verifica se esse login e senha estão corretos (Caso login e senha sejam informados corretamente, retorna o login)."""
    dicLogins = dicionarioLogins()
    continuar = True
    while continuar:
        login = input("Digite o seu Login: ")
        teste = login in dicLogins
        if teste == False:
            print("\nLogin Inválido!!\n")
        else:
            continuar2 = True
            continuar = False
    while continuar2:
        listaTupla = dicLogins[login]
        senhaCorreta = listaTupla[0]
        senha = input("Digite sua senha: ")
        if senhaCorreta == senha:
            listaLog8 = [login,dataTexto,"Entrou no Sistema."]
            listaLOG.append(listaLog8)
            log(listaLOG)
            print("\nSeja Bem Vindo!\n")
            return login
        else:
            print("\nSenha Inválida!!\n")
            
def salvarLogins(dicLogins):
    """Função para salvar os cadastros dos usuários (Salva no arquivo "usuarios.csv" todos os logins, senhas e níveis de acesso existentes)."""
    arq = open("usuarios.csv","w")
    arq.write("Login;")
    arq.write("Senha;")
    arq.write("Nível de Acesso;")
    arq.write("\n")
    lista1 = dicLogins.keys()
    for t in lista1:
        login = t
        s = dicLogins[t]
        senha = s[0]
        l = dicLogins[t]
        acesso = l[1]
        arq.write(login)
        arq.write(";")
        arq.write(senha)
        arq.write(";")
        arq.write(acesso)
        arq.write("\n")
    arq.close()

def importaLog():
    """Função para  importar todos os registros de log existentes (Retorna uma lista de Logs)."""
    arq = open("log.csv","r")
    listaInicial = arq.readlines()
    listaLOG = []
    listaAux = []
    for t in listaInicial:
        a = t.split(";")
        if a != ["Usuário","Data e Hora","Execução\n"] and a!= ["Usuário","Data e Hora","Execução","\n"] and a!= ["","",""] and a != ["","","\n"] and a!= ["","","","\n"]:
            string = ""
            for i  in a[2]:
               if i != "\n":
                   string = string+i
            a[2] = string
            listaAux = [a[0],a[1],a[2]]
            listaLOG.append(listaAux)
            listaAux = []        
    arq.close()
    return listaLOG

def log(listaLOG):
    """Função para registrar todas as operações do sistema (Cria o arquivo "LOG.csv" com as seguintes informações: quem executou, quando executou e o que executou)."""
    arq = open("log.csv","w")
    arq.write("Usuário;")
    arq.write("Data e Hora;")
    arq.write("Execução;")
    arq.write("\n")
    for t in listaLOG:
        usuario = t[0]
        data = t[1]
        execucao = t[2]
        arq.write(usuario)
        arq.write(";")
        arq.write(data)
        arq.write(";")
        arq.write(execucao)
        arq.write("\n")
    arq.close()   
    
def cadastroUsuario(login):
    """Função para realizar alterações cadastrais (Permite criar novo usuário, alterar senha ou nível de acesso e remover usuários cadastrados)."""
    continuar = True
    while continuar:
        desejo = input("\nO que você deseja fazer?\nDigite 1 - Cadastrar novo usuário\nDigite 2 - Remover usuário cadastrado\nDigite 3 - Alterar Senha de usuário cadastrado\nDigite 4 - Alterar nível de acesso de usuário cadastrado\nDigite 5 - Retornar ao Menu Principal\n")
        if desejo == "1":
            continuar3 = True
            while continuar3:
                login1 = input("Digite o login de acesso: ")
                teste = login1 in dicLogins
                if teste == True:
                    print("\nLogin já cadastrado!!\n")
                else:
                    senha = input("Digite a senha de acesso: ")
                    continuar2 = True
                    while continuar2:
                        tipo = input("Qual o nível de acesso?\nDigite 1 - Analista\nDigite 2 - Estagiário\n")
                        if tipo == "1":
                            acesso = "analista"
                            continuar2 = False
                        elif tipo == "2":
                            acesso = "estagiario"
                            continuar2 = False
                        else:
                            print("\nOpção Inválida!!\n")
                    tupla = (senha,acesso)
                    dicLogins[login1] = tupla
                    salvarLogins(dicLogins)
                    listaLog1 = [login,dataTexto,"Cadastrou um Novo Usuário: "+login1]
                    listaLOG.append(listaLog1)
                    log(listaLOG)
                    print("\nUsuário Cadastrado com Sucesso!!\n")
                    continuar = False
                    continuar3 = False
        elif desejo == "2":
            continuar8 = True
            while continuar8:
                login2 = input("\nDigite o login do usuário que você deseja remover: ")
                teste = login2 in dicLogins
                if teste == False:
                    print("\nUsário não encontrado!!\n")
                    continuar8 = False    
                elif login == login2:
                    print("\nVocê não pode remover o seu usuário!!\n")
                    continuar8 = False
                else:
                    dicLogins.pop(login2)
                    salvarLogins(dicLogins)
                    listaLog2 = [login,dataTexto,"Removeu o Usuário: "+login2]
                    listaLOG.append(listaLog2)
                    log(listaLOG)
                    print("\nUsuário Removido com Sucesso!!\n")
                    continuar = False
                    continuar8 = False            
        elif desejo == "3":
            continuar5 =  True
            while continuar5:
                login2 = input("\nDigite o login do usuário que você deseja alterar a senha: ")
                teste = login2 in dicLogins
                if teste == False:
                    print("\nUsário não encontrado!!\n")
                    continuar5 = False    
                else:
                    novaSenha = input("\nDigite a nova senha: ")
                    valores = dicLogins[login2]
                    novaTupla=(novaSenha,valores[1])
                    dicLogins[login2] = novaTupla
                    salvarLogins(dicLogins)
                    listaLog3 = [login,dataTexto,"Alterou Senha do Usuário: "+login2]
                    listaLOG.append(listaLog3)
                    log(listaLOG)
                    print("\nAlteração Realizada com Sucesso!!\n")
                    continuar = False
                    continuar5 = False
        elif desejo == "4":
            continuar6 =  True
            while continuar6:
                login3 = input("\nDigite o login do usuário que você deseja alterar o nível de acesso: ")
                teste = login3 in dicLogins
                if teste == False:
                    print("\nUsário não encontrado!!\n")
                    continuar6 = False
                elif login == login3:
                    print("\nVocê não pode alterar o seu nível de acesso!!\n")
                    continuar8 = False
                else:
                    continuar7 = True
                    while continuar7:
                        novoAcesso = input("\nNovo nível de acesso para o usuário:\nDigite 1 - Analista\nDigite 2 - Estagiário\n")
                        if novoAcesso == "1":
                            acesso = "analista"
                            continuar7 = False
                        elif novoAcesso == "2":
                            acesso = "estagiario"
                            continuar7 = False
                        else:
                            print("\nOpção Inválida!!\n")
                    valores = dicLogins[login3]
                    novaTupla=(valores[0],acesso)
                    dicLogins[login3] = novaTupla
                    salvarLogins(dicLogins)
                    listaLog4 = [login,dataTexto,"Alterou o Nivel de Acesso do Usuário: "+login3]
                    listaLOG.append(listaLog4)
                    log(listaLOG)
                    print("\nAlteração Realizada com Sucesso!!\n")
                    continuar = False
                    continuar6 = False
        elif desejo == "5":
            continuar = False
        else:
            print("\nOpção Inválida!!\n")

def abertura(listaInicial):
    """Função reconhecer todos os treinamentos já cadastrados (Retorna uma lista com todos os treinamentos cadastrados)."""
    tamanho = len(listaInicial)
    n = 0
    listaGeral = []
    if tamanho >= 8:
        while n < tamanho:
            lista = [listaInicial[n],listaInicial[n+1],listaInicial[n+2],listaInicial[n+3],listaInicial[n+4],listaInicial[n+5],listaInicial[n+6],listaInicial[n+7]]
            n += 8
            listaGeral.append(lista)  
    return listaGeral

def dicionario(listaGeral):
    """Função para criar um dicionário com todos os treinamentos já cadastrados (Retorna um dicionário com todos os treinamentos cadastrados)."""
    dic = {}
    for x in listaGeral:
        if x != ["","","","","","",""]:
            chave = x[0]
            matricula = x[1]
            curso = x[2]
            inicio = x[3]
            termino = x[4]
            cargaHoraria = x[5]
            cadastro = x[6]
            modificacao = x[7]
            tupla = (matricula,curso,inicio,termino,cargaHoraria,cadastro,modificacao)
            dic[chave] = tupla
    return dic 
        
def cadastroTreinamento(dic):
    """Função para cadastrar novos treinamentos (Permite Cadastro Manual ou Importar de uma Planilha que segue um Modelo Padrão)."""
    continuar2 = True
    continuar3 = True
    while continuar2:
        cadastro = input("\nComo você deseja realizar o cadastro?\nDigite 1 - Cadastro Manual de Treinamento\nDigite 2 - Importar Planilha de Treinamento\nDigite 3 - Retornar ao Menu Principal\n")
        if cadastro != "1" and cadastro != "2" and cadastro != "3":
            print("\nOpção Inválida\n")
        elif cadastro == "3":
            continuar2 = False
        elif cadastro == "1":
            matricula = input("Digite a Matrícula do Empregado: ")
            curso = input("Digite o Nome do Treinamento: ")
            inicio = input("Digite a Data de Início do Treinamento (Formato: DD/MM/AAAA): ")
            termino = input("Digite a Data de Término do Treinamento (Formato: DD/MM/AAAA): ")
            cargaHoraria = input("Digite a Carga Horária do Treinamento: ")
            chave = matricula+"-"+inicio
            teste = chave in dic
            if teste == True:
                continuar4 = True
                desejo = input("Já existe um cadastro para esse empregado nesta data, deseja atualizar com as novas informações?\nDigite 1 - Para Sim\nDigite 2 - Para Não\n")
                while continuar4:
                    if desejo == "1":
                        for h in listaGeral:
                            if h[0] == chave:
                                cadastro = h[6]
                                listaGeral.remove(h)
                                listaLog5 = [login,dataTexto,"Atualizou o Registro de um Treinamento, chave: "+chave]
                                listaLOG.append(listaLog5)
                                log(listaLOG)
                                continuar3 == True
                                continuar4 = False
                    if desejo == "2":
                        continuar3 = False
                        continuar4 = False
                    if desejo != "1" and desejo != "2":
                        print("\nOpção Inválida\n")
            else:
                cadastro = dataTexto
                listaLog6 = [login,dataTexto,"Cadastrou Manualmente um Treinamento, chave: "+chave]
                listaLOG.append(listaLog6)
                log(listaLOG)
                continuar3 == True
            if continuar3 == True:                
                modificacao = dataTexto
                tupla = (matricula,curso,inicio,termino,cargaHoraria,cadastro,modificacao)
                dic[chave]=tupla
                lista = [chave,matricula,curso,inicio,termino,cargaHoraria,cadastro,modificacao]
                listaGeral.append(lista)
                cripto(dic)
                print("\nCadastro Realizado com Sucesso!!\n")
                return dic
        elif cadastro == "2":
                print("\nInsira a planilha de importação (importartreinamento.csv) na mesma pasta do programa!\n")
                print("Caso o treinamento já esteja cadastrado, o sistema irá atualizar com as novas informações!!\n")
                continuar10 = True
                while continuar10:
                    escolha = input("Importar agora?\nDigite 1 - Para Importar Agora\nDigite 2 - Para Retornar ao Menu Anterior\n")
                    if escolha != "1" and escolha != "2":
                        print("\nOpção Inválida\n")
                    elif escolha == "2":
                        continuar2 = True
                        continuar10 = False
                    elif escolha == "1":
                        arq = open("importartreinamento.csv","r")
                        lista3 = arq.readlines()
                        lista2 = []
                        for x in lista3:
                            a = x.split(";")
                            if a != ["Matrícula (Apenas Número)","Curso","Data de Início (DD/MM/AAAA)","Data de Término (DD/MM/AAAA)","Carga Horária (Apenas Número)\n"] and a != ["","","","","\n"]:
                                if len(a)==5:
                                    string = ""
                                    for x in a[4]:
                                        if x != "\n":
                                            string = string+x
                                    a[4] = string
                                    chave = a[0]+"-"+a[2]
                                    teste = chave in dic
                                    if teste == True:
                                        for h in listaGeral:
                                            if h[0] == chave:
                                                cadastro = h[6]
                                                listaGeral.remove(h)
                                    else:
                                        cadastro = dataTexto
                                    modificacao = dataTexto
                                    lista1=[chave,a[0],a[1],a[2],a[3],a[4],cadastro,modificacao]
                                    listaGeral.append(lista1)
                        print("\nImportação Concluída com Sucesso!!\n")
                        dic2 = dicionario(listaGeral)
                        cripto(dic2)
                        listaLog7 = [login,dataTexto,"Importou uma Planilha de Treinamento."]
                        listaLOG.append(listaLog7)
                        log(listaLOG)
                        continuar10 = False
                        return dic2

def altera(listaGeral):
    """Função para alterar treinamentos já cadastrados (Permite alterar: matrícula, nome do curso, data de início, data de término e carga horária)."""
    continuar7 =  True
    while continuar7:
        matricula = input("Digite a Matrícula do Empregado Cadastrado: ")
        inicio = input("Digite a Data de Início do Treinamento Cadastrado(Formato: DD/MM/AAAA): ")
        chaveTeste= matricula+"-"+inicio
        teste = chaveTeste in dic
        if teste == True:
            dic.pop(chaveTeste)
            print("\nRegistro Encontrado!!\n")
            alteracao = input("O que você deseja alterar?\nDigite 1 - Para Matrícula\nDigite 2 - Para Curso\nDigite 3 - Para Data de Início\nDigite 4 - Para Data de Término\nDigite 5 - Para Carga Horária\nDigite 6 - Para Retornar ao Menu Principal\n")
            if alteracao == "1":
                novaMatricula = input("Digite a Nova Matrícula: \n")
                for t in listaGeral:
                    if chaveTeste == t[0]:
                        t[1] = novaMatricula
                        chave = novaMatricula+"-"+t[3]
                        t[0] = chave
                        modificacao = dataTexto
                        t[7] = modificacao
                        tupla=(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
                        dic[chave] = tupla     
                print("\nRegistro Alterado com Sucesso!!\n")
                cripto(dic)
                listaLog10 = [login,dataTexto,"Alterou o Registro de um Treinamento (Alteração de Matrícula), chave: "+chave]
                listaLOG.append(listaLog10)
                log(listaLOG)
                continuar7 =  False
            elif alteracao == "2":
                novoCurso = input("Digite o novo Nome do Curso: ")
                for t in listaGeral:
                    if chaveTeste == t[0]:
                        t[2] = novoCurso
                        chave = matricula+"-"+t[3]
                        t[0] = chave
                        modificacao = dataTexto
                        t[7] = modificacao
                        tupla=(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
                        dic[chave] = tupla
                print("\nRegistro Alterado com Sucesso!!\n")
                cripto(dic)
                listaLog11 = [login,dataTexto,"Alterou o Registro de um Treinamento (Alteração do Nome do Curso), chave: "+chave]
                listaLOG.append(listaLog11)
                log(listaLOG)
                continuar7 =  False
            elif alteracao == "3":
                novoInicio = input("Digite a Nova Data de Início (Formato: DD/MM/AAAA): ")
                for t in listaGeral:
                    if chaveTeste == t[0]:
                        t[3] = novoInicio
                        chave = matricula+"-"+t[3]
                        t[0] = chave
                        modificacao = dataTexto
                        t[7] = modificacao
                        tupla=(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
                        dic[chave] = tupla
                print("\nRegistro Alterado com Sucesso!!\n")
                cripto(dic)
                listaLog12 = [login,dataTexto,"Alterou o Registro de um Treinamento (Alteração da Data de Início), chave: "+chave]
                listaLOG.append(listaLog12)
                log(listaLOG)
                continuar7 =  False
            elif alteracao == "4":
                novoTermino = input("Digite a Nova Data de Término (Formato: DD/MM/AAAA): ")
                for t in listaGeral:
                    if chaveTeste == t[0]:
                        t[4] = novoTermino
                        chave = matricula+"-"+t[3]
                        t[0] = chave
                        modificacao = dataTexto
                        t[7] = modificacao
                        tupla=(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
                        dic[chave] = tupla
                print("Registro Alterado com Sucesso!!\n")
                cripto(dic)
                listaLog13 = [login,dataTexto,"Alterou o Registro de um Treinamento (Alteração da Data de Término), chave: "+chave]
                listaLOG.append(listaLog13)
                log(listaLOG)
                continuar7 =  False
            elif alteracao == "5":
                novaCarga = input("Digite a Nova Carga Horária: ")
                for t in listaGeral:
                    if chaveTeste == t[0]:
                        t[5] = novaCarga
                        chave = matricula+"-"+t[3]
                        t[0] = chave
                        modificacao = dataTexto
                        t[7] = modificacao
                        tupla=(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
                        dic[chave] = tupla
                print("\nRegistro Alterado com Sucesso!!\n")
                cripto(dic)
                listaLog14 = [login,dataTexto,"Alterou o Registro de um Treinamento (Alteração da Carga Horária), chave: "+chave]
                listaLOG.append(listaLog14)
                log(listaLOG)
                continuar7 =  False
            elif alteracao == "6":
                continuar7 =  False
            else:
                print("\nOpção Inválida\n")
            
        else:
            print("\nRegistro Não Encontrado!!\n")
            continuar8 = True
            while continuar8:
                desejo = input("Deseja Buscar Novamente?\nDigite 1 - Para Sim\nDigite 2 - Para Retornar ao Menu Principal\n")
                if desejo == "1":
                    continuar7 =  True
                    continuar8 = False
                elif desejo == "2":
                    continuar7 =  False
                    continuar8 = False
                else:
                    print("\nOpção Inválida\n") 

def buscar(listaGeral):
    """Função para realizar buscas no programa."""
    continuar9 = True
    while continuar9:
        busca = input("\nO que você deseja buscar?\nDigite 1 - Para os Imprimir todos os Treinamentos de um Empregado\nDigite 2 - Para os Imprimir todos os Empregados que Realizaram um Determinado Curso\n")
        if busca == "1":
            encontrado = False
            mat = input("Digite a Matrícula do Empregado: ")
            listaLog15 = [login,dataTexto,"Realizou uma Busca dos Treinamentos Realizados pelo Colaborador de Matrícula: "+mat]
            listaLOG.append(listaLog15)
            log(listaLOG)
            listaMat = []
            for t in listaGeral:
                if t[1] == mat:
                    print("Curso: ",t[2])
                    listaMat.append(t)
                    encontrado = True
            print("\n")
            continuar9 = False
            if encontrado == False:
                print("Não Há Treinamentos Cadastrados para essa Matrícula!!\n")
                continuar9 = False
        if busca == "2":
            encontrado2 = False
            curso = input("Digite o nome do Curso: ")
            listaLog17 = [login,dataTexto,"Realizou uma Busca de Todas as Matrículas que Realizaram o Curso: "+curso]
            listaLOG.append(listaLog17)
            log(listaLOG)
            listaCurso = []
            for i in listaGeral:
                if i[2] == curso:
                    print("Matrícula: ",i[1])
                    encontrado2 = True
                    listaCurso.append(i)
            print("\n")
            continuar9 = False
            if encontrado2 == False:
                print("Não Há Empregados que realizaram o curso procurado!!\n")
                continuar9 = False
                       
def elimina(listaGeral):
    """Função para excluir treinamentos já cadastrados."""
    continuar5 = True
    while continuar5:
        eliminaMat= input("Digite a Matrícula Empregado: ")
        eliminaData = input("Digite a Data de Início do Curso (Formato: DD/MM/AAAA): ")
        chaveTeste = eliminaMat+"-"+eliminaData
        if chaveTeste in dic:
            listaLog19 = [login,dataTexto,"Excluiu um Treinamento, chave: "+chaveTeste]
            listaLOG.append(listaLog19)
            log(listaLOG)
            print("\nTreinamento Excluído com Sucesso!!\n")     
            for t in listaGeral:
                if t[0] == chaveTeste:
                    listaGeral.remove(t)
            dic.pop(chaveTeste)
            cripto(dic)
        else:
            print("\nTreinamento Não Encontrado!\n")
            listaLog20 = [login,dataTexto,"Tentou excluir um Treinamento Não Cadastrado."]
            listaLOG.append(listaLog20)
            log(listaLOG)
        continuar6 = True
        while continuar6:
            desejo = input("Deseja excluir outro registro?\nDigite 1 - Para Excluir Outro Registro\nDigite 2 - Para Retornar ao Menu Principal\n")
            if desejo != "1" and desejo != "2":
                print("\nOpção Inválida\n")
            if desejo == "1":
                continuar5 = True
                continuar6 = False
            if desejo == "2":
                continuar6 = False
                continuar5 = False
                
def ordenar(listaGeral):
    """Função para ordernar todos os treinamentos realizados (Salva o arquivo "elementos.csv" de forma ordenada com base na matrícula)."""
    continuar = True
    while continuar:
        desejo = input("\nComo você deseja ordernar?\nDigite 1 - Ordenar Planilha de Treinamento por Número da Matrícula\nDigite 2 - Retornar ao Menu Principal\n")
        if desejo == "1":
            menor = 1
            novaLista = []
            tamanho = len(listaGeral)
            cont = 0
            while cont < tamanho:
                for i in listaGeral:
                    teste = int(i[1])
                    if menor == teste:
                        novaLista.append(i)
                        cont += 1
                menor +=1
            listaGeral = novaLista
            cripto(dic)
            relatorioOrdenado(listaGeral)
            print("\nArquivo Ordenado com Sucesso! Arquivo RelatoriosOrdenado.csv foi Salvo!\n")
            listaLog21 = [login,dataTexto,"Ordenou o arquivo Elementos."]
            listaLOG.append(listaLog21)
            log(listaLOG)
            return listaGeral
            continuar = False
        elif desejo == "2":
            continuar = False
        else:
            print("\nOpção Inválida\n")
            
def relatorioOrdenado(listaGeral):
    """Função para gerar um relatório como todos os treinamentos de forma ordenada(Salva no arquivo "RelatorioOrdenado.csv")."""
    arq = open("RelatorioOrdenado.csv","w")
    arq.write("Chave;")
    arq.write("Matrícula;")
    arq.write("Curso;")
    arq.write("Data de Início;")
    arq.write("Data de Término;")
    arq.write("Carga Horária;")
    arq.write("Data do Cadastro;")
    arq.write("Última Modificação;")
    arq.write("\n")
    for c in listaGeral:
        if len(c)==8 and c != ["","","","","","","",""]:
            chave = c[0]
            matricula = c[1]
            curso = c[2]
            inicio = c[3]
            termino = c[4]
            carga = c[5]
            cadastro = c[6]
            modificacao = c[7]
            arq.write(chave)
            arq.write(";")
            arq.write(matricula)
            arq.write(";")
            arq.write(curso)
            arq.write(";")
            arq.write(inicio)
            arq.write(";")
            arq.write(termino)
            arq.write(";")
            arq.write(carga)
            arq.write(";")
            arq.write(cadastro)
            arq.write(";")
            arq.write(modificacao)
            arq.write("\n")
    arq.close()
   
def relatorio(listaGeral):
    """Função para gerar um relatório como todos os treinamentos cadastrados(Salva no arquivo "RelatoriosElementos.csv")."""
    arq = open("RelatorioElementos.csv","w")
    arq.write("Chave;")
    arq.write("Matrícula;")
    arq.write("Curso;")
    arq.write("Data de Início;")
    arq.write("Data de Término;")
    arq.write("Carga Horária;")
    arq.write("Data do Cadastro;")
    arq.write("Última Modificação;")
    arq.write("\n")
    for c in listaGeral:
        if len(c)==8 and c != ["","","","","","","",""]:
            chave = c[0]
            matricula = c[1]
            curso = c[2]
            inicio = c[3]
            termino = c[4]
            carga = c[5]
            cadastro = c[6]
            modificacao = c[7]
            arq.write(chave)
            arq.write(";")
            arq.write(matricula)
            arq.write(";")
            arq.write(curso)
            arq.write(";")
            arq.write(inicio)
            arq.write(";")
            arq.write(termino)
            arq.write(";")
            arq.write(carga)
            arq.write(";")
            arq.write(cadastro)
            arq.write(";")
            arq.write(modificacao)
            arq.write("\n")
    arq.close()
    print("\nRelatório Gerado com Sucesso! Arquivo RelatoriosElementos.csv foi Salvo!\n")
    listaLog22 = [login,dataTexto,"Gerou um relatório com todos os elementos."]
    listaLOG.append(listaLog22)
    log(listaLOG)

dataAtual = datetime.now()
dataTexto = dataAtual.strftime("%d/%m/%Y %H:%M")
listaLOG = importaLog()
login = login()
dicLogins = dicionarioLogins()
tupla = dicLogins[login]
acesso = tupla[1]

listaInicial = descripto()
listaGeral = abertura(listaInicial)
dic = dicionario(listaGeral)
