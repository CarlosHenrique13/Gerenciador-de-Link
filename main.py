from generector import *
from time import sleep

def Interface():
    print(f"""{'='*20} Menu {'='*20}
    ls Listar Conteudo
    cd Listar as classe que existe
    cd NOME para entra na classe
    new -c NOME para criar uma classe
    new -l NOME para cria link, nome da classe que pertence o link
    mont NOME para montar o Arquivo final
    save NOME para salvar o projeto
    load NOME para carrega o projeto
    """)

    # Variaveis de Armazenamento do Usuario
    classes = {}
    #comando = ['new -c programa','new -c Java','new -l programa','new -l Java','ls','cd Java','ls']

    # Variavel Temporal
    local = ''
    while True:
    #for c in comando:
        links = {}
        comando = str(input(f"{local}>> "))
        cod = comando.split(' ')
        #cod = c.split(' ')

        # Comandos com mais de uma entrada de dados
        if len(cod) >= 2:
            # Criar Classes
            if f"{cod[0]} {cod[1]}" == 'new -c':
                try:
                    if cod[2]:
                        try:
                            classes[cod[2]] = {}
                            print(f"classe {cod[2]} criada com Sucesso!!\n")
                        except:
                            print(f"Erro não foi possivel Criar a Classe {cod[2]}")

                    else:
                        print("Esta faltando Valores no Comando")
                except(IndexError):
                    print("Esta faltando Valores no Comando")
            # Criar Links para uma classe
            elif f"{cod[0]} {cod[1]}" == 'new -l':
                try:
                    if cod[2]:
                        try:
                            while True:
                                name = str(input("Nome para o Link: "))
                                link = str(input("Link: "))
                                if (name != None and link != None) and (name != '' and link != ''):
                                    classes[cod[2]][name] = link
                                    print(f"Link {name} Adiciona com Sucesso!\n")
                                    break
                                else:
                                    print("Valores Invalidos")
                        except:
                            print("Erro não foi possivel Criar o Link")
                    else:
                        print("Esta faltando Valores no Comando")
                except(IndexError):
                    print("Esta faltando Valores no Comando")
            # Voltar de uma Classe
            elif f"{cod[0]}" == 'cd':
                if cod[1] != '..':
                    local = cod[1]
                    print(f'Você foi para classes {cod[1]}\n')
                else:
                    local = ''
                    print(f'Você foi para Home \n')
            # Salvar o projeto
            elif f"{cod[0]}" == 'save':
                    print(cod[1],classes)
                    status = Save(cod[1],classes)
                    print(status)
            # Carregar o Arquivo
            elif f"{cod[0]}" == 'load':
                classes = Load(cod[1])


        # Comando sem entrada de dados
        elif len(cod) == 1:

            if f"{cod[0]}" == 'cd':
                try:
                    print("="*10," Classes ","="*10)
                    for clas in classes.keys():
                        print(clas)
                    print()
                except:
                    print('Erro Não foi possivel Mostra as Classe')

            elif f"{cod[0]}" == 'ls':
                try:
                    if local == '':
                        print("="*10," Classes ","="*10)
                        for clas in classes.keys():
                            print("-"*5,f" {clas} ","-"*5)
                            for linkr in classes[clas]:
                                print(f'- {linkr}')
                        print()
                    else:
                        for clas in classes[local].keys():
                            print(f'{clas} {"."*(30-len(clas))} {classes[local][clas]}')
                        print()

                except:
                    print("Erro não foi possivel listar o conteudo")



            elif cod[0] == 'exit':
                break

    print('Finalizando...')
    sleep(0.8)
    print("Finalizado.")

if __name__ == '__main__':
    Interface()

