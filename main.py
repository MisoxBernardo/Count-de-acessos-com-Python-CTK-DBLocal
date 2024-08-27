# main.py

import customtkinter as ctk
from sqlalchemy.orm import sessionmaker
from models import User, engine

# Configuração da sessão do banco de dados
Session = sessionmaker(bind=engine)

# Função de login
def login_user(username, password):
    session = Session()

    # Tenta encontrar o usuário com as credenciais fornecidas
    user = session.query(User).filter_by(username=username, password=password).first()

    if user:
        # Incrementa o contador de acessos
        user.access_count += 1
        session.commit()
        return f"Login bem-sucedido! Contagem de acessos: {user.access_count}"
    else:
        return "Credenciais inválidas!"

# Função chamada pelo botão de login
def on_login_click():
    username = entry_username.get()
    password = entry_password.get()
    result = login_user(username, password)
    label_result.config(text=result)

# Configuração da interface gráfica
app = ctk.CTk()
app.title("Login")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Input para o nome de usuário
label_username = ctk.CTkLabel(app, text="Username")
label_username.pack(padx=10, pady=(10, 0))

entry_username = ctk.CTkEntry(app)
entry_username.pack(padx=10, pady=10)

# Input para a senha
label_password = ctk.CTkLabel(app, text="Password")
label_password.pack(padx=10, pady=(10, 0))

entry_password = ctk.CTkEntry(app, show="*")
entry_password.pack(padx=10, pady=10)

# Botão de login
button_login = ctk.CTkButton(app, text="Login", command=on_login_click)
button_login.pack(padx=10, pady=10)

# Label para exibir o resultado do login
label_result = ctk.CTkLabel(app, text="")
label_result.pack(padx=10, pady=10)

# Iniciar a interface
app.mainloop()
