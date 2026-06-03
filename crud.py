#cadastrar , ler, buscar, deletar 
#tem que ter isso para -->combustíveis(tipos,preço), clientes(id,cpf,nome,combustível que abasteceu,fentista e bomba)
#frentistas(nome, quantidade de vezes que abasteceu) ,bomba(númeração e tipos de combustível)

clientes = []
combustiveis = []
bombas = []
frentistas = []

#------------------Funções CLIENTES-----------------------------
#------------------criar clientes-------------------------------
def criar_cliente(cliente_novo):
            clientes.append(cliente_novo)
            return clientes
#------------------listarclientes-------------------------------
def listar_clientes(clientes):
         print(clientes)
#------------------DELETAR CLIENTES------------------------------
def deletar_clientes(cliente_deletado):
            clientes.remove(cliente_deletado)
            return clientes
#------------------Achar clientes-------------------------------
def achar_clientes(cliente_nemo):
    if cliente_nemo in clientes:
        print(f"'{cliente_nemo}' está na lista!")
    else:
        print("Cliente não encontrado.")

#------------------Funções COMBUSTIVEIS-------------------------
#------------------criar combustiveis-------------------------------
def criar_comb(c):
    combustiveis.append(c)
#------------------listarcombustiveis-------------------------------
def listar_comb():
    print(combustiveis)
#------------------DELETAR COMBUSTIVEIS------------------------------
def deletar_comb(c):
    if c in combustiveis:
        combustiveis.remove(c)
#------------------Achar combustiveis-------------------------------
def acha_comb(c):
    if c in combustiveis:
        print('tem', c)
    else:
        print('n achou')

#------------------Funções BOMBA--------------------------------
#------------------criar bomba-------------------------------
def add_bomba(num):
      bombas.append(num)
#------------------listarbomba-------------------------------
def ver_bombas():
      print(bombas)
#------------------DELETAR BOMBA------------------------------
def tira_bomba(num):
    if num in bombas:
       bombas.remove(num)
#------------------Achar bomba-------------------------------
def busca_bomba(num):
   if num in bombas: print('achou bomba')
   else: print('bomba n existe')

#------------------Funções FRENTISTA----------------------------
#------------------criar frentista-------------------------------
def cadastra_frentista(nome):
    frentistas.append(nome)
#------------------listarfrentista-------------------------------
def lista_frents():
    print(frentistas)
#------------------DELETAR FRENTISTA------------------------------
def demite_frentista(nome):
    if nome in frentistas:
        frentistas.remove(nome)
    else:
        print('ja foi demitido')
#------------------Achar frentista-------------------------------
def achar_frentista(nome):
    if nome in frentistas:
        print(f"{nome} ta ai")
    else:
        print('n vi')

while True:
    #----------------------Menu inicial -------------------------   
    print("*****Menu*****")
    print('escolha uma das categorias abaixo:')
    print("1->clientes")
    print("2->combustíveis")
    print("3->bomba")
    print("4->frentista")
    print("0->sair do sistema")
    escolha_menu = int(input("iai qual vc quer ?"))

    if escolha_menu == 0:
        print("falou!")
        break

    #--------------------MENU CLIENTE----------------------------
    if escolha_menu == 1:
        while True:
            print('vc escolheu a categoria clientes!!!')
            print('***menu_clientes***')          
            print('--->Opções')
            print('1.CADASTRO,2.LISTAR,3.DELETAR,4.BUSCAR,0.VOLTAR')
        #INPUT do user 
            escolha_cliente = int(input('qual sua escolha ?:'))      
            if escolha_cliente == 0:
                break
            elif escolha_cliente == 1:#cria cliente novo
                cliente_novo = input("qual o nome do cliente novo ?:")
                criar_cliente(cliente_novo)
            elif escolha_cliente == 2:#lista os clientes obv
                listar_clientes(clientes)
            elif escolha_cliente == 3 :#apaga algum ciente
                 cliente_deletado =input('qual o cliente que vc quer deletar?')
                 deletar_clientes(cliente_deletado)
            elif escolha_cliente == 4 :#acha um cliente
                cliente_nemo=input('qual o cliente que tu quer achar?:')
                achar_clientes(cliente_nemo)

    elif escolha_menu == 2:
    #--------------------MENU COMBUSTIVEL------------------------
        while True:
            print('categoria combustiveis')
            print('1.ADD 2.VER 3.APAGAR 4.BUSCAR 0.VOLTAR')
            op = int(input('escolha:'))
            if op == 0:
                break
            elif op == 1:#novo comb
                c = input('novo combustivel:')
                criar_comb(c)
            elif op == 2:#lista comb obv
                listar_comb()
            elif op == 3:#apaga algum comb
                c = input('apagar qual?')
                deletar_comb(c)
            elif op == 4:#acha comb
                c = input('buscar qual?')
                acha_comb(c)

    elif escolha_menu == 3:
    #--------------------MENU BOMBA------------------------------
        while True:
            print('bombas')
            print('1.ADD 2.LISTA 3.DELETA 4.BUSCA 0.VOLTAR')
            opt = int(input('oq qr fzr? '))
            if opt == 0:
                break
            elif opt == 1:#add bomba nova
                b = input('num da bomba:')
                add_bomba(b)
            elif opt == 2:#lista as bombas obv
                ver_bombas()
            elif opt == 3:#apaga a bomba
                b = input('tirar qual bomba?')
                tira_bomba(b)
            elif opt == 4:#acha bomba
                b = input('buscar bomba:')
                busca_bomba(b)

    elif escolha_menu == 4:
    #--------------------MENU FRENTISTA--------------------------
        while True:
            print('frentistas')
            print('1.NOVO 2.LISTAR 3.DEMITIR 4.BUSCAR 0.VOLTAR')
            e = int(input('vai:'))
            if e == 0:
                break
            elif e == 1:#contrata frentista
                f = input('nome:')
                cadastra_frentista(f)
            elif e == 2:#lista os mano
                lista_frents()
            elif e == 3:#demite alguem
                f = input('nome pra demitir:')
                demite_frentista(f)
            elif e == 4:#acha o mano
                f = input('procurar quem?')
                achar_frentista(f)