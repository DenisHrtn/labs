import re

from django import forms

from users.models import User, Customer


from datetime import date
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")
    age = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm', 'is_customer', 'is_client']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
        if not re.match(email_regex, email):
            raise forms.ValidationError("Введите корректный адрес электронной почты.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        is_customer = cleaned_data.get("is_customer")
        is_client = cleaned_data.get("is_client")
        age = cleaned_data.get("age")

        if age:
            today = date.today()
            age = today.year - age.year - (
                (today.month, today.day) < (age.month, age.day)
            )
            if age < 18:
                raise forms.ValidationError("Вам должно быть не менее 18 лет для регистрации.")
        else:
            raise forms.ValidationError("Укажите дату рождения.")

        if is_customer and is_client:
            raise forms.ValidationError("Нельзя быть как заказчиком, так и клиентом!")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        user.is_customer = self.cleaned_data["is_customer"]
        user.is_client = self.cleaned_data["is_client"]
        user.age = self.cleaned_data["age"]

        if commit:
            user.save()

        if user.is_customer:
            Customer.objects.create(user=user)

        return user
