import re

import hashid
import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/')
soup = BeautifulSoup(request.content, 'html5lib')
text = soup.get_text()

def hash_finder(text):
    pat = re.compile("[0-9a-zA-Z]{30,}")
    hassh = pat.findall(text)
    return hassh


achou = hash_finder(text)
lista_final={}

for i in achou:
    try:
        first = i
    except:
        first = None

    while True:
        try:
            gerar=[]
            print("-"*50)
            if first:
                h = first
            else:
                print('1')
                h = input(" HASH: ")

            temp= list(filter(None,gerar))
            gerar = temp

            if len(gerar)==0:
                print("\n Not Found.")
                nope = "Not Found"
                lista_final[nope] = i

            elif len(gerar)>2:
                print('2')
                gerar.sort()
                print("\nPossible Hashs:")
                print("[+] "+str(hashid.algorithms[gerar[0]]))
                print("[+] "+str(hashid.algorithms[gerar[1]]))

                anexa_lista2 = str(hashid.algorithms[gerar[0]])
                lista_final[i] = anexa_lista2

                print("\nLeast Possible Hashs:")
                for a in range(int(len(gerar))-2):
                    print("[+] "+str(hashid.algorithms[gerar[a+2]]))
            else:
                print('3')
                gerar.sort()
                print("\nPossible Hashs:")
                for a in range(len(gerar)):
                    print("[+] "+str(hashid.algorithms[gerar[a]]))
                    anexa_lista = str(hashid.algorithms[gerar[a]])
                    lista_final[i] = anexa_lista

            first = None
            break
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()

del lista_final["Not Found"]
print(lista_final)
