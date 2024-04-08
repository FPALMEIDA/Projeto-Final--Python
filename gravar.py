import csv
import tkinter as tk
from tkinter import messagebox
import os


def gravar_contato():

    if entry_nome.get() == "" or entry_fone.get() == "" or entry_email.get () == "":
        messagebox.showerror(title="ERRO ao gravar", message="Todos os campos devem ser preenchido")
    else:
        with open("dados.csv", "a", newline="") as arquivo_dados:
            escritor = csv.writer(arquivo_dados)
            escritor.writerow([entry_nome.get().strip(), entry_fone.get().strip(), entry_email.get().strip()])
            messagebox.showinfo("Sistema contatos", "Contato cadastrado com sucesso!")
            limpar_campos()
        ler_contatos()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_fone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome.focus_set()


def ler_contatos():
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        lista_contatos.delete(0, tk.END)# limpar a lista
        for linha in leitor:
            lista_contatos.insert("end", linha[0])






def buscar_contato_pelo_indice(indice_procurado):
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        contador_volta = 0
        for linha in leitor:
            if contador_volta == indice_procurado:
                entry_nome.insert(tk.END, linha[0])
                entry_fone.insert(tk.END, linha[1])
                entry_email.insert(tk.END, linha[2])
                break
            contador_volta = contador_volta + 1


def excluir_contato():

    resposta = messagebox.askokcancel("Deletar contato", "Deseja excluir o contato?")
    if resposta:
        with (open("dados.csv", "r") as arquivo_dados, open("temp.csv", "a", newline="") as arquivo_temp):
            leitor = csv.reader(arquivo_dados)
            escritor = csv.writer(arquivo_temp)

            i = 0
            for contato in leitor:
                if entry_nome.get() != contato[0] and entry_fone.get() != contato[1] and entry_email.get() != contato[2]:
                    escritor.writerow([contato[0], contato[1], contato[2]])


        os.remove("dados.csv")

        os.rename("temp.csv","dados.csv")
        messagebox.showinfo("Deletar contato", message="Contato deletado com sucesso!")

        limpar_campos()
        ler_contatos()

    else:
        messagebox.showinfo("Deletar contato", message="Operação cancelada pelo usuário!")




def obter_indice(event):
    indice = lista_contatos.curselection()[0]
    limpar_campos()
    buscar_contato_pelo_indice(indice)


janela = tk.Tk()
janela.title("Cadastro de usuário!")
janela.geometry("540x300")

label_nome = tk.Label(janela, text="Nome:")
label_fone = tk.Label(janela, text="Telefone:")
label_email = tk.Label(janela, text="E-mail:")
label_contatos = tk.Label(janela, text="Contatos")

entry_nome = tk.Entry(janela)
entry_fone = tk.Entry(janela)
entry_email = tk.Entry(janela)

button_gravar = tk.Button(text="Gravar Contato", command=gravar_contato)
button_excluir = tk.Button(text="Excluir", command=excluir_contato)

lista_contatos = tk.Listbox(janela, selectmode="single")
lista_contatos.bind("<<ListboxSelect>>", obter_indice)

label_nome.config(font=("Verdana", 12))
label_nome.place(x=10, y=10)
entry_nome.config(font=("Arial", 12))
entry_nome.place(x=10, y=40, width=250, height=30)

label_contatos.config(font=("Arial", 12))
label_contatos.place(x=320, y=10)

label_fone.config(font=("Arial", 12))
label_fone.place(x=10, y=80)
entry_fone.config(font=("Arial", 12))
entry_fone.place(x=10, y=110, width=250, height=30)

label_email.config(font=("Arial", 12))
label_email.place(x=10, y=150)
entry_email.config(font=("Arial", 12))
entry_email.place(x=10, y=180, width=250, height=30)

button_gravar.config(font=("Arial", 12))
button_gravar.place(x=10, y=230, width=250, height=60)

button_excluir.config(font=("Arial", 12))
button_excluir.place(x=280, y=230, width=250, height=60)

lista_contatos.config(font=("Arial", 12))
lista_contatos.place(x=280, y=40, width=250, height=170)

ler_contatos()





janela.mainloop()