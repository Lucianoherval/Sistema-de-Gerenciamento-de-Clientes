# Sistema-de-Gerenciamento-de-Clientes

# 🛍️ Sistema de Gerenciamento de Clientes

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)](https://www.sqlite.org/)
[![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-1.10-orange.svg)](https://ttkbootstrap.readthedocs.io/)

Um sistema desktop completo para gestão de clientes com interface moderna e banco de dados integrado, desenvolvido em Python com Tkinter.

!![image](https://github.com/user-attachments/assets/51242374-6570-420f-b58a-ae76b5ccb525)
 <!-- Adicione uma imagem real do seu sistema aqui -->

## ✨ Funcionalidades Principais

- **Cadastro Completo**: Registre todos os dados do cliente (CPF, endereço, contato, etc.)
- **CRUD Integrado**: 
  - ✅ Criar novos clientes
  - 🔍 Pesquisar registros
  - ✏️ Editar informações
  - 🗑️ Excluir cadastros
- **Interface Intuitiva**: Design moderno com ttkbootstrap
- **Banco de Dados Seguro**: Armazenamento local com SQLite
- **Validação de Dados**: Proteção contra entradas inválidas
- **Relatório Instantâneo**: Visualização em tabela interativa

## 🚀 Como Executar

1. **Pré-requisitos**
   - Python 3.8+
   - Git (opcional)

2. **Instalação**
   ```bash
   # Clone o repositório
   git clone https://github.com/seu-usuario/gerenciador-clientes.git
   cd gerenciador-clientes

   # Crie um ambiente virtual (recomendado)
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows

   # Instale as dependências
   pip install -r requirements.txt

   # Execução
   python main.py

## 🛠️ Tecnologias Utilizadas
 - **Linguagem: Python 3**

 - **GUI: Tkinter + ttkbootstrap**

 - **Banco de Dados: SQLite3**

 - **Gerenciamento de Pacotes: pip**

# 📦 Estrutura do Banco de Dados
    ```bash
    # sql
    CREATE TABLE cliente (
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


## 🔮 Melhorias Futuras
 - **Implementar mascara para CPF/Telefone**

 - **Exportar dados para Excel/PDF**

 - **Sistema de login de usuários**

 - **Geração de relatórios estatísticos**

 - **Integração com API de CEP**

- **Backup automático do banco de dados**

  Feito com 🤪 por Luciano Herval | ⭐ Deixe sua estrela no repositório!
