import pygal
from django.db.models import Max
from django.shortcuts import render
from bugs.models import Bugs
from features.models import Features
from graphs.graphs import BugsPieChart, BugsDailyStatus, BugsWeeklyStatus, BugsMonthlyStatus, FeaturesPieChart, FeaturesDailyStatus, FeaturesWeeklyStatus, FeaturesMonthlyStatus


def index(request):
    """ A view that displays the index page"""
    most_upvoted_bug = Bugs.objects.order_by('upvotes').last()
    most_upvoted_Feature = Features.objects.order_by('upvotes').last()

    bugs_status_total = BugsPieChart()
    bugs_status_daily = BugsDailyStatus()
    bugs_status_weekly = BugsWeeklyStatus()
    bugs_status_monthly = BugsMonthlyStatus()
    features_status_total = FeaturesPieChart()
    features_status_daily = FeaturesDailyStatus()
    features_status_weekly = FeaturesWeeklyStatus()
    features_status_monthly = FeaturesMonthlyStatus()

    return render(request, 'index.html', {'most_upvoted_bug': most_upvoted_bug,
                                          'most_upvoted_Feature':most_upvoted_Feature,
                                          'bugs_status_total': bugs_status_total,
                                          'bugs_status_daily': bugs_status_daily,
                                          'bugs_status_weekly': bugs_status_weekly,
                                          'bugs_status_monthly': bugs_status_monthly,
                                          'features_status_total': features_status_total,
                                          'features_status_daily': features_status_daily,
                                          'features_status_weekly': features_status_weekly,
                                          'features_status_monthly': features_status_monthly})
