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


class TeamData(models.Model):
    teamid = models.AutoField(primary_key=True, blank=True, null=False)
    team = models.TextField(blank=True, null=True)
    avg_age = models.FloatField(blank=True, null=True)  # This field type is a guess.
    possession = models.FloatField(blank=True, null=True)  # This field type is a guess.
    games = models.IntegerField(blank=True, null=True)
    gk_wins = models.IntegerField(blank=True, null=True)
    gk_ties = models.IntegerField(blank=True, null=True)
    gk_losses = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    shots_on_target = models.IntegerField(blank=True, null=True)
    goals_per_shot = models.FloatField(blank=True, null=True)  # This field type is a guess.
    goals_per_shot_on_target = models.FloatField(blank=True, null=True)  # This field type is a guess.
    average_shot_distance = models.FloatField(blank=True, null=True)  # This field type is a guess.
    npxg_per_shot = models.FloatField(blank=True, null=True)  # This field type is a guess.
    goals = models.IntegerField(blank=True, null=True)
    xg = models.FloatField(blank=True, null=True)  # This field type is a guess.
    goals_pens = models.IntegerField(blank=True, null=True)
    npxg = models.FloatField(blank=True, null=True)  # This field type is a guess.
    assists = models.IntegerField(blank=True, null=True)
    xg_assist = models.FloatField(blank=True, null=True)  # This field type is a guess.
    crosses = models.IntegerField(blank=True, null=True)
    corner_kicks = models.IntegerField(blank=True, null=True)
    sca = models.IntegerField(blank=True, null=True)
    sca_dribbles = models.IntegerField(blank=True, null=True)
    sca_shots = models.IntegerField(blank=True, null=True)
    sca_fouled = models.IntegerField(blank=True, null=True)
    sca_defense = models.IntegerField(blank=True, null=True)
    gca = models.IntegerField(blank=True, null=True)
    gca_dribbles = models.IntegerField(blank=True, null=True)
    gca_shots = models.IntegerField(blank=True, null=True)
    gca_fouled = models.IntegerField(blank=True, null=True)
    gca_defense = models.IntegerField(blank=True, null=True)
    tackles_att_3rd = models.IntegerField(blank=True, null=True)
    touches_mid_3rd = models.IntegerField(blank=True, null=True)
    touches_att_3rd = models.IntegerField(blank=True, null=True)
    touches_att_pen_area = models.IntegerField(blank=True, null=True)
    dribbles = models.IntegerField(blank=True, null=True)
    dribbles_completed = models.IntegerField(blank=True, null=True)
    gk_goals_against = models.IntegerField(blank=True, null=True)
    gk_shots_on_target_against = models.IntegerField(blank=True, null=True)
    gk_clean_sheets = models.IntegerField(blank=True, null=True)
    gk_psxg_net = models.FloatField(blank=True, null=True)  # This field type is a guess.
    gk_crosses = models.IntegerField(blank=True, null=True)
    gk_crosses_stopped = models.IntegerField(blank=True, null=True)
    gk_def_actions_outside_pen_area = models.IntegerField(blank=True, null=True)
    gk_avg_distance_def_actions = models.FloatField(blank=True, null=True)  # This field type is a guess.
    tackles_def_3rd = models.IntegerField(blank=True, null=True)
    tackles_mid_3rd = models.IntegerField(blank=True, null=True)
    dribble_tackles = models.IntegerField(blank=True, null=True)
    dribbled_past = models.IntegerField(blank=True, null=True)
    blocked_passes = models.IntegerField(blank=True, null=True)
    blocked_shots = models.IntegerField(blank=True, null=True)
    interceptions = models.IntegerField(blank=True, null=True)
    clearances = models.IntegerField(blank=True, null=True)
    touches_def_pen_area = models.IntegerField(blank=True, null=True)
    touches_def_3rd = models.IntegerField(blank=True, null=True)
    gk_passes_length_avg = models.FloatField(blank=True, null=True)  # This field type is a guess.
    passes = models.IntegerField(blank=True, null=True)
    passes_total_distance = models.IntegerField(blank=True, null=True)
    passes_progressive_distance = models.IntegerField(blank=True, null=True)
    passes_completed_short = models.IntegerField(blank=True, null=True)
    passes_short = models.IntegerField(blank=True, null=True)
    passes_completed_medium = models.IntegerField(blank=True, null=True)
    passes_medium = models.IntegerField(blank=True, null=True)
    passes_completed_long = models.IntegerField(blank=True, null=True)
    passes_long = models.IntegerField(blank=True, null=True)
    gk_passes_completed_launched = models.IntegerField(blank=True, null=True)
    gk_passes_launched = models.IntegerField(blank=True, null=True)
    pass_xa = models.FloatField(blank=True, null=True)  # This field type is a guess.
    assisted_shots = models.IntegerField(blank=True, null=True)
    passes_into_final_third = models.IntegerField(blank=True, null=True)
    passes_into_penalty_area = models.IntegerField(blank=True, null=True)
    crosses_into_penalty_area = models.IntegerField(blank=True, null=True)
    progressive_passes = models.IntegerField(blank=True, null=True)
    passes_offsides = models.IntegerField(blank=True, null=True)
    passes_blocked = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    miscontrols = models.IntegerField(blank=True, null=True)
    dispossessed = models.IntegerField(blank=True, null=True)
    passes_received = models.IntegerField(blank=True, null=True)
    ball_recoveries = models.IntegerField(blank=True, null=True)
    cards_yellow = models.IntegerField(blank=True, null=True)
    cards_red = models.IntegerField(blank=True, null=True)
    cards_yellow_red = models.IntegerField(blank=True, null=True)
    fouls = models.IntegerField(blank=True, null=True)
    fouled = models.IntegerField(blank=True, null=True)
    touches = models.IntegerField(blank=True, null=True)
    tackles = models.IntegerField(blank=True, null=True)
    tackles_won = models.IntegerField(blank=True, null=True)
    pens_won = models.IntegerField(blank=True, null=True)
    pens_conceded = models.IntegerField(blank=True, null=True)
    own_goals = models.IntegerField(blank=True, null=True)
    aerials_won= models.IntegerField(blank=True, null=True)
    aerials_lost = models.IntegerField(blank=True, null=True)
    manager = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'team_data'


class RadarData(models.Model):
    teamid = models.IntegerField(blank=True, primary_key=True)
    team = models.TextField(blank=True, null=True)
    discipline_score = models.FloatField(blank=True, null=True)
    passes_score = models.FloatField(blank=True, null=True)
    possession_score = models.FloatField(blank=True, null=True)
    defensive_score = models.FloatField(blank=True, null=True)
    attacking_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'radar_data'

class SankeyData(models.Model):
    teamid = models.AutoField(primary_key=True, blank=True)
    team = models.TextField(blank=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    loss = models.IntegerField(blank=True, null=True)
    team_strategy = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sankey_data'

class TeamRanking(models.Model):
    teamid = models.AutoField(primary_key=True, blank=True)
    team = models.TextField(blank=True, null=True)
    team_code = models.TextField(blank=True, null=True)
    points_2018 = models.FloatField(blank=True, null=True)
    points_2014 = models.FloatField(blank=True, null=True)
    points_2022 = models.FloatField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'team_ranking'


