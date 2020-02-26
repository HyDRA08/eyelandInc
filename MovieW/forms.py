from django import forms

class FormLogin(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'UserName...','class':'loginform'}))
    password=forms.CharField(max_length=30,widget=
        forms.PasswordInput(attrs={'placeholder': 'Password...','class':'loginform'})
    )

class FormSignup(forms.Form):
    firstname=forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name...','class':'loginform'}))

    lastname=forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name...','class':'loginform'}))
    email=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'E mail...','class':'loginform'}))

    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'User Name...','class':'loginform'}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Password...','class':'loginform'}))
    confirm_password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...','class':'loginform'}))
    mobilenumber=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Mobile Number...','class':'loginform'}))
    # dob= forms.DateTimeField(
    #     input_formats=['%d/%m/%Y'],
    #     widget=forms.TextInput(attrs=
    #     {
    #         'class':'datepicker',
    #         'placeholder': 'Date of Birth...'

    #     }))

class FormSearchMovies(forms.Form):
    movie_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Search...'}))

