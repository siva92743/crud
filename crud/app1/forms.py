from django.contrib.auth.forms import UserCreationForm

from app1.models import Login


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('name', 'age', 'address', 'email', 'contact_no')

