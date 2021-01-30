from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=200, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
    password = forms.CharField(label='Hasło', max_length=200, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))


class RegistryForm(forms.Form):
    first_name = forms.CharField(label='Imie', max_length=200, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
    last_name = forms.CharField(label='Nazwisko', max_length=200, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
    email = forms.EmailField(label='Email', max_length=200, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
    password = forms.CharField(label='Hasło', max_length=200, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
    password2 = forms.CharField(label='Powtórz hasło', max_length=200, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm mr-sm-2'}))
