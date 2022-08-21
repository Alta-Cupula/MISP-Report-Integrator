import requests
import re
import hashid
from bs4 import BeautifulSoup


request = requests.get('https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/')
#request = requests.get('https://resecurity.com/blog/article/blackcat-aka-alphv-ransomware-is-increasing-stakes-up-to-25m-in-demands')
soup = BeautifulSoup(request.content, 'html5lib')
text = soup.get_text()

def hash_finder(text):
    pat = re.compile("[0-9a-zA-Z]{30,}")
    hassh = pat.findall(text)
    #print(hassh) #é uma lista
    return hassh

#print(soup.prettify())
    

achou = hash_finder(text)
#print(achou)
lista_final={}

for i in achou:
    #print("\n{}".format(i)) #Deixar
    try:
        first = i
        #print(first)
    except:
        first = None

    while True:
        try:
            jerar=[]
            print("-"*50)
            if first:
                h = first
            else:
                print('1')
                h = input(" HASH: ")

            #hashid.ADLER32(h); hashid.CRC16(h); hashid.CRC16CCITT(h); hashid.CRC32(h); hashid.CRC32B(h); hashid.DESUnix(h); hashid.DomainCachedCredentials(h); hashid.FCS16(h); hashid.GHash323(h); hashid.GHash325(h); hashid.GOSTR341194(h); hashid.Haval128(h); hashid.Haval128HMAC(h); hashid.Haval160(h); hashid.Haval160HMAC(h); hashid.Haval192(h); hashid.Haval192HMAC(h); hashid.Haval224(h); hashid.Haval224HMAC(h); hashid.Haval256(h); hashid.Haval256HMAC(h); hashid.LineageIIC4(h); hashid.MD2(h); hashid.MD2HMAC(h); hashid.MD4(h); hashid.MD4HMAC(h); jerar.append(hashid.MD5(h)); jerar.append(hashid.MD5APR(h)); jerar.append(hashid.MD5HMAC(h)); jerar.append(hashid.MD5HMACWordpress(h)); jerar.append(hashid.MD5phpBB3(h)); jerar.append(hashid.MD5Unix(h)); jerar.append(hashid.MD5Wordpress(h)); jerar.append(hashid.MD5Half(h)); jerar.append(hashid.MD5Middle(h)); jerar.append(hashid.MD5passsaltjoomla1(h)); jerar.append(hashid.MD5passsaltjoomla2(h)); jerar.append(hashid.MySQL(h)); hashid.MySQL5(h); hashid.MySQL160bit(h); hashid.NTLM(h); hashid.RAdminv2x(h); hashid.RipeMD128(h); hashid.RipeMD128HMAC(h); hashid.RipeMD160(h); hashid.RipeMD160HMAC(h); hashid.RipeMD256(h); hashid.RipeMD256HMAC(h); hashid.RipeMD320(h); hashid.RipeMD320HMAC(h); hashid.SAM(h); jerar.append(hashid.SHA1(h)); hashid.SHA1Django(h); hashid.SHA1HMAC(h); hashid.SHA1MaNGOS(h); hashid.SHA1MaNGOS2(h); hashid.SHA224(h); hashid.SHA224HMAC(h); jerar.append(hashid.SHA256(h)); jerar.append(hashid.SHA256s(h)); hashid.SHA256Django(h); hashid.SHA256HMAC(h); hashid.SHA256md5pass(h); hashid.SHA256sha1pass(h); hashid.SHA384(h); hashid.SHA384Django(h); hashid.SHA384HMAC(h); hashid.SHA512(h); hashid.SHA512HMAC(h); hashid.SNEFRU128(h); hashid.SNEFRU128HMAC(h); hashid.SNEFRU256(h); hashid.SNEFRU256HMAC(h); hashid.Tiger128(h); hashid.Tiger128HMAC(h); hashid.Tiger160(h); hashid.Tiger160HMAC(h); hashid.Tiger192(h); hashid.Tiger192HMAC(h); hashid.Whirlpool(h); hashid.WhirlpoolHMAC(h); hashid.XOR32(h); hashid.md5passsalt(h); hashid.md5saltmd5pass(h); hashid.md5saltpass(h); hashid.md5saltpasssalt(h); hashid.md5saltpassusername(h); hashid.md5saltmd5pass(h); hashid.md5saltmd5passsalt(h); hashid.md5saltmd5passsalt(h); hashid.md5saltmd5saltpass(h); hashid.md5saltmd5md5passsalt(h); hashid.md5username0pass(h); hashid.md5usernameLFpass(h); hashid.md5usernamemd5passsalt(h); hashid.md5md5pass(h); hashid.md5md5passsalt(h); hashid.md5md5passmd5salt(h); jerar.append(hashid.md5md5saltpass(h)); jerar.append(hashid.md5md5saltmd5pass(h)); jerar.append(hashid.md5md5usernamepasssalt(h)); jerar.append(hashid.md5md5md5pass(h)); jerar.append(hashid.md5md5md5md5pass(h)); jerar.append(hashid.md5md5md5md5md5pass(h)); jerar.append(hashid.md5sha1pass(h)); jerar.append(hashid.md5sha1md5pass(h)); jerar.append(hashid.md5sha1md5sha1pass(h)); jerar.append(hashid.md5strtouppermd5pass(h)); jerar.append(hashid.sha1passsalt(h)); jerar.append(hashid.sha1saltpass(h)); jerar.append(hashid.sha1saltmd5pass(h)); jerar.append(hashid.sha1saltmd5passsalt(h)); jerar.append(hashid.sha1saltsha1pass(h)); jerar.append(hashid.sha1saltsha1saltsha1pass(h)); jerar.append(hashid.sha1usernamepass(h)); jerar.append(hashid.sha1usernamepasssalt(h)); jerar.append(hashid.sha1md5pass(h)); jerar.append(hashid.sha1md5passsalt(h)); jerar.append(hashid.sha1md5sha1pass(h)); jerar.append(hashid.sha1sha1pass(h)); jerar.append(hashid.sha1sha1passsalt(h)); jerar.append(hashid.sha1sha1passsubstrpass03(h)); jerar.append(hashid.sha1sha1saltpass(h)); jerar.append(hashid.sha1sha1sha1pass(h)); jerar.append(hashid.sha1strtolowerusernamepass(h))
            jerar.append(hashid.MD5(h)); jerar.append(hashid.MD5APR(h)); jerar.append(hashid.MD5HMAC(h)); jerar.append(hashid.MD5HMACWordpress(h)); jerar.append(hashid.MD5phpBB3(h)); jerar.append(hashid.MD5Unix(h)); jerar.append(hashid.MD5Wordpress(h)); jerar.append(hashid.MD5Half(h)); jerar.append(hashid.MD5Middle(h)); jerar.append(hashid.MD5passsaltjoomla1(h)); jerar.append(hashid.MD5passsaltjoomla2(h)); jerar.append(hashid.MySQL(h)); jerar.append(hashid.SHA1(h)); hashid.SHA1Django(h); hashid.SHA1HMAC(h); hashid.SHA1MaNGOS(h); hashid.SHA1MaNGOS2(h); hashid.SHA224(h); hashid.SHA224HMAC(h); jerar.append(hashid.SHA256(h)); jerar.append(hashid.SHA256s(h)); hashid.SHA256Django(h); hashid.SHA256HMAC(h); hashid.SHA256md5pass(h); hashid.SHA256sha1pass(h); hashid.SHA384(h); hashid.SHA384Django(h); hashid.SHA384HMAC(h); hashid.SHA512(h); hashid.SHA512HMAC(h); hashid.XOR32(h); hashid.md5passsalt(h); hashid.md5saltmd5pass(h); hashid.md5saltpass(h); hashid.md5saltpasssalt(h); hashid.md5saltpassusername(h); hashid.md5saltmd5pass(h); hashid.md5saltmd5passsalt(h); hashid.md5saltmd5passsalt(h); hashid.md5saltmd5saltpass(h); hashid.md5saltmd5md5passsalt(h); hashid.md5username0pass(h); hashid.md5usernameLFpass(h); hashid.md5usernamemd5passsalt(h); hashid.md5md5pass(h); hashid.md5md5passsalt(h); hashid.md5md5passmd5salt(h); jerar.append(hashid.md5md5saltpass(h)); jerar.append(hashid.md5md5saltmd5pass(h)); jerar.append(hashid.md5md5usernamepasssalt(h)); jerar.append(hashid.md5md5md5pass(h)); jerar.append(hashid.md5md5md5md5pass(h)); jerar.append(hashid.md5md5md5md5md5pass(h)); jerar.append(hashid.md5sha1pass(h)); jerar.append(hashid.md5sha1md5pass(h)); jerar.append(hashid.md5sha1md5sha1pass(h)); jerar.append(hashid.md5strtouppermd5pass(h)); jerar.append(hashid.sha1passsalt(h)); jerar.append(hashid.sha1saltpass(h)); jerar.append(hashid.sha1saltmd5pass(h)); jerar.append(hashid.sha1saltmd5passsalt(h)); jerar.append(hashid.sha1saltsha1pass(h)); jerar.append(hashid.sha1saltsha1saltsha1pass(h)); jerar.append(hashid.sha1usernamepass(h)); jerar.append(hashid.sha1usernamepasssalt(h)); jerar.append(hashid.sha1md5pass(h)); jerar.append(hashid.sha1md5passsalt(h)); jerar.append(hashid.sha1md5sha1pass(h)); jerar.append(hashid.sha1sha1pass(h)); jerar.append(hashid.sha1sha1passsalt(h)); jerar.append(hashid.sha1sha1passsubstrpass03(h)); jerar.append(hashid.sha1sha1saltpass(h)); jerar.append(hashid.sha1sha1sha1pass(h)); jerar.append(hashid.sha1strtolowerusernamepass(h))
            temp= list(filter(None,jerar))
            jerar = temp

            if len(jerar)==0:
                print("\n Not Found.")
                nope = "Not Found"
                lista_final[nope] = i

            elif len(jerar)>2:
                print('2')
                jerar.sort()
                print("\nPossible Hashs:")
                print("[+] "+str(hashid.algorithms[jerar[0]]))
                print("[+] "+str(hashid.algorithms[jerar[1]]))

                anexa_lista2 = str(hashid.algorithms[jerar[0]])
                lista_final[i] = anexa_lista2

                print("\nLeast Possible Hashs:")
                for a in range(int(len(jerar))-2):
                    print("[+] "+str(hashid.algorithms[jerar[a+2]]))
            else:
                print('3')
                jerar.sort()
                print("\nPossible Hashs:")
                for a in range(len(jerar)):
                    print("[+] "+str(hashid.algorithms[jerar[a]]))
                    anexa_lista = str(hashid.algorithms[jerar[a]])
                    lista_final[i] = anexa_lista

            first = None
            break
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()

del lista_final["Not Found"]
print(lista_final)

