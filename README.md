# ecommerce

Sistema de vendas desenvolvido em Django para gerenciamento de clientes, produtos, vendas e avaliações.

🚀 Tecnologias

Django

Django REST Framework

Python

PostgreSQL (ou SQLite para testes)

📌 Modelos

Client: Clientes cadastrados (nome, CPF, email, data de nascimento).

Product: Produtos à venda (nome, categoria, preço, média de avaliações).

Sale: Registra vendas (cliente, produto, quantidade, data).

Avaliation: Permite avaliações de produtos (cliente, produto, nota, comentário, data).

⚡ Instalação

# Clone o repositório
git clone https://github.com/seu-usuario/sistema-vendas.git
cd sistema-vendas

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver

📡 API Endpoints

GET /clients/ - Lista clientes.

POST /clients/ - Cria cliente.

GET /products/ - Lista produtos.

POST /products/ - Adiciona produto.

GET /sales/ - Lista vendas.

POST /sales/ - Registra venda.

GET /avaliations/ - Lista avaliações.

POST /avaliations/ - Cria avaliação.

📜 Licença

MIT License. Sinta-se livre para usar e modificar!

