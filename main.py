import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox, ttk, END
import sqlite3

# Classe com funções básicas de manipulação do banco e dos widgets
class Funcoes:
    def limpar_tela(self):
        self.entry_cpf.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_inscricao_estadual.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_numero.delete(0, END)
        self.entry_bairro.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.entry_estado.set("")  # Limpa o combobox
        self.entry_telefone.delete(0, END)
        self.text_observacao.delete("1.0", END)

    def salvar(self):
        try:
            self.conectar_banco()

            # Tratamento para o campo "número"
            numero_texto = self.entry_numero.get().strip()
            numero = int(numero_texto) if numero_texto else 0

            dados = {
                'cpf': self.entry_cpf.get().strip(),
                'nome': self.entry_nome.get().strip(),
                'inscricao': self.entry_inscricao_estadual.get().strip(),
                'endereco': self.entry_endereco.get().strip(),
                'numero': numero,
                'bairro': self.entry_bairro.get().strip(),
                'cidade': self.entry_cidade.get().strip(),
                'estado': self.entry_estado.get().strip(),
                'telefone': self.entry_telefone.get().strip(),
                'observacao': self.text_observacao.get("1.0", END).strip()
            }

            if not dados['cpf'] or not dados['nome']:
                messagebox.showwarning('Atenção', 'CPF e Nome são obrigatórios!')
                return

            self.cursor.execute("""
                INSERT INTO cliente (cpf, nome, inscricao, endereco, numero,
                                       bairro, cidade, estado, telefone, observacao)
                VALUES (:cpf, :nome, :inscricao, :endereco, :numero,
                        :bairro, :cidade, :estado, :telefone, :observacao)
            """, dados)

            self.conn.commit()
            self.limpar_tela()
            self.carregar_clientes()  # Atualiza a Treeview
            messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')

        except ValueError as ve:
            messagebox.showerror('Erro', 'O campo número deve conter apenas números!')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao salvar cliente: {str(e)}')
        finally:
            self.desconectar_banco()

    def conectar_banco(self):
        try:
            self.conn = sqlite3.connect("database/clientes.db")
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao conectar ao banco: {str(e)}')

    def desconectar_banco(self):
        if hasattr(self, 'conn'):
            self.conn.close()

    def montar_tabelas(self):
        try:
            self.conectar_banco()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cliente (
                    cod INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf CHAR(11) NOT NULL,
                    nome CHAR(100) NOT NULL,
                    inscricao CHAR(11),
                    endereco CHAR(100),
                    numero INTEGER,
                    bairro CHAR(20),
                    cidade CHAR(20),
                    estado CHAR(2),
                    telefone CHAR(11),
                    observacao CHAR(100)
                )
            """)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao criar tabela: {str(e)}')
        finally:
            self.desconectar_banco()


# Classe principal da aplicação, que herda de Funcoes
class aplicacao(Funcoes):
    def __init__(self):
        self.root = root
        self.style = style
        self.tela_principal()
        self.frame_superior()
        self.labels_entry()
        self.caixa_de_texto()  # Agora usa frame_observacao e text_observacao
        self.frame_inferior()
        self.montar_tabelas()
        self.botoes()
        self.botoes_inferior()
        self.treeview()
        self.carregar_clientes()  # Carrega os dados na Treeview ao iniciar
        self.limpar_tela()
        root.mainloop()

    def tela_principal(self):
        self.root.title("Sistema de Gerenciamento de Clientes")
        self.root.geometry("1300x700")
        self.root.resizable(False, False)

    def frame_superior(self):
        self.frame_superior = tk.LabelFrame(self.root, text="Dados do Cliente", font=("Arial", 8, "bold"),
                                             borderwidth=2, relief="solid", width=800, height=300)
        self.frame_superior.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.frame_superior.grid_propagate(True)

    def labels_entry(self):
        # CPF/CNPJ:
        self.label_cpf = tk.Label(self.frame_superior, text="CPF/CNPJ:", font=("Arial", 8, "bold"))
        self.label_cpf.place(x=10, y=10)
        self.entry_cpf = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=20)
        self.entry_cpf.place(x=80, y=10)

        # Nome:
        self.label_nome = tk.Label(self.frame_superior, text="Nome:", font=("Arial", 8, "bold"))
        self.label_nome.place(x=250, y=10)
        self.entry_nome = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=100)
        self.entry_nome.place(x=300, y=10)

        # Inscrição estadual:
        self.label_inscricao_estadual = tk.Label(self.frame_superior, text="Inscrição Estadual:", font=("Arial", 8, "bold"))
        self.label_inscricao_estadual.place(x=930, y=10)
        self.entry_inscricao_estadual = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=20)
        self.entry_inscricao_estadual.place(x=1050, y=10)

        # Endereço:
        self.label_endereco = tk.Label(self.frame_superior, text="Endereço:", font=("Arial", 8, "bold"))
        self.label_endereco.place(x=10, y=50)
        self.entry_endereco = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=40)
        self.entry_endereco.place(x=80, y=50)

        # Número:
        self.label_numero = tk.Label(self.frame_superior, text="Número:", font=("Arial", 8, "bold"))
        self.label_numero.place(x=350, y=50)
        self.entry_numero = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=5)
        self.entry_numero.place(x=420, y=50)

        # Bairro:
        self.label_bairro = tk.Label(self.frame_superior, text="Bairro:", font=("Arial", 8, "bold"))
        self.label_bairro.place(x=480, y=50)
        self.entry_bairro = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=20)
        self.entry_bairro.place(x=530, y=50)

        # Cidade:
        self.label_cidade = tk.Label(self.frame_superior, text="Cidade:", font=("Arial", 8, "bold"))
        self.label_cidade.place(x=670, y=50)
        self.entry_cidade = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=20)
        self.entry_cidade.place(x=730, y=50)

        # Estado:
        self.label_estado = tk.Label(self.frame_superior, text="Estado:", font=("Arial", 8, "bold"))
        self.label_estado.place(x=870, y=50)
        self.entry_estado = ttk.Combobox(self.frame_superior,
                                         values=["SP", "RJ", "MG", "ES", "RS", "PR", "SC", "BA", "SE", "PE", "AL", "PB", "RN",
                                                 "CE", "PI", "MA", "PA", "AP", "AM", "RO", "RR", "TO", "GO", "DF"],
                                         font=("Arial", 6, "bold"), width=3)
        self.entry_estado.place(x=930, y=50)

        # Telefone:
        self.label_telefone = tk.Label(self.frame_superior, text="Telefone:", font=("Arial", 8, "bold"))
        self.label_telefone.place(x=980, y=50)
        self.entry_telefone = tk.Entry(self.frame_superior, font=("Arial", 8, "bold"), width=20)
        self.entry_telefone.place(x=1050, y=50)

    def caixa_de_texto(self):
        # Corrigindo o conflito de nomes: Frame e Text com nomes diferentes
        self.frame_observacao = tk.LabelFrame(self.frame_superior, text="Observação:", font=("Arial", 8, "bold"),
                                              borderwidth=2, relief="solid", width=900, height=150)
        self.frame_observacao.place(x=10, y=100)
        self.text_observacao = tk.Text(self.frame_observacao, font=("Arial", 8, "bold"), width=885)
        self.text_observacao.place(x=15, y=10, width=870, height=100)

    def botoes(self):
        # Botão Salvar:
        self.botao_salvar = tk.Button(self.frame_superior, text="Salvar", font=("Arial", 8, "bold"),
                                       width=10, height=1, command=self.salvar)
        self.botao_salvar.place(x=950, y=110)

        # Botão Alterar:
        self.botao_alterar = tk.Button(self.frame_superior, text="Alterar", font=("Arial", 8, "bold"),
                                        width=10, height=1, command=self.alterar_cliente)
        self.botao_alterar.place(x=1050, y=110)

        # Botão Limpar:
        self.botao_limpar = tk.Button(self.frame_superior, text="Limpar", font=("Arial", 8, "bold"),
                                       width=10, height=1, command=self.limpar_tela)
        self.botao_limpar.place(x=950, y=180)

        # Botão Excluir:
        self.botao_excluir = tk.Button(self.frame_superior, text="Excluir", font=("Arial", 8, "bold"),
                                       width=10, height=1, command=self.excluir_cliente)
        self.botao_excluir.place(x=1050, y=180)

    def frame_inferior(self):
        self.frame_inferior = tk.LabelFrame(self.root, text="Dados dos Clientes", font=("Arial", 8, "bold"),
                                            borderwidth=2, relief="solid", width=1480, height=300)
        self.frame_inferior.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_propagate(True)

    def botoes_inferior(self):
        self.label_pesquisa = tk.Label(self.root, text="O que você procura?", font=("Arial", 8, "bold"))
        self.label_pesquisa.place(x=10, y=630)
        self.entry_pesquisa = tk.Entry(self.root, font=("Arial", 8, "bold"), width=30)
        self.entry_pesquisa.place(x=10, y=650)
        self.botao_pesquisar = tk.Button(self.root, text="Pesquisar", font=("Arial", 8, "bold"),
                                         width=10, height=1, command=self.pesquisar_cliente)
        self.botao_pesquisar.place(x=200, y=650)

    def treeview(self):
        # Criação das scrollbars
        self.vertical_scrollbar = ttk.Scrollbar(self.frame_inferior, orient='vertical')
        self.horizontal_scrollbar = ttk.Scrollbar(self.frame_inferior, orient='horizontal')

        # Criação da Treeview com colunas consistentes com o banco
        self.produtos_treeview = ttk.Treeview(self.frame_inferior,
                                              columns=("cpf", "nome", "inscricao", "endereco", "numero",
                                                       "bairro", "cidade", "estado", "telefone", "observacao"),
                                              show="headings",
                                              xscrollcommand=self.horizontal_scrollbar.set,
                                              yscrollcommand=self.vertical_scrollbar.set)

        self.vertical_scrollbar.config(command=self.produtos_treeview.yview)
        self.horizontal_scrollbar.config(command=self.produtos_treeview.xview)

        # Configuração dos cabeçalhos
        self.produtos_treeview.heading("cpf", text="CPF/CNPJ")
        self.produtos_treeview.heading("nome", text="Nome")
        self.produtos_treeview.heading("inscricao", text="Inscrição")
        self.produtos_treeview.heading("endereco", text="Endereço")
        self.produtos_treeview.heading("numero", text="Número")
        self.produtos_treeview.heading("bairro", text="Bairro")
        self.produtos_treeview.heading("cidade", text="Cidade")
        self.produtos_treeview.heading("estado", text="Estado")
        self.produtos_treeview.heading("telefone", text="Telefone")
        self.produtos_treeview.heading("observacao", text="Observação")

        # Configuração das colunas
        for col in ("cpf", "nome", "inscricao", "endereco", "numero",
                    "bairro", "cidade", "estado", "telefone", "observacao"):
            self.produtos_treeview.column(col, width=100, minwidth=50)

        # Posicionamento dos elementos
        self.produtos_treeview.grid(row=0, column=0, sticky="nsew")
        self.vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        self.horizontal_scrollbar.grid(row=1, column=0, sticky="ew")
        self.frame_inferior.grid_rowconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(0, weight=1)

        # Vincula o duplo clique para selecionar o cliente e preencher os campos
        self.produtos_treeview.bind("<Double-1>", self.selecionar_cliente)

    def carregar_clientes(self):
        try:
            self.conectar_banco()
            self.cursor.execute("SELECT * FROM cliente")
            registros = self.cursor.fetchall()
            self.produtos_treeview.delete(*self.produtos_treeview.get_children())
            for registro in registros:
                # registro[0] = cod, [1]=cpf, [2]=nome, [3]=inscricao, [4]=endereco,
                # [5]=numero, [6]=bairro, [7]=cidade, [8]=estado, [9]=telefone, [10]=observacao
                self.produtos_treeview.insert('', END, iid=registro[0],
                                              values=(registro[1], registro[2], registro[3],
                                                      registro[4], registro[5], registro[6],
                                                      registro[7], registro[8], registro[9], registro[10]))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar clientes: {str(e)}")
        finally:
            self.desconectar_banco()

    def selecionar_cliente(self, event):
        selected = self.produtos_treeview.focus()
        if selected:
            valores = self.produtos_treeview.item(selected, 'values')
            # Preenche os campos com os dados do cliente selecionado
            self.entry_cpf.delete(0, END)
            self.entry_cpf.insert(0, valores[0])
            self.entry_nome.delete(0, END)
            self.entry_nome.insert(0, valores[1])
            self.entry_inscricao_estadual.delete(0, END)
            self.entry_inscricao_estadual.insert(0, valores[2])
            self.entry_endereco.delete(0, END)
            self.entry_endereco.insert(0, valores[3])
            self.entry_numero.delete(0, END)
            self.entry_numero.insert(0, valores[4])
            self.entry_bairro.delete(0, END)
            self.entry_bairro.insert(0, valores[5])
            self.entry_cidade.delete(0, END)
            self.entry_cidade.insert(0, valores[6])
            self.entry_estado.set(valores[7])
            self.entry_telefone.delete(0, END)
            self.entry_telefone.insert(0, valores[8])
            self.text_observacao.delete("1.0", END)
            self.text_observacao.insert("1.0", valores[9])

    def alterar_cliente(self):
        try:
            selected = self.produtos_treeview.focus()
            if not selected:
                messagebox.showwarning("Atenção", "Selecione um cliente para alterar")
                return
            cliente_cod = selected
            numero_texto = self.entry_numero.get().strip()
            numero = int(numero_texto) if numero_texto else 0
            dados = {
                'cpf': self.entry_cpf.get().strip(),
                'nome': self.entry_nome.get().strip(),
                'inscricao': self.entry_inscricao_estadual.get().strip(),
                'endereco': self.entry_endereco.get().strip(),
                'numero': numero,
                'bairro': self.entry_bairro.get().strip(),
                'cidade': self.entry_cidade.get().strip(),
                'estado': self.entry_estado.get().strip(),
                'telefone': self.entry_telefone.get().strip(),
                'observacao': self.text_observacao.get("1.0", END).strip(),
                'cod': cliente_cod
            }
            if not dados['cpf'] or not dados['nome']:
                messagebox.showwarning("Atenção", "CPF e Nome são obrigatórios!")
                return

            self.conectar_banco()
            self.cursor.execute("""
                UPDATE cliente
                SET cpf=:cpf, nome=:nome, inscricao=:inscricao, endereco=:endereco, numero=:numero,
                    bairro=:bairro, cidade=:cidade, estado=:estado, telefone=:telefone, observacao=:observacao
                WHERE cod=:cod
            """, dados)
            self.conn.commit()
            self.desconectar_banco()
            self.limpar_tela()
            self.carregar_clientes()
            messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar cliente: {str(e)}")
            self.desconectar_banco()

    def excluir_cliente(self):
        try:
            selected = self.produtos_treeview.focus()
            if not selected:
                messagebox.showwarning("Atenção", "Selecione um cliente para excluir")
                return
            cliente_cod = selected
            self.conectar_banco()
            self.cursor.execute("DELETE FROM cliente WHERE cod=?", (cliente_cod,))
            self.conn.commit()
            self.desconectar_banco()
            self.limpar_tela()
            self.carregar_clientes()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir cliente: {str(e)}")
            self.desconectar_banco()

    def pesquisar_cliente(self):
        try:
            termo = self.entry_pesquisa.get().strip()
            self.conectar_banco()
            query = "SELECT * FROM cliente WHERE cpf LIKE ? OR nome LIKE ?"
            self.cursor.execute(query, ('%' + termo + '%', '%' + termo + '%'))
            registros = self.cursor.fetchall()
            self.produtos_treeview.delete(*self.produtos_treeview.get_children())
            for registro in registros:
                self.produtos_treeview.insert('', END, iid=registro[0],
                                              values=(registro[1], registro[2], registro[3],
                                                      registro[4], registro[5], registro[6],
                                                      registro[7], registro[8], registro[9], registro[10]))
            self.desconectar_banco()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar cliente: {str(e)}")
            self.desconectar_banco()


root = tk.Tk()
style = Style(theme='superhero')
aplicacao()


