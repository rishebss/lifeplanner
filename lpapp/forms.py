from django import forms
from .models import Appointment
from .models import Webinar
from .models import Team
# from .models import Review,Team


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['name','mail']     



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'phone', 'img'] 
