import pygal
from django.shortcuts import render
from bugs.models import Bugs
from graphs.graphs import BugsPieChart, BugsDailyStatus, FeaturesPieChart


def index(request):
    """ A view that displays the index page"""
    bugs_status_chart = BugsPieChart()
    features_status_chart = FeaturesPieChart()
    bugs_daily_status = BugsDailyStatus()
    return render(request, 'index.html', {'bugs_status_chart': bugs_status_chart, 'BugsDailyStatus':BugsDailyStatus,
                                          'features_status_chart': features_status_chart})
