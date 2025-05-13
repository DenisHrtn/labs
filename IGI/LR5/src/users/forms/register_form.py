from django import forms

from users.models import User, Customer


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm', 'is_customer', 'is_client']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        is_customer = cleaned_data.get("is_customer")
        is_client = cleaned_data.get("is_client")

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

        if commit:
            user.save()

        if user.is_customer:
            customer = Customer.objects.create(user=user)
            customer.save()

        return user
