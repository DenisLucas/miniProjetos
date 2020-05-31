print("give me your email")
email = input().strip()
usuario = email[:email.index("@")]
dominio = email[email.index("@")+1:]
print(f"seu email é {email} seu nome de usuario é {usuario} e seu dominio é {dominio}")

