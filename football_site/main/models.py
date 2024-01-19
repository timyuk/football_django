from django.db import models

class Matches(models.Model):
    teamid = models.IntegerField(primary_key=True)
    country_home = models.TextField(blank=True, null=True)
    country_away = models.TextField(blank=True, null=True)
    score_home = models.TextField(blank=True, null=True)
    score_away = models.TextField(blank=True, null=True)
    flag_home = models.TextField(blank=True, null=True)
    flag_away = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    winner = models.IntegerField(blank=True, null=True)
    status_home = models.TextField(blank=True, null=True)
    status_away = models.TextField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'matches'

class MatchTeam(models.Model):
    teamid = models.IntegerField(primary_key=True)
    home_possession = models.IntegerField(blank=True, null=True)
    away_possession = models.IntegerField(blank=True, null=True)
    home_completed_passes = models.IntegerField(blank=True, null=True)
    home_attempted_pases = models.IntegerField(blank=True, null=True)
    away_completed_passes = models.IntegerField(blank=True, null=True)
    away_attempted_pases = models.IntegerField(blank=True, null=True)
    home_team = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'match_team_data'

class MatchData(models.Model):
    matchid = models.IntegerField(blank=True, null=False, primary_key=True)
    match = models.IntegerField(blank=True, null=True)
    match_time = models.DateTimeField(blank=True, null=True)
    home_team = models.TextField(blank=True, null=True)
    away_team = models.TextField(blank=True, null=True)
    home_xg = models.FloatField(blank=True, null=True)  # This field type is a guess.
    away_xg = models.FloatField(blank=True, null=True)  # This field type is a guess.
    score = models.TextField(blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    referee = models.TextField(blank=True, null=True)
    home_formation = models.TextField(blank=True, null=True)
    away_formation = models.TextField(blank=True, null=True)
    away_manager = models.TextField(blank=True, null=True)
    home_possession = models.IntegerField(blank=True, null=True)
    away_possession = models.IntegerField(blank=True, null=True)
    home_completed_passes = models.IntegerField(blank=True, null=True)
    home_attempted_pases = models.IntegerField(blank=True, null=True)
    away_completed_passes = models.IntegerField(blank=True, null=True)
    away_attempted_pases = models.IntegerField(blank=True, null=True)
    home_sot = models.IntegerField(blank=True, null=True)
    away_sot = models.IntegerField(blank=True, null=True)
    home_total_shots = models.IntegerField(blank=True, null=True)
    away_total_shots = models.IntegerField(blank=True, null=True)
    home_saves = models.IntegerField(blank=True, null=True)
    away_saves = models.IntegerField(blank=True, null=True)
    home_fouls = models.IntegerField(blank=True, null=True)
    away_fouls = models.IntegerField(blank=True, null=True)
    home_corners = models.IntegerField(blank=True, null=True)
    away_corners = models.IntegerField(blank=True, null=True)
    home_crosses = models.IntegerField(blank=True, null=True)
    away_crosses = models.IntegerField(blank=True, null=True)
    home_touches = models.IntegerField(blank=True, null=True)
    away_touches = models.IntegerField(blank=True, null=True)
    home_tackles = models.IntegerField(blank=True, null=True)
    away_tackles = models.IntegerField(blank=True, null=True)
    home_interceptions = models.IntegerField(blank=True, null=True)
    away_interceptions = models.IntegerField(blank=True, null=True)
    home_aerials_won = models.IntegerField(blank=True, null=True)
    away_aerials_won = models.IntegerField(blank=True, null=True)
    home_offsides = models.IntegerField(blank=True, null=True)
    away_offsides = models.IntegerField(blank=True, null=True)
    home_throw_ins = models.IntegerField(blank=True, null=True)
    away_throw_ins = models.IntegerField(blank=True, null=True)
    home_pass_accuracy = models.FloatField(blank=True, null=True)  # This field type is a guess.
    away_pass_accuracy = models.FloatField(blank=True, null=True)  # This field type is a guess.
    home_shots_on_target = models.FloatField(blank=True, null=True)  # This field type is a guess.
    away_shots_on_target = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'match_data'

