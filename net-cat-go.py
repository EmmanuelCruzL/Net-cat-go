#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import  sys
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def banner():
    
    print( bcolors.FAIL +("""     
    ----[Net-Cat-Go Admin Panel Finder]----        
    |   |\      _,,,---,,_         |
    |   /,`.-'`'    -.  ;-;;,_     |
    |  |,4-  ) )-,_..;\ (  `'-'    |  
    |  '---''(_/--'  `-'\_)        |
    |  zZzzZ...                    |
    |                              |
    ---[By  Rubickcuv /*/*/*/]---
-----------------------------------------------------------------------------
Ejemplo: Net-Cat-Go >> http(s)://ejemplo.com.ar """) + bcolors.WARNING  + ("""
-----------------------------------------------------------------------------""") + bcolors.ENDC)

def  convert_txt_to_list():
    lista = list()
    with open('directorys.txt','rb') as f:
        for x in f:
            lista.append(x.strip())
    return lista

def conver_list_to_txt(list,name):
    with open("{}.txt".format(name),"w") as f:
        wr  =csv.writer(f,delimiter="\n")
        wr.writerow(list)

def request(url):
    lista = convert_txt_to_list()
    posibles = list()
    with requests.get(url) as peticion:

        if peticion.status_code == 200:
            for x in lista:
                r = requests.get(f"{url}/{x}")
                print(bcolors.WARNING,f"[*] Probando {url}/{x}...")
                if r.status_code == 200:
                    print(bcolors.OKGREEN,f"[?] Posible directorio del admin [CODE: 200]: {url}/{x}")
                    posibles.append(r)
                elif r.status_code == 400:
                    print(bcolors.FAIL,f"[!] No existe dicho directorio [CODE: 404]: {url}/{x}")
        else:
            print(f"[!] La web {url} no funciona o introducio mal la url")
            sys.exit(1)
def main():
    banner()
    url = input(bcolors.OKBLUE +"[*] Net-Cat-Go  (url)>> ")
    posibles_admin = list(request(url))
    print(posibles_admin)
    print()
    opt = input("Desea guardarlo (Y/N)")
    if(opt.upper() == 'Y'):
        conver_list_to_txt(posibles_admin,url)


if __name__ == '__main__':
    main()