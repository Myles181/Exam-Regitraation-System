from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32)
    reg_no = forms.CharField(label='Registration Number', max_length=32)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput())
    rpassword = forms.CharField(label='Re-enter Password', max_length=32, widget=forms.PasswordInput())
    phno = forms.CharField(label='Phone Number', max_length=32)

#CHOICES = [('student', 'examiner', 'admin')]
CHOICES = [('c1', 'Student'), ('c2', 'Examiner'), ('c3', 'Admin')]


class LoginForm(forms.Form):
    reg_no = forms.CharField(
        required=True,
        label='User Id',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password :',
        max_length=500,
        widget=forms.PasswordInput()
    )
    user = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
    )

