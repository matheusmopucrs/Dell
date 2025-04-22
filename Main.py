# main.py

from tournament import register_startups, run_tournament, show_results

# Função principal que organiza o fluxo do torneio
# Chama a função para registrar as startups no torneio e armazena elas na variável 'startups'
# Executa o torneio, passando as startups registradas, e armazena os resultados na variável 'all_startups'
# Exibe os resultados finais do torneio
def main():
    print("=== Bem‑vindo ao Startup Rush ===")
    startups = register_startups()
    input("\nPressione Enter para INICIAR o torneio…")
    all_startups = run_tournament(startups)
    show_results(all_startups)

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()
