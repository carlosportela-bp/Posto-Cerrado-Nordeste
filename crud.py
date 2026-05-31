#cadastrar , ler, buscar, deletar 
#tem que ter isso para -->combustíveis(tipos,preço), clientes(id,cpf,nome,combustível que abasteceu,fentista e bomba)
#frentistas(nome, quantidade de vezes que abasteceu) ,bomba(númeração e tipos de combustível)
#----------------------Menu inicial -------------------------   
print("*****Menu*****")
print('escolha uma das categorias abaixo:')
print("1->clientes")
print("2->combustíveis")
print("3->bomba")
print("4->frentista")
escolha_menu = int(input("iai qual vc quer ?"))
clientes = []
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
#--------------------MENU CLIENTE----------------------------
if escolha_menu == 1:
    print('vc escolheu a categoria clientes!!!')
    print('***menu_clientes***')          
    print('--->Opções')
    print('1.CADASTRO,2.LISTAR,3.DELETAR,4.BUSCAR')
#INPUT do user 
    escolha_cliente = int(input('qual sua escolha ?:'))      
    if escolha_cliente == 1:#cria cliente novo
        cliente_novo = input("qual o nome do cliente novo ?:")
        criar_cliente(cliente_novo)
    elif escolha_cliente == 2:#lista os clientes obv
        listar_clientes(clientes)
    elif escolha_cliente ==3 :#apaga algum ciente
         cliente_deletado =input('qual o cliente que vc quer deletar?')
         deletar_clientes(cliente_deletado)
    else :#acha um cliente
        cliente_nemo=input('qual o cliente que tu quer achar?:')
        achar_clientes(cliente_nemo)


            

        
            