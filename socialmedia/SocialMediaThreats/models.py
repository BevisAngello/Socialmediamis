from django.forms import ModelForm, Textarea
from django.db import models
# Create your models here.
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
# from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
# from simple_history.models import HistoricalRecords

THREAT_CHOICES= [
    (' Electronic fraud', ' Electronic fraud'),
    ('Cyber harassment', 'Cyber harassment'),
    ('Revenge porn', 'Revenge porn'),
    ('Cyber stalking', 'Cyber stalking'),
    ('Phishing', 'Phishing'),

    ]

AWARENESS_CHOICES= [
    (' Radio Ads', ' Radio Ads'),
    ('Television', 'Television'),
    ('Social media Influencing', 'Social media Influencing'),
    ('Cyber education', 'Cyber education'),
    ('Phishing Awareness', 'Phishing Awareness'),

    ]
                 


class Threats(models.Model):
    name = models.CharField(max_length=100, blank=True)
    typeofsocialmediacrime= models.CharField(max_length=100, choices=THREAT_CHOICES, default= 'SELECT')
    descriptionofthreat = models.CharField(max_length=254)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100, null=True)
    date_created_threat = models.DateTimeField(auto_now_add=True)

    def yearreported(self):
        return self.date_created_threat.strftime('%Y')

    def monthreported(self):
        return self.date_created_threat.strftime('%B')

    
    

class Meta:
    db_table = "threatreporting"

class Techniques(models.Model):
    name_person_technique = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    name_of_technique = models.CharField(max_length=100, null=True) 
    descriptionoftechnique = models.CharField(max_length=254)
    date_created_technique = models.DateTimeField(auto_now_add=True)
    


class Meta:
    db_table = "techniques"

class Awareness(models.Model):
    name_person_awareness = models.CharField(max_length=100, blank=True)
    typeofawareness= models.CharField(max_length=100, choices=AWARENESS_CHOICES, default= 'SELECT')
    descriptionofawareness = models.CharField(max_length=254)
    date_createdawareness = models.DateTimeField(auto_now_add=True)
    

    

class Meta:
    db_table = "awareness"


# typeofawareness = models.CharField(max_length=100)
