from django import forms
from .models import Client
from dobwidget import DateOfBirthWidget

class ClientsForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = "__all__"

        labels = {
            'fullname':'Your name',
            'sum_insured': 'Sum Insured',
            'dob': 'Date of Birth',
            'policy_type': 'Policy Type'
        }

        
        widgets = {
            'dob': DateOfBirthWidget(),
        }

    def __init__(self,*args,**kwargs):
        super(ClientsForm,self).__init__(*args,**kwargs)
        self.fields['policy_type'].empty_label = "Select"
 