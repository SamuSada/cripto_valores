from tkinter import *
import requests
from bs4 import BeautifulSoup


def actualizar_datos_bitcoin():
    cripto = 'bitcoin'
    url = f"https://crypto.com/price/es/bitcoin"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    dato1 = sopa.find('span', class_="chakra-text css-13hqrwd").text
    label1.config(text=dato1)
    print(f"Bitcoin = {dato1}")
    return dato1


def actualizar_datos_etherum():
    cripto = 'bitcoin'
    url = f"https://crypto.com/price/es/ethereum"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    dato1 = sopa.find('span', class_="chakra-text css-13hqrwd").text
    label2.config(text=dato1)
    print(f"Etherum = {dato1}")
    return dato1


def actualizar_datos_dogecoin():
    cripto = 'bitcoin'
    url = f"https://crypto.com/price/es/dogecoin"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    dato1 = sopa.find('span', class_="chakra-text css-13hqrwd").text
    label3.config(text=dato1)
    print(f"Dogecoin = {dato1}")
    return dato1


def refrescar_datos():
    label1.configure(text=actualizar_datos_bitcoin())
    label2.configure(text=actualizar_datos_etherum())
    label3.configure(text=actualizar_datos_dogecoin())


root = Tk()
root.title('Cripto Valores')
root.minsize(800, 600)
root.maxsize(800, 600)

# fuente
fuente = ("Courier 10 Pitch", 20, "bold")

# images
bitcoin_image = PhotoImage(file='images/bitcoin.png')
etherum_image = PhotoImage(file='images/etherum.png')
dogecoin_image = PhotoImage(file='images/dogecoin.png')

# Actualizar
# boton_actualizar = Button(root, text='ACTUALIZAR', command=lambda: [actualizar_datos_bitcoin(), actualizar_datos_etherum(), actualizar_datos_dogecoin()])
# boton_actualizar.pack(padx=10, pady=10)

# frame1 - principal
frame1 = Frame(root)
frame1.pack()

# Botones - frame1
boton1 = Button(frame1, image=bitcoin_image, command=actualizar_datos_bitcoin)
boton1.grid(row=0, column=0, padx=10, pady=10)
label1 = Label(frame1, font=fuente, width=15)
label1.grid(row=0, column=1, padx=10, pady=10)

boton2 = Button(frame1, image=etherum_image, command=actualizar_datos_etherum)
boton2.grid(row=1, column=0, padx=10, pady=10)
label2 = Label(frame1, font=fuente, width=15)
label2.grid(row=1, column=1, padx=10, pady=10)

boton3 = Button(frame1, image=dogecoin_image, command=actualizar_datos_dogecoin)
boton3.grid(row=2, column=0, padx=10, pady=10)
label3 = Label(frame1, font=fuente, width=15)
label3.grid(row=2, column=1, padx=10, pady=10)

refrescar_datos()
root.after(3000, refrescar_datos())

root.mainloop()
