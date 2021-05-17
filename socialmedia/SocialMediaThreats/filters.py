import django_filters
from django_filters import DateFilter
import datetime

from .models import *

class ThreatsFilter(django_filters.FilterSet):
    class Meta:
        model = Threats
        fields = '__all__'
        exclude = ['name', 'date_created_threat', 'descriptionofthreat']

class MonthlyFilter(django_filters.FilterSet):
    class Meta:
        model = Threats
        
        fields = '__all__'
        exclude = ['name', 'descriptionofthreat']

    


        # today = datetime.date.today()
        #  MyModel.objects.filter(mydatefield__year=today.year,
        #                    mydatefield__month=today.month)
        