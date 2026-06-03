#menu principal e loop de execução;
import crud
import utils

while True:
    print("\n*****Menu Posto Cerrado Nordeste*****")
    print("escolha uma categoria:")
    print("1->clientes")
    print("2->combustiveis")
    print("3->bomba")
    print("4->frentista")
    print("5->relatorio")
    print("0->sair")
    escolha_menu = utils.ler_int("iai qual vc quer? ")

    if escolha_menu == 0:
        print("falou!")
        break

    #-------------------- CLIENTE ----------------------------
    if escolha_menu == 1:
        while True:
            print("\n***menu clientes***")
            print("1.CADASTRO 2.LISTAR 3.DELETAR 4.BUSCAR 5.EDITAR 0.VOLTAR")
            e = utils.ler_int("qual sua escolha? ")
            if e == 0:
                break
            elif e == 1:
                crud.criar_cliente()
            elif e == 2:
                crud.listar_clientes()
            elif e == 3:
                crud.deletar_cliente()
            elif e == 4:
                crud.buscar_cliente()
            elif e == 5:
                crud.editar_cliente()

    #-------------------- COMBUSTIVEL ------------------------
    elif escolha_menu == 2:
        while True:
            print("\ncategoria combustiveis")
            print("1.ADD 2.VER 3.APAGAR 4.BUSCAR 0.VOLTAR")
            op = utils.ler_int("escolha: ")
            if op == 0:
                break
            elif op == 1:
                crud.criar_comb()
            elif op == 2:
                crud.listar_comb()
            elif op == 3:
                crud.deletar_comb()
            elif op == 4:
                crud.acha_comb()

    #-------------------- BOMBA ------------------------------
    elif escolha_menu == 3:
        while True:
            print("\nbombas")
            print("1.ADD 2.LISTA 3.DELETA 0.VOLTAR")
            opt = utils.ler_int("oq qr fzr? ")
            if opt == 0:
                break
            elif opt == 1:
                crud.add_bomba()
            elif opt == 2:
                crud.ver_bombas()
            elif opt == 3:
                crud.tira_bomba()

    #-------------------- FRENTISTA --------------------------
    elif escolha_menu == 4:
        while True:
            print("\nfrentistas")
            print("1.NOVO 2.LISTAR 3.DEMITIR 0.VOLTAR")
            f = utils.ler_int("vai: ")
            if f == 0:
                break
            elif f == 1:
                crud.cadastra_frentista()
            elif f == 2:
                crud.lista_frents()
            elif f == 3:
                crud.demite_frentista()

    #-------------------- RELATORIO --------------------------
    elif escolha_menu == 5:
        crud.relatorio_abastecimentos()
