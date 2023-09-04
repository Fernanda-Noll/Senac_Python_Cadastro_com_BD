from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        global con
        con = mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
        )
    except Error as erro:
        print('Erro de conexão '+ erro)

def abririnfo():
    global tv
    try: 
        conectar()
        consulta_sql = "SELECT * FROM cliente"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            tv.insert('','end',values=(linha))
            print('Sucesso')
    except Error as erro:
        print('Erro ao abrir as informações '+ erro)

def inserir():
    try:
        conectar()
        nome = ent_nome.get()
        idade = ent_data_nascimento.get()
        sexo = ent_sexo.get()
        cidade = ent_cidade.get()
        inserir_clientes = f"""INSERT INTO cliente
                                (nomeCliente, dataNascimentoCliente, idSexo, idCidade)
                                VALUES
                                ("{nome}", "{idade}", {sexo}, {cidade})
                            """
        cursor = con.cursor()
        cursor.execute(inserir_clientes)
        con.commit()
        atualizar()
        #messagebox.showinfo(title='Informação', message='Informação cadastrada!')
        res = messagebox.askyesno('Limpar', 'Deseja limpar os valores da entrda')
        if(res==True):
            ent_nome.delete(0,END)
            ent_data_nascimento.delete(0,END)
            ent_sexo.delete(0,END)
            ent_cidade.delete(0,END)
        print(cursor.rowcount, 'registros inseridos na tabela!')
        cursor.close()
    except Error as erro:
        print('Falha ao inserir dadods MySQL: {}'.format(erro))
        messagebox.showerror(title='Erro', message='Errro ao cadastrar a informação!')
    finally:
            if(con.is_connected()):
                cursor.close()
                con.close()
                print('Conexão ao MySQL finalizada')

def deletar():
    try:
        conectar()
        id_controle=-1
        itemSelecionado = tv.selection()[0]     
        valores = tv.item(itemSelecionado,"values")
        id_controle=valores[0]
        deleta_cadastro = f'''DELETE FROM cliente WHERE idCliente = {id_controle}'''
        tv.delete(itemSelecionado)   
        cursor = con.cursor()
        cursor.execute(deleta_cadastro)
        con.commit() 
        #messagebox.showinfo(title='Informação', message='Informação deletada!')
        atualizar()
        res = messagebox.askyesno('Limpar', 'Deseja limpar os valores da entrda')
        if(res==True):
            ent_nome.delete(0,END)
            ent_data_nascimento.delete(0,END)
            ent_sexo.delete(0,END)
            ent_cidade.delete(0,END)
    except:
        messagebox.showerror(title='ERRO', message='Selecione uma opção para ser deletada!')
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL finalizada')        


def atualizar_registro():
    try:
        conectar()
        id_controle=-1
        itemSelecionado = tv.selection()[0]     
        valores = tv.item(itemSelecionado,"values")
        id_controle=valores[0]
        nome_novo = ent_nome.get()
        data_nascimento_novo = ent_data_nascimento.get()
        sexo_Novo = ent_sexo.get()
        cidade_novo = ent_cidade.get()

        atualizacao_cliente = f'''UPDATE cliente SET nomeCliente = '{nome_novo}', dataNascimentoCliente = '{data_nascimento_novo}' , idSexo =  {sexo_Novo}, idCidade = {cidade_novo}
                                WHERE idCliente = {id_controle} '''
        cursor = con.cursor()
        cursor.execute(atualizacao_cliente)
        con.commit()
        atualizar()
        res = messagebox.askyesno('Limpar', 'Deseja limpar os valores da entrda')
        if(res==True):
            ent_nome.delete(0,END)
            ent_data_nascimento.delete(0,END)
            ent_sexo.delete(0,END)
            ent_cidade.delete(0,END)

    except:
        messagebox.showerror(title='Erro', message='Errro ao atualizar a informação!\nPreencha todas as informações!')
        
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL finalizada')

def atualizar():
    try:
        conectar()
        tv.delete(*tv.get_children()) #Deleta a os dados do tv para depois atualizar com os dados atuais 
        consulta_sql = "SELECT * FROM cliente"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print('Numerdo de registros retornados: ', cursor.rowcount)

        print('\nMostrar os clientes cadastrados')
        for linha in linhas:
            tv.insert('','end',values=(linha))
        messagebox.showinfo(title='Informação', message='Informação atualizada!')

    except Error as erro:
        print('Falha ao acessar tabela MySQL: {}'.format(erro))
        messagebox.showerror(title='Erro', message='Errro ao atualizar a informação a informação!')

    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL finalizada')

janela = Tk()
janela.geometry('700x600')
janela.resizable(FALSE,FALSE )
janela.title = 'Cadastro de pessoa'

lb_nome = Label(janela,text='Nome')
ent_nome=Entry(janela)

lb_data_nascimento = Label(janela,text='Data Nascimento')
ent_data_nascimento=Entry(janela)

lb_sexo = Label(janela,text='Sexo')
ent_sexo=Entry(janela)

lb_cidade = Label(janela,text='Cidade')
ent_cidade=Entry(janela)

tv = ttk.Treeview(janela, columns=('idCliente','nome','dataNascimento','idSexo','idCidade'), show='headings')
tv.column('idCliente', minwidth=0,width=30)
tv.column('nome', minwidth=0,width=110)
tv.column('dataNascimento', minwidth=0,width=80)
tv.column('idSexo', minwidth=0,width=50)
tv.column('idCidade', minwidth=0,width=100)
tv.heading('idCliente', text='ID')
tv.heading('nome', text='NOME')
tv.heading('dataNascimento', text='DATA DE NASCIMENTO')
tv.heading('idSexo', text='SEXO')
tv.heading('idCidade', text='CIDADE')
tv.pack()
abririnfo()

btn_inserir = Button(janela, text='Inserir', command=inserir)
btn_deletar = Button(janela, text='Deletar', command=deletar)
btn_consultar = Button(janela, text='Atualizar Registro', command=atualizar_registro)
btn_atualizar = Button(janela, text='Atualizar', command=atualizar)


lb_nome.place(relx=0.10, rely= 0.01)
ent_nome.place(relx=0.10, rely= 0.05, relheight=0.05, relwidth=0.25)

lb_data_nascimento.place(relx=0.40, rely= 0.01)
ent_data_nascimento.place(relx=0.40, rely= 0.05, relheight=0.05, relwidth=0.15)

lb_sexo.place(relx=0.60, rely= 0.01)
ent_sexo.place(relx=0.60, rely= 0.05, relheight=0.05, relwidth=0.10)

lb_cidade.place(relx=0.75, rely= 0.01)
ent_cidade.place(relx=0.75, rely= 0.05, relheight=0.05, relwidth=0.15)

tv.place(relx=0.10, rely= 0.20, relheight=0.60, relwidth=0.80)

btn_inserir.place(relx=0.10, rely=0.85, relheight=0.05, relwidth=0.15)
btn_deletar.place(relx=0.30, rely=0.85, relheight=0.05, relwidth=0.15)
btn_consultar.place(relx=0.50, rely=0.85, relheight=0.05, relwidth=0.15)
btn_atualizar.place(relx=0.70, rely=0.85, relheight=0.05, relwidth=0.15)



mainloop()