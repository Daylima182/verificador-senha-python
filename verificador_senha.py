# Verificador de Segurança de Senha
# Primeiro projeto em Python para Cybersecurity

def analisar_senha(senha):
    print("\n--- ANÁLISE DE SEGURANÇA ---")
    
    pontos = 0
    
    # 1. Verifica tamanho mínimo
    if len(senha) >= 8:
        print("[✔] Tamanho adequado (pelo menos 8 caracteres)")
        pontos += 1
    else:
        print("[❌] Senha muito curta! Use pelo menos 8 caracteres.")

    # 2. Verifica se tem números
    if any(caractere.isdigit() for caractere in senha):
        print("[✔] Contém números")
        pontos += 1
    else:
        print("[❌] Adicione pelo menos um número")

    # 3. Verifica se tem letras maiúsculas
    if any(caractere.isupper() for caractere in senha):
        print("[✔] Contém letras maiúsculas")
        pontos += 1
    else:
        print("[❌] Adicione pelo menos uma letra maiúscula")

    # 4. Avaliação final
    print("\nResultado:")
    if pontos == 3:
        print("🟢 SENHA FORTE: Boa combinação para uso básico!")
    elif pontos == 2:
        print("🟡 SENHA MÉDIA: Pode melhorar adicionando os itens com [❌].")
    else:
        print("🔴 SENHA FRACA: Fácil de ser quebrada por dicionário ou força bruta!")

# Execução do programa
if __name__ == "__main__":
    senha_usuario = input("Digite uma senha para testar a segurança: ")
    analisar_senha(senha_usuario)
    