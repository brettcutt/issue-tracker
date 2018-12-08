import pygal
from bugs.models import Bugs
from features.models import Features
from pygal.style import Style
from datetime import date, datetime, timedelta


custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#53E89B',
    foreground_strong='#53A0E8',
    foreground_subtle='#630C0D',
    transition='400ms ease-in',
    colors=('red', 'orange', 'green'),

    value_font_size=30,
    legend_font_size=20,
    tooltip_font_size=30,
    no_data_font_size=30
)


def chart_total(ticket_type):
    """Renders graphs by a tickets status.  """
    status = ticket_type.objects.filter(status='Waiting').count()
    status1 = ticket_type.objects.filter(status='In Progress').count()
    status2 = ticket_type.objects.filter(status='Completed').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style,
                        inner_radius=.5)

    p_chart.add('Waiting', status)
    p_chart.add('In Progress', status1)
    p_chart.add('Completed', status2)
    return p_chart.render()


def chart_by_time(ticket_type, amount_of_days):
    """Renders graphs by the amount of days in a specific ticket status """
    status = ticket_type.objects.filter(
        status='Waiting', waiting_date__gte=datetime.now() - timedelta(days=amount_of_days)).count()
    status1 = ticket_type.objects.filter(
        status='In Progress', in_progress_date__gte=datetime.now() - timedelta(days=amount_of_days)).count()
    status2 = ticket_type.objects.filter(
        status='Completed', completion_date__gte=datetime.now() - timedelta(days=amount_of_days)).count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style,
                        inner_radius=.5,
                        no_data_font_size=30,
                        no_data_text='No Recorded Data',
                        no_data_font_family='san-sarif')

    p_chart.add('Waiting', status)
    p_chart.add('In Progress', status1)
    p_chart.add('Completed', status2)
    return p_chart.render()


def BugsPieChart():
    chart = chart_total(Bugs)
    return chart


def BugsDailyStatus():
    chart = chart_by_time(Bugs, 1)
    return chart


def BugsWeeklyStatus():
    chart = chart_by_time(Bugs, 7)
    return chart


def BugsMonthlyStatus():
    chart = chart_by_time(Bugs, 30)
    return chart


def FeaturesPieChart():
    chart = chart_total(Features)
    return chart


def FeaturesDailyStatus():
    chart = chart_by_time(Features, 1)
    return chart


def FeaturesWeeklyStatus():
    chart = chart_by_time(Features, 7)
    return chart


def FeaturesMonthlyStatus():
    chart = chart_by_time(Features, 30)
    return chart
