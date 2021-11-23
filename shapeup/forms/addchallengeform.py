from django import forms

class AddChallenge(forms.Form):
    start = forms.BooleanField(required=False)#initial=False, required=False,  widget=forms.RadioSelect(attrs={'class':'img'})
