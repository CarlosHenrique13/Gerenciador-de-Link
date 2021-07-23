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
        if os.path.isfile(f'proj/{name}.link'):
            arg = open(f'proj/{name}.link','r')
            lines = arg.read()
            arg.close()
            print(f"Arquivo {name}.link Carregado com Sucesso!\n")
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

    if not os.path.isfile(f"proj/{name}.link"):
        arg = open(f"proj/{name}.link",'w+')
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
                arg = open(f"proj/{name}.link", 'w+')
                arg.write(f'{value}\n')
                arg.close()
                return "Arquivo Salvo com Sucesso\n"
            else:
                print("Não foi enviado uma respostar valida")

def NewStyle(name):
    """
    -> Novos Styles
    :param name: Nome do novo estilos
    :return: Status do estilo
    """
    def MontStyle():
        """
        -> Montar o Novo Style
        :return: Dicionario com os comandos e styles
        """
        style = {}
        style['bg'] = str(input("Cor do Fundo da Pagina: "))
        style['bg1'] = str(input("Cor de Fundo do Cabeçalho: "))
        style['h1'] = str(input("Cor da letra do titulo H1: "))
        style['h2'] = str(input("Cor da letra do titulo H2: "))
        style['div'] = str(input("Cor do Fundo das Classes e dos Links: "))
        style['a'] = str(input("Cor do Link: "))
        style['a1'] = str(input("Cor do Link quando o mouse passar: "))
        #style[''] = str(input(""))
        return style


    value = MontStyle()
    if not os.path.isdir("proj"):
        os.makedirs("proj")

    if not os.path.isfile(f"proj/{name}.style"):
        arg = open(f"proj/{name}.style",'w+')
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
                arg = open(f"proj/{name}.style", 'w+')
                arg.write(f'{value}\n')
                arg.close()
                return "Arquivo Salvo com Sucesso\n"
            else:
                print("Não foi enviado uma respostar valida")

def LoadStyle(name):
    """
    -> Carregar o Arquivo de Dezine
    :param name: Nome do arquivo
    :return: Dicionario com os comandos de style
    """
    try:
        if os.path.isfile(f'proj/{name}.style'):
            arg = open(f'proj/{name}.style','r')
            lines = arg.read()
            arg.close()
            print(f"Arquivo {name}.style Carregado com Sucesso!\n")
            return ast.literal_eval(lines)
        else:
            print("Arquivo de dezaine não encontrado!!. Usando Arquivo Padrao")
            return 'defaut'
    except:
        print(f"Não foi possivel Carregado o Arquivo")

def MontStyle(name):
    """
    -> Montar o Style em CSS Final
    :param name: Nome do arquivo de style
    :return: style pronto para o html
    """
    styl = LoadStyle(name=name)
    style = '''
    <style>
        *{
            font-family: Arial, Helvetica, sans-serif;
            background-color: '''
    style+=f'{styl["bg"]};\n'
    style += '''
        }
        body{
            text-align: center;
            margin: auto;
        }
        section{
            margin: auto;
            width: 50%;
            height: 50%;
            background-color: '''
    style+=f'{styl["bg1"]};\n'
    style += '''
        }
        h1{
            color:'''
    style += f'{styl["h1"]};\n'
    style += '''
            background: none;
        }
        h2{
            color: '''
    style +=f'{styl["h2"]};\n'
    style += '''
            background: none;
        }
        h2:hover{
            font-size: 25px;
        }
        div{
            text-align: left;
            background-color: '''
    style += f'{styl["div"]};\n'
    style += '''
        }
        h3{
            text-indent: 0.5em;
            font-size: 23px;
            color: '''
    style += f'{styl["h2"]};\n'
    style += '''
            background: none;
        }
        h3:hover{
            background: none;
            font-size: 25px;
        }
        div#list{
            margin-top: -20px;
            background: none;
            text-indent: 1.5em;
            padding: 5px;
            text-align: left;
        }
        a{
            background: none;
            margin-top: 10px;
            display:block;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            color:  '''
    style += f'{styl["a"]};\n'
    style += '''
        }
        a:hover{
            color: '''
    style += f'{styl["a1"]};\n'
    style += '''
            font-size: 20px;
        }
    </style>'''
    return style



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

    def Mont(value,name,version,versao,user='Anonimo',style='defaut'):
        try:
            html = f'''
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>
{MontStyle(style)}
</head>
<body>
    <section>
        <h1>Gerenciador de Link</h1>
        <h2>Projeto {name}</h2>
        <div>'''
            for clas in value.keys():
                html += f'<h3>{clas}</h3>\n<div id="list">\n'
                for linkr in value[clas]:
                    html += f'<a href="{value[clas][linkr]}">{linkr}</a><br>\n'
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
        arg.write(Mont(value=value,name=name,version=version,versao=versao,user=user,style=style))
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
                arg.write(Mont(value=value,name=name,version=version,versao=versao,user=user,style=style))
                arg.close()
                return f"Arquivo Salvo com Sucesso. links/{name}.html\n"
            else:
                print("Não foi enviado uma respostar valida")
