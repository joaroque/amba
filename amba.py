import requests
import json
from os import system

class Amba():
	
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
		url_info = []
		url_info.append(user_name)
		url_info.append(repo_name)
		url_info.append(repo_full_name)
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
		for key,value in res.items():
			items.append(key)
			items.append(value)
		return items

	def get_author_name(self,user_name):
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

		text = f"""- **[{repo_name}]({self.url})** by [{author_name}](https://github.com/{user_name})  
		{desc}  
		![Stars](https://img.shields.io/github/stars/{repo_full_name}?style=flat-square)

	==================== Langs and scores ====================
		{lang}
"""
		with open('amba-repos/output.txt', '+a') as repo_details:
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
		git_command = fr"""git add ./amba-repos/output.txt
git commit -m "Adding another Awesome project"
git branch -M ambaBot
git remote add origin https://github.com/joaroque/awesome-made-by-angolans.git
git push -u origin main"""
		try:
			input(system(git_command))
			print("Proccess conclude now wait to manteiners merge your pull and update the details..\nThank you for being Awesome!")
		except Exception as erro:
			print('\n'+erro)

 

def main():
    banner = r"""
                 ___      .___  ___. .______        ___      
                /   \     |   \/   | |   _  \      /   \     
               /  ^  \    |  \  /  | |  |_)  |    /  ^  \    
              /  /_\  \   |  |\/|  | |   _  <    /  /_\  \   
             /  _____  \  |  |  |  | |  |_)  |  /  _____  \  
            /__/     \__\ |__|  |__| |______/  /__/     \__\ 
    
    Script que automatiza escrita de projectos em Awesom-made-by-angolans
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

	
if __name__ == '__main__':
	main()
