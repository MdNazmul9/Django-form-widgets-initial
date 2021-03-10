from django import forms
# from django.forms import ModelForm
from .models import Consumer

class ConsumerForm(forms.ModelForm):
    commission = forms.IntegerField(initial=10)
    name = forms.CharField( required=True, 
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows":10,
                "column":30


            }
        ))
    class Meta:
        model = Consumer
        fields = ['name','title', 'commission']
 

class RawConsumerForm(forms.Form):
    name = forms.CharField()
    title = forms.CharField()
    commission = forms.IntegerField()



