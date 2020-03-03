import requests
import os

from PIL import Image
from io import BytesIO
from urllib.parse import urlparse


def image_name(url):
    pos = urlparse(url).path.split('/')
    name_split = pos[len(pos)-1].split('.')
    extension = name_split[len(name_split)-1]

    name_image = input("Digite o nome da imagem: ")
    
    return name_image + '.' + extension


def question_1(url):
    r = requests.get(url)

    print("\nValor URL: ", r.url)
    print("\nStatus Code: ", r.status_code)
    print("\nEncoding: ", r.encoding)
    #print("\nText: ", r.content)


def question_2(url):
    r = requests.get(url)
    
    if r.status_code == 200:
        save_name = image_name(url)
        img = Image.open(BytesIO(r.content))
        img = img.save(save_name)
        print("\nImagem Salva: ", save_name)
    
    else:
        print("\nProblema na URL")


def question_3():
    url = input("Digite a URL: ")
    r = requests.get(url)
    
    

if __name__ == "__main__":
    op = input("Selecione a Questao(1|2|3): ")
    url = input("Digite a URL: ")
    
    if (op == "1") :
        question_1(url)
    elif (op == "2") :
        question_2(url)
    elif (op == "3") :
        question_3()
    else :
        print ("Opcao invalida!!!")

   

# https://conteudo.imguol.com.br/c/carros/blogs/32/2018/08/31/citroen-c4-cactus-para-pcd-ja-pode-ser-encomendado-por-r-69990-1535734358325_v2_900x506.jpg
# https://i.dlpng.com/static/png/6440700_preview.png
