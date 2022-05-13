from tkinter import *
from tkinter import ttk
import settings
import csv
import codecs



root = Tk()
root.title("Alicuotas")
root.configure(bg="#004966")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)

def search_alicuota(a, b, c):
    if int(a) <= 0 or int(a)> 12:
        #insertar msgbox
        lista = list(b)
        if len(lista) != 4:
            pass #insertar msgbox
    elif int(a) > 0 and int(a) < 10:
        file_arba = f"ARBA0{a}{b}.txt"
        file_caba = f"CABA0{a}{b}.txt"
        file_cordoba = f"CORDOBA0{a}{b}.txt"
    elif int(a) >= 10 and int(a) <=12:
        file_arba = f"ARBA{a}{b}.txt"
        file_caba = f"CABA{a}{b}.txt"
        file_cordoba = f"CORDOBA{a}{b}.txt"    

    #Busca en archivo ARBA
    with open("padrones\\" + file_arba, "r") as f1:
        valor_arba=""
        csv_reader1 = csv.reader(f1, delimiter=";")
        
        for line in csv_reader1:
            if line[0] == str(c):
                valor_arba = line[1]
        label_alicuota.insert(END, f"   Alicuota ARBA: {valor_arba}%\n")
        f1.close()
    #Busca en archivo CABA
    with open("padrones\\" + file_caba, "r") as f2:
        valor_caba=""
        csv_reader2 = csv.reader(f2, delimiter=";")
        for line2 in csv_reader2:
            if line2[0] == str(c):
                valor_caba = line2[1]
        label_alicuota.insert(END, f"   Alicuota CABA: {valor_caba}%\n")
        f2.close()
    #Busca en archivo Córdoba
    with open("padrones\\" + file_cordoba, "r") as f3:
        valor_cordoba=""
        csv_reader3 = csv.reader(f3, delimiter=";")
        try:   
            for line3 in csv_reader3:
                if line3[0] == str(c):
                    valor_cordoba = line3[1]
            label_alicuota.insert(END, f"   Alicuota CORDOBA: {valor_cordoba}%\n")
        except:
            label_alicuota.insert(END, f"   Sin Alicuota para CORDOBA")       

 


top_frame = Frame (
        root,
        bg='black',
        width=settings.WIDTH,
        height=settings.height_per(28)
)
top_frame.place(x=0, y=0)

label_month = Label (
        top_frame,
        text= "Mes:",
        fg="White" ,
        bg="Black"      
)
label_month.place (x=36, y=4)

month_txtbox = ttk.Entry(
        top_frame,
        width= 4,
        justify="center"       
)
month_txtbox.place(x=84, y = 4)

year_txtbox = ttk.Entry(
        top_frame,
        width= 4,
        justify="center"    
)
year_txtbox.place(x=84, y= 26)

label_year = Label (
        top_frame,
        text= "Año:",
        fg="White" ,
        bg="Black"      
)
label_year.place (x=36, y=26)

cuit_txtbox = ttk.Entry(
        top_frame,
        width= 14,
        justify="center"   
)
cuit_txtbox.place(x=84, y= 48)

label_cuit = Label (
        top_frame,
        text= "CUIT:",
        fg="White" ,
        bg="Black"      
)
label_cuit.place (x=36, y=48)

search_button = Button(
        
        top_frame,
        text="Buscar",        
        command= lambda:search_alicuota(month_txtbox.get(),year_txtbox.get(),cuit_txtbox.get()),
        
       
)
search_button.place (x = 200, y = settings.height_per(28)//4)

label_alicuota = Text(
        root,
        fg="Black",
        bg="#c7c9c9",
        font=(12),
        height=10,
        width=300

        
)

label_alicuota.place (x= 0, y=100)

root.mainloop()

