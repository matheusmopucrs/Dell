# eventos.py

EVENTS = {
    'pitch':       ('Pitch convincente',      +6),
    'bugs':        ('Produto com bugs',       -4),
    'traction':    ('Boa tração de usuários', +3),
    'investor':    ('Investidor irritado',    -6),
    'fake_news':   ('Fake news no pitch',     -8),
}


class Startup:
    def __init__(self, name, slogan, year):
        self.name = name
        self.slogan = slogan
        self.year = year
        self.score = 70
        self.stats = {k: 0 for k in EVENTS}

    def apply_event(self, event_key):
        desc, pts = EVENTS[event_key]
        self.score += pts
        self.stats[event_key] += 1

    def __str__(self):
        return f"{self.name} ({self.score} pts)"
