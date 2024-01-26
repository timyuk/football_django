from django.shortcuts import render
from main.models import Matches, MatchTeam, MatchData, TeamData, RadarData, TeamRanking, SankeyData
import pandas as pd
import json
# Create your views here.
def get_base_context(request, pagename):
    return {
        'pagename': pagename,
        'user': request.user,
    }


def index(request):
    context = get_base_context(request, 'index')
    context['games'] = {'rounds':[Matches.objects.filter(order__lte = 4).order_by('order'),
                        Matches.objects.filter(order__gte = 5, order__lte = 7).order_by('order'),
                        Matches.objects.filter(order__gte = 8, order__lte = 9).order_by('order'),
                        Matches.objects.filter(order__gte = 10, order__lte = 12).order_by('order'),
                        Matches.objects.filter(order__gte = 13).order_by('order')],
                        'all':json.dumps(list(Matches.objects.all().order_by('order').values()), default=str)}
    context['match_teams'] = json.dumps(list(MatchTeam.objects.all().values()), default=str)
    context['match_data'] = json.dumps(list(MatchData.objects.all().values()), default=str)
    context['team_data'] = json.dumps(list(TeamData.objects.all().values()), default=str)
    context['radar_data'] = json.dumps(list(RadarData.objects.all().values()), default=str)
    context['team_ranking'] = json.dumps(list(TeamRanking.objects.all().values()), default=str)
    context['sankey_data'] = json.dumps(list(SankeyData.objects.all().values()), default=str)

    return render(request, 'main/index.html', context)