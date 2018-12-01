import pygal
from bugs.models import Bugs
from features.models import Features
from pygal.style import Style
from datetime import date, datetime, timedelta


custom_style=Style(
        background='transparent',
        plot_background='transparent',
        foreground='#53E89B',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        transition='400ms ease-in',
        colors=('red', 'orange', 'green'),

        value_font_size=30,
        legend_font_size=30,
        tooltip_font_size=30
    )


def BugsPieChart():

    status = Bugs.objects.filter(status='To Do').count()
    status1 = Bugs.objects.filter(status='Doing').count()
    status2 = Bugs.objects.filter(status='Done').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style)

    p_chart.add('To Do', status)
    p_chart.add('Doing', status1)
    p_chart.add('Done', status2)
    return p_chart.render()


def FeaturesPieChart():

    status = Features.objects.filter(status='To Do').count()
    status1 = Features.objects.filter(status='Doing').count()
    status2 = Features.objects.filter(status='Done').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style)

    p_chart.add('To Do', status)
    p_chart.add('Doing', status1)
    p_chart.add('Done', status2)
    return p_chart.render()


def BugsDailyStatus():
    print("first", date.today())
    test = Bugs.objects.filter(
        created_date__gte=datetime.now() - timedelta(days=1))
    print('second', test)


    status = Bugs.objects.filter(
        status='To Do', created_date__gte=datetime.now() - timedelta(days=1)).count()
    status1 = Bugs.objects.filter(
        status='Doing', created_date__gte=datetime.now() - timedelta(days=1)).count()
    status2 = Bugs.objects.filter(
        status='Done', created_date__gte=datetime.now() - timedelta(days=1)).count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style)

    p_chart.add('To Do', status)
    p_chart.add('Doing', status1)
    p_chart.add('Done', status2)
    return p_chart.render()
