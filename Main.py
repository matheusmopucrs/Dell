# main.py

from tournament import register_startups, run_tournament, show_results

def main():
    print("=== Bem‑vindo ao Startup Rush ===")
    startups = register_startups()
    input("\nPressione Enter para INICIAR o torneio…")
    all_startups = run_tournament(startups)
    show_results(all_startups)


if __name__ == "__main__":
    main()
