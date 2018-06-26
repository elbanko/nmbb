from django.db import models

# Create your models here.
class LegalFields (models.Model):
    Litigation = models.BooleanField()
    Corporate = models.BooleanField()
    Real_Estate = models.BooleanField()
    Tax = models.BooleanField()
    Trusts_and_Estates = models.BooleanField()
    Employment = models.BooleanField()
    Environmental = models.BooleanField()
    Compliance = models.BooleanField()
    Regulatory = models.BooleanField()
    International = models.BooleanField()
    Other = models.BooleanField()

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LegalField(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Posting(models.Model):
    position_title = models.CharField(max_length=1000)
    client_name = models.CharField(max_length=1000)
    date = models.DateField(null=True, blank=True)
    states = models.ManyToManyField(State, blank=True, default='Alabama')
    position_state = models.CharField(max_length=2, null=True, blank=True)
    position_city = models.CharField(max_length= 200, null=True, blank=True)
    position_location = models.CharField(max_length=1000)
    position_description = models.TextField(max_length=100000)
    position_link = models.URLField(blank=True, null=True)
    posted_by = models.CharField(max_length=1000000, blank=True, null=True)
    legal_field = models.ManyToManyField(LegalField,  blank=True)
    legal_fields = models.ManyToManyField(LegalFields,  blank=True)
    accept_terms = models.BooleanField()

    def __str__(self):
        return self.position_title


class PrePosting(models.Model):
    position_title = models.CharField(max_length=1000)
    client_name = models.CharField(max_length=1000)
    date = models.DateField(null=True, blank=True, help_text='Enter as YYYY-MM-DD.')
    state = models.CharField(max_length=120, null=True, blank=True)
    states = models.ManyToManyField(State, blank=True)
    position_state = models.CharField(max_length=2, null=True, blank=True, help_text='Enter State Abbreviation.')
    position_city = models.CharField(max_length=200, null=True, blank=True)
    position_location = models.CharField(max_length=1000, blank=True, null=True, help_text='Enter as City, State Abbreviation.')
    position_description = models.TextField(max_length=100000, help_text='Expand the text box size by dragging the lower right corner.')
    position_link = models.URLField(blank=True, null=True)
    posted_by = models.CharField(max_length=1000000, null=True, blank=True, help_text='Leave blank.')
    legal_field = models.ManyToManyField(LegalField, blank=True)
    legal_fields = models.ManyToManyField(LegalFields, blank=True)
    accept_terms = models.BooleanField()

    def __str__(self):
        return self.position_title
