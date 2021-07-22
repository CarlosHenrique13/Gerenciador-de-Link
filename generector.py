import os
import ast
from datetime import date


def Load(name):
    """
    -> Carrega o Projeto
    :param name: Nome do Projeto
    :return: Status do Propjeto
    """
    try:
        if os.path.isfile(f'proj/{name}.txt'):
            arg = open(f'proj/{name}.txt','r')
            lines = arg.read()
            arg.close()
            print(f"Arquivo {name}.txt Carregado com Sucesso!\n")
            return ast.literal_eval(lines)
    except:
        print(f"Não foi possivel Carregado o Arquivo")
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


def MontFile(name,value,versao,user='Anonimo',version='1.0',style='defaut'):
    """
    -> Montar o Arquivo HTML
    :param name: Nome do arquivo
    :param value: Conteudo do arquivo a ser armazenado(os links)
    :param versao: Versão da pagina que você criou
    :param user: Nome do Criado da pagina
    :param version: Versão do aplicativo que foi criada a pagina
    :param style: Desine da pagina (cores da pagina)
    :return: Status da Função (se foi possivel criar o arquivo ou atualizalo)
    """

    def Mont(value,name,version,versao,user):
        try:
            html = f'''
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>
</head>
<body>
    <section>
        <h1>Gerenciador de Link</h1>
        <h2>Projeto {name}</h2>
        <div>'''
            for clas in value.keys():
                html += f'<h3>{clas}</h3>\n<div id="list">\n'
                for linkr in value[clas]:
                    html += f'<a href="{linkr}">{value[clas][linkr]}</a><br>\n'
                html += '</div>'
            html += f'''
        </div>
    </section>
    <footer>
        <p>Data de Atualização: {date.today()}<br>
            &copy; {user}<br>
            Versão do projeto: {version}
        </p>
        <p>
            Criador do Codigo<br>
            &copy; Carlos Henrique A. Santos<br>
            Versão: {versao}
        </p>
    </footer>
</body>
</html>'''
            print(f"Arquivo {name}.html criado com Sucesso!!\n")
            return html.encode('utf-8')
        except:
            print(f"Erro em Montar o Arquivo {name}.html !!")

    name = name.strip(' ')
    # Criar pasta de Origem do Arquivo
    if not os.path.isdir("links"):
        os.makedirs("links")
    # Montar o arquivo
    if not os.path.isfile(f"links/{name}.html"):
        arg = open(f'links/{name}.html','wb+')
        arg.write(Mont(value=value,name=name,version=version,versao=versao,user=user))
        arg.close()
        return f"Arquivo Criado com Sucesso. links/{name}.html\n"
    else:
        while True:
            print("Você que salvar a alteração do arquivo? ")
            res = str(input('"S" para sim e "N" para não>>')).lower()
            if res == 'n':
                return "Arquivo não salvo!"
            elif res == 's':
                arg = open(f'links/{name}.html','wb+')
                arg.write(Mont(value=value,name=name,version=version,versao=versao,user=user))
                arg.close()
                return f"Arquivo Salvo com Sucesso. links/{name}.html\n"
            else:
                print("Não foi enviado uma respostar valida")
