from django import forms

# ModelForm: MenuForm
class MenuForm(forms.Form):
    item_name = forms.CharField(max_length = 200)
    category = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000)
