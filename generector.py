import os
import ast

def Load(name):
    """
    -> Carrega o Projeto
    :param name: Nome do Projeto
    :return: Status do Propjeto
    """
    if os.path.isfile(f'proj/{name}.txt'):
        arg = open(f'proj/{name}.txt','r')
        lines = arg.read()
        arg.close()
        return ast.literal_eval(lines)

def Save(name,value):
    """
    -> Salvar um projeto como racunho
    :param name: Nome do Arquivo
    :param value: Valor que sera Armazenado
    :return: Status do Arquivo
    """

    #Verificar se a pasta ja existe
    if not os.path.isdir("proj"):
        os.makedirs("proj")

    if not os.path.isfile(f"proj/{name}.txt"):
        arg = open(f"proj/{name}.txt",'w+')
        arg.write(f'{value}\n')
        arg.close()
        return "Arquivo Criado com Sucesso\n"
    else:
        while True:
            print("Você que salvar a alteração do arquivo? ")
            res = str(input('"S" para sim e "N" para não>>')).lower()
            if res == 'n':
                return "Arquivo não salvo!"
            elif res == 's':
                arg = open(f"proj/{name}.txt", 'w+')
                arg.write(f'{value}\n')
                arg.close()
                return "Arquivo Salvo com Sucesso\n"
            else:
                print("Não foi enviado uma respostar valida")


def MontFile(name,value,style):
    """
    -> Montar Arquivo Html
    :return:
    """

    def Mont(value,name):
        return f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{name}</title>
    <style>
    </style>
</head>
<body>
    
</body>
        """


    # Criar pasta de Origem do Arquivo
    if not os.path.isdir("links"):
        os.makedirs("links")
    # Montar o arquivo
    if os.path.isfile(f"links/{name}"):
        arg = open(f'links/{name}','w+')
        arg.write(Mont(value,name))
        arg.close()
        return f"Arquivo Criado com Sucesso. links/{name}.html\n"
    else:
        while True:
            print("Você que salvar a alteração do arquivo? ")
            res = str(input('"S" para sim e "N" para não>>')).lower()
            if res == 'n':
                return "Arquivo não salvo!"
            elif res == 's':
                arg = open(f'links/{name}','w+')
                arg.write(Mont(value,name))
                arg.close()
                return f"Arquivo Salvo com Sucesso. links/{name}.html\n"
            else:
                print("Não foi enviado uma respostar valida")
