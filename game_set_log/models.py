from django.db import models

# Create your models here.
from django.db import models

class Opponent(models.Model):
    name = models.CharField(max_length=100, help_text="Opponent's full name")
    skill_level = models.CharField(
        max_length=50,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
            ("Pro", "Pro"),
        ],
        help_text="Opponent's estimated skill level"
    )
    play_style = models.CharField(
        max_length=100,
        help_text="Description of opponent's play style (e.g., aggressive baseliner, serve-and-volley)"
    )

    def __str__(self):
        return f"{self.name} ({self.skill_level})"


class TennisMatch(models.Model):
    opponent = models.ForeignKey(Opponent, on_delete=models.CASCADE, related_name="matches")
    match_date = models.DateField(help_text="Date when the match took place")
    result = models.CharField(
        max_length=20,
        choices=[
            ("Win", "Win"),
            ("Loss", "Loss"),
        ],
        help_text="Match result"
    )
    score = models.CharField(max_length=20, help_text="Final score (e.g., 6-3, 4-6, 7-6)")
    short_description = models.TextField(
        help_text="Brief match summary (e.g., 'Tough match, but won in the final set!')"
    )
    highlights = models.TextField(
        blank=True,
        null=True,
        help_text="Special highlights (e.g., 'Hit 5 aces, strong net play, saved 3 match points')"
    )
    tournament_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of the tournament (leave blank if not a tournament match)"
    )
    court_name = models.CharField(
        max_length=100,
        help_text="Name of the court where the match was played"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.match_date}: {self.result} vs {self.opponent.name} ({self.score})"