# torneio.py

import random
from Startup import Startup, EVENTS


class Battle:
    def __init__(self, s1: Startup, s2: Startup):
        self.s1 = s1
        self.s2 = s2
        self.done = False
        
        
def register_startups():
    startups = []
    while True:
        try:
            n = int(input("Quantas startups? (4, 6 ou 8) "))
            if n in (4, 6, 8):
                break
        except ValueError:
            pass
        print("  Entrada inválida. Digite 4, 6 ou 8.")

    for i in range(1, n + 1):
        name = input(f"#{i} Nome da startup: ").strip()
        slogan = input(f"#{i} Slogan: ").strip()
        year = input(f"#{i} Ano de fundação: ").strip()
        startups.append(Startup(name, slogan, year))
    return startups


def administer(self):
        print(f"\nBatalha: {self.s1.name} ({self.s1.score}) x {self.s2.name} ({self.s2.score})")
        applied = {self.s1.name: set(), self.s2.name: set()}

        for type, (description, _) in EVENTS.items():
            for startup in (self.s1, self.s2):
                if type not in applied[startup.name]:
                    resp = input(f"  {startup.name}: ocorreu '{description}'? (s/n) ").strip().lower() 
                    if resp == 's':
                        startup.apply_event(type)
                        applied[startup.name].add(type)

        print(f"  Placar pós‑eventos: {self.s1.name}={self.s1.score}, {self.s2.name}={self.s2.score}")

        if self.s1.score == self.s2.score:
            print("  EMPATE! Shark Fight (+2 pts aleatório)")
            winner = random.choice((self.s1, self.s2))
            winner.score += 2
            print(f"  → {winner.name} venceu o Shark Fight (+2 pts)!")
        else:
            winner = self.s1 if self.s1.score > self.s2.score else self.s2

        winner.score += 30
        print(f"  → {winner.name} vence a batalha e recebe +30 pts!\n")
        self.done = True
        return winner

def run_tournament(startups):
    round_num = 1
    participants = startups[:]

    while len(participants) > 1:
        print(f"\n=== Rodada {round_num} ({len(participants)} participantes) ===")
        random.shuffle(participants)

        battles = [Battle(participants[i], participants[i + 1])
                   for i in range(0, len(participants), 2)]

        while any(not b.done for b in battles):
            print("\nBatalhas pendentes:")
            for idx, b in enumerate(battles, 1):
                if not b.done:
                    print(f"  {idx}: {b.s1.name} x {b.s2.name}")
            choice = input("Selecione o número da batalha para administrar: ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(battles) and not battles[idx].done:
                    battles[idx].administer()

        participants = [b.s1 if b.s1.score > b.s2.score else b.s2 for b in battles]
        round_num += 1

    champion = participants[0]
    print(f"\n🏆 CAMPEÃ: {champion.name} – \"{champion.slogan}\"")
    return startups


def show_results(startups):
    print("\n=== Classificação Final ===")
    print(f"{'Startup':<20}{'Pts':<6}{'Pitches':<8}{'Bugs':<6}"
          f"{'Tração':<7}{'Inv.':<6}{'Fake':<6}")
    for s in sorted(startups, type=lambda x: x.score, reverse=True):
        print(f"{s.name:<20}{s.score:<6}{s.stats['pitch']:<8}"
              f"{s.stats['bugs']:<6}{s.stats['traction']:<7}"
              f"{s.stats['investor']:<6}{s.stats['fake_news']:<6}")
