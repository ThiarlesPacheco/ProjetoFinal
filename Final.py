
# Objetivo: Criar um algorítimo para somar os casos de COVID-19 por cidades e estados dentro do Brasil.

class Estado():
    def __init__(self,nome,sigla):
        self.nome = nome
        self.sigla = sigla
        self.pais = 'Brasil'
        self.quantidade = 0


    def atualiza_casos(self,nova_qtd):
        self.quantidade += nova_qtd


    def diminui_casos(self,menos):
        self.quantidade -= menos


    def mostra_sigla(self):
        return self.sigla


    def __str__(self):
        return "..Nome: "+ self.nome.ljust(20) + "..Sigla: "+self.sigla.ljust(5)+ "..Pais: "+self.pais.ljust(10)+ "..Casos no Estado: "+str(self.quantidade).ljust(10)


class Cidade():
    def __init__(self,nome,estado):
        self.nome = nome
        self.estado = estado
        self.casos = 0

    
    def atualiza_casos_cidade(self,nova_qtd):
        self.casos += nova_qtd
        self.estado.atualiza_casos(nova_qtd)
    

    def diminui_casos_cidade(self, menos):
        self.casos -= menos
        self.estado.diminui_casos(menos)


    def __str__(self):
        return "..Nome: "+self.nome.ljust(15) + "..Casos na Cidade: "+str(self.casos).ljust(5)



listaestado = []
listacidade = []

def cadastrar_estado():
    estado = cadastro_de_estado()
    sigla = cadastro_de_sigla()
    listaestado.append(Estado(estado,sigla))


def cadastro_de_estado():
    while True:
        estado = str(input('Digite o nome do Estado: ')).upper()
        if estado.isnumeric():
            input('Erro...Não pode ser Numeros..[Enter]')
            continue
        if estado in [x.nome for x in listaestado]:
            input('Estado ja consta no cadastro.[Enter]')
        else:
            return estado


def cadastro_de_sigla():
    while True:
        sigla = str(input('Digite a Sigla do Estado: ')).upper()
        if sigla.isnumeric() or len(sigla) == 1 or len(sigla) > 2:
            input('Erro...Digite 2 letras e Não pode ser Numeros..[Enter] ')
            continue
        if sigla in [x.sigla for x in listaestado]:
            input('Sigla ja consta no cadastro..[Enter]')
        else:
            return sigla


def relatorio_estado():
    for i in listaestado:
        print(i)


def cadastrar_cidade():
    nome_cidade = cadastro_de_cidades()
    estado_escolhido = coloca()
    listacidade.append(Cidade(nome_cidade,estado_escolhido))

        
def cadastro_de_cidades():
    while True:
        cidade = str(input('Digite o nome da Cidade: ')).upper()
        if cidade.isnumeric():
            input('Erro...Não pode ser Numeros..[Enter]')
            continue
        if cidade in [x.nome for x in listacidade]:
            input('Estado ja consta no cadastro..[Enter]')
        else:
            return cidade
        
            
def casos_cidade():
    def ler_casos():
        while True:
            try:
                qtde = int(input("Digite a quantidade de casos na Cidade: "))
                if qtde >= 0:
                    return qtde
                else:
                    print("..Erro..A quantidade nao pode ser menor que 0..[Enter]")
            except: input('..Erro..Digite apenas numeros..[Enter]')
    cidade_escolhida = atualizar()
    cidade_escolhida.atualiza_casos_cidade(ler_casos())


def tira_casos():
    def tirar():
        while True:
            try:
                qtde = int(input("Digite a quantidade de melhoras Cidade: "))
                if qtde >= 0:
                    return qtde
                else:
                    print("..Erro..A quantidade nao pode ser menor que 0..[Enter]")
            except: input('..Erro..Digite apenas numeros..[Enter]')
    cidade_escolhida = atualizar()
    cidade_escolhida.diminui_casos_cidade(tirar())

    
def relatorio_cidade():
    for a in listacidade:
        print(a)


def atualizar():
    while True:
        relaciona()
        try:
            escolha =int(input('..Escolha: '))
            return listacidade[escolha]
        except: input('..Escolha incorreta..[Enter] ')
    

def relaciona():
    print('Escolha a cidade pelo indice.')
    try:
        for i,a in enumerate(listacidade):
            print(i,a)
        return listacidade
    except: input('..Erro..Escolha invalida..[Enter]')
    return relaciona()


def coloca():
    try:
        for x in range(len(listaestado)):
            print('..',x,'....',listaestado[x].mostra_sigla())
        return listaestado[int(input('Escolha o Indice: '))]
    except: input('..Erro..Escolha incorreta..[Enter]')
    return coloca()

    
while True:
    e = input('''

    0- Finalizar.
    1- Cadastrar Estado.
    2- Cadastrar Cidades.
    3- Relatorio de Estados.
    4- Relatorio de Cidades.
    5- Atualizar casos na Cidade.
    6- Escluir numero de casos na Cidade.
    
    Escolha: ''')

    if e == '0':
        break
    elif e == '1':
        cadastrar_estado()
    elif e == '2':
        cadastrar_cidade()
    elif e == '3':
        relatorio_estado()
    elif e == '4':
        relatorio_cidade()
    elif e == '5':
        casos_cidade()
    elif e == '6':
        tira_casos()
    else:
        input('..Erro! Opção invalida..')