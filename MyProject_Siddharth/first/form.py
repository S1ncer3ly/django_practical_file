from django import forms

class MyForm(forms.Form):
    member_id = forms.CharField(label='Member ID')
    member_email = forms.EmailField(label='Member Email')
    course = forms.CharField(label='Course')
    staff = forms.BooleanField(label='Staff', required=False)
