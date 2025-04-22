# Startup.py

# Classe que representa uma Startup
class Startup:
    def __init__(self, name, slogan, year):
        self.name = name
        self.slogan = slogan
        self.year = year
        self.score = 70
        self.stats = {k: 0 for k in EVENTS}
        

# Aplica um evento à startup: aumenta o score e registra o evento no dicionário de stats
    def apply_event(self, event_type):
        description, pts = EVENTS[event_type]
        self.score += pts
        self.stats[event_type] += 1

 # Método para imprimir as informações básicas da startup
    def __str__(self):
        return f"({self.name} ({self.score} pts)"

# Dicionário que mapeia os tipos de eventos para suas descrições e pontos atribuídos
EVENTS = {
    'pitch':       ('Pitch convincente',      +6),
    'bugs':        ('Produto com bugs',       -4),
    'Tração':      ('Boa tração de usuários', +3),
    'investor':    ('Investidor irritado',    -6),
    'fake_news':   ('Fake news no pitch',     -8),
}

