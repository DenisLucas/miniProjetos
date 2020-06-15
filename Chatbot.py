"""
Um robo que arruma seu cronograma
"""
import sqlite3

banco = sqlite3.connect('Chatbot.db')
cursor = banco.cursor()

correto = False
while correto == False:
    acao = input(print("Bom dia, Você deseja criar alterar ou apagar ou ver um evento?")).upper().split(" ")
    for palavras in acao:
        
        if palavras == "DELETAR" or "APAGAR" or "REMOVER" or "DESTRUIR":
                cursor.execute("""
                 SELECT * FROM EVENTOS;
            """)
                for linha in cursor.fetchall():
                    print(linha)

                print("qual deve ser deletado (escolha pelo numero/id)")
                deletar = int(input())
                cursor.execute("""
                   DELETE FROM EVENTOS
                   WHERE id = ?
                   """, (deletar,))

                banco.commit()
                correto = True
        
        elif palavras == "CRIAR":
            print("Qual é o titulo... descrição do evento que quer ser registrado")
            nome = input()
            print("me de a data")
            data = input()
            cursor.execute("""
            INSERT INTO EVENTOS(nome,data)
            VALUES(?,?)
            """, (nome, data))
            banco.commit()
            
            print("obrigado pelas informações")
            correto = True
        elif palavras == "ALTERAR":
            cursor.execute("""
                 SELECT * FROM EVENTOS;
            """)
            for linha in cursor.fetchall():
                print(linha)

            print("qual vai alterar(id/primeiro numero)")
            identificacao = input()
            print("me de a nova data")
            data = input()
            print("me de o novo titulo")
            titulo = input()
            cursor.execute("""
                UPDATE EVENTOS
                SET nome = ?, data = ?
                WHERE id = ?
                """, (titulo, data, identificacao))

            banco.commit()
            correto = True
        
        elif palavras == "VER":
            cursor.execute("""
                 SELECT * FROM EVENTOS;
            """)

            for linha in cursor.fetchall():
                print(linha)

            correto = True
        
        if correto == False:
            print("desculpe isso não é uma alternativa")
        
banco.close()