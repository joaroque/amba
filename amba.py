import requests
import json

def clear_url(url):
    link_parse = url[19:]
    a = link_parse.find("/")
    user_name = link_parse[:a]
    repo_name = link_parse[a+1:]
    repo_full_name = link_parse
    info = list()
    info.append(user_name)
    info.append(repo_name)
    info.append(repo_full_name)
    return info
    
def get_repo_desc(full_name):
    url = f"https://api.github.com/repos/{full_name}"
    r = requests.get(url).json()
    return r['description']

def show_info(repo_name, url, user_name, desc, repo_full_name):
    info = f"""
    - **[{repo_name}]({url})** by [Marco Pitra](https://github.com/{user_name})  
  {desc}  
  ![Stars](https://img.shields.io/github/stars/{repo_full_name}?style=flat-square)
    """
    return info
    
def write_file(info):
    file = open('projects.txt', 'a')
    file.writelines(info)
    file.close
    
def main():
    banner = """
                 ___      .___  ___. .______        ___      
                /   \     |   \/   | |   _  \      /   \     
               /  ^  \    |  \  /  | |  |_)  |    /  ^  \    
              /  /_\  \   |  |\/|  | |   _  <    /  /_\  \   
             /  _____  \  |  |  |  | |  |_)  |  /  _____  \  
            /__/     \__\ |__|  |__| |______/  /__/     \__\ 
    Script to automatize projects list in Awesom-made-by-angolans
    by: @joaroque        
    Example input: https://github.com/joaroque/awesome-made-by-angolans
    """
    
    print(banner)
    url = input("amba-> ")
    str(url)
    
    # Pegar nome do usuário, repositório e descrição do projecto
    info = clear_url(url)
    user_name = info[0]
    repo_name = info[1]
    repo_full_name = info[2]
    desc = get_repo_desc(repo_full_name)
    info = show_info(repo_name,url,user_name,desc,repo_full_name)
    write_file(info)
    print("_________________ O/_________________________________________")
    print(f"""
        Usuário: {user_name}
        Repositório: {repo_full_name}
        Descrição: {desc}
    """)

if __name__ == "__main__":
    main()


