from django import forms

# from myapp1.models import Musician, Album
from myapp1 import models

class MusicianForm(forms.ModelForm):

    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    instrument = forms.CharField(label="Instrument")
    class Meta:
        model = models.Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    name = forms.CharField(label="Album Name")
    release_datefield = forms.DateField(label="Release Date",widget = forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"
