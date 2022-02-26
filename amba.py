import requests
import json
from os import system, mkdir, path


class Amba:

    def __init__(self, url):
        self.url = url

    def get_names(self):
        link = self.url[19:]
        # find "/" in URL
        # get username and repo_name in url
        f = link.find("/")

        # get user & repo name
        user_name = link[:f]
        repo_name = link[f+1:]
        repo_full_name = link

        # append all in list
        url_info = [user_name, repo_name, repo_full_name]
        return url_info

    def get_repo_desc(self):
        # get repo description

        # get repo_full_name in get_names()
        full_name = self.get_names()
        full_name = full_name[2]

        # example url = https://api.github.com/repos/joaroque/amba
        url = f"https://api.github.com/repos/{full_name}"
        # get response in json
        res = requests.get(url).json()
        # return in API repo description
        return res['description']

    def get_repo_lang(self):
        # get repo_full_name in get_names()
        full_name = self.get_names()
        full_name = full_name[2]

        url = f"https://api.github.com/repos/{full_name}/languages"
        res = requests.get(url).json()
        items = []
        for key, value in res.items():
            items.append(key)
            items.append(value)
        return items

    def get_author_name(self, user_name):
        # example url = https://api.github.com/users/joaroque
        url = f"https://api.github.com/users/{user_name}"
        res = requests.get(url).json()
        return res['name']

    def write_file(self):
        names = self.get_names()
        user_name = names[0]
        repo_name = names[1]
        repo_full_name = names[2]
        desc = self.get_repo_desc()
        lang = self.get_repo_lang()
        author_name = self.get_author_name(user_name)

        text = fr"""- **[{repo_name}]({self.url})** by [{author_name}](https://github.com/{user_name}) \
        {desc} \
        ![Stars](https://img.shields.io/github/stars/{repo_full_name}?style=flat-square)

    ==================== Langs and scores ====================
        {lang}
"""
        if not path.exists("amba-bin/amba-repos"):
            mkdir("amba-bin/amba-repos")
        with open('amba-bin/amba-repos/output.txt', 'w+') as repo_details:
            print(text, file=repo_details)

    def print_info(self):
        names = self.get_names()
        desc = self.get_repo_desc()
        lang = self.get_repo_lang()
        print(f"""
    _________________ O/_________________________________________
        USERNAME: {names[0]}
        REPOSITÓRIO: {names[1]}
        DESCRIÇÃO: {desc}
        LINGUAGEM(ENS) | PONTOS: {lang}
    _________________ O/_________________________________________
    """)

    def pull_request(self):
        print("Agora bora enviar os seus detalhes para o projeto principal..? (^_^)")
        git_command = "sh pull_request.sh"
        try:
            input(f"{system(git_command)}\n[!!] Para autenticar o seu PR Escreva (AmbaBot) e pressione ENTER\n\tEm seguida (awesomemadebyangolans1) e pressione ENTER..\n")
            print("\nProccesso concluido agora só resta esperar ate que os responsaveis aceitem e façam as atualizações dos seus detalhes..")
        except Exception as erro:
            print('\n'+erro)
        finally:
            print("Obrigado por ser Awesome!")
=======


def main():
    banner = r"""
                 ___      .___  ___. .______        ___      
                /   \     |   \/   | |   _  \      /   \     
               /  ^  \    |  \  /  | |  |_)  |    /  ^  \    
              /  /_\  \   |  |\/|  | |   _  <    /  /_\  \   
             /  _____  \  |  |  |  | |  |_)  |  /  _____  \  
            /__/     \__\ |__|  |__| |______/  /__/     \__\ 
    
    Script que automatiza escrita de projectos em Awesome-made-by-angolans
    Exemplo de entrada: https://github.com/joaroque/awesome-made-by-angolans
    by: https://github.com/joaroque
    """
    print(banner)
    url = str(input("Cole (digite) a url --> "))
    amba = Amba(url)
    amba.get_names()
    amba.get_repo_desc()
    amba.get_repo_lang()
    amba.write_file()
    amba.print_info()
    amba.pull_request()


if __name__ == '__main__':
    main()
