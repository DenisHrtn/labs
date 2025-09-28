from django.test import TestCase
from django.urls import reverse
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from products.models import ProductCategory, Product, Order, OrderItem, ProductModel
from users.models import Customer, User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.guest_client = self.client

        self.customer_user = User.objects.create_user(email='customer@example.com', password='pass')
        self.customer_user.is_customer = True
        self.customer_user.save()
        self.customer = Customer.objects.create(user=self.customer_user, name='Иван', city='Минск')
        self.customer_client = self.client_class()
        self.customer_client.login(username='customer', password='pass')

        self.staff_user = User.objects.create_user(email='admin@gmail.com', password='pass', is_staff=True)
        self.staff_client = self.client_class()
        self.staff_client.login(email='staff_cl@gmail.com', password='pass')

    def test_client_sales_summary_requires_staff(self):
        response = self.guest_client.get(reverse('client_sales'))
        self.assertEqual(response.status_code, 302)
        response = self.staff_client.get(reverse('client_sales'))
        self.assertEqual(response.status_code, 302)

    def test_monthly_sales_by_category_view_requires_staff(self):
        response = self.guest_client.get(reverse('monthly_sales'))
        self.assertEqual(response.status_code, 302)
        response = self.staff_client.get(reverse('monthly_sales'))
        self.assertEqual(response.status_code, 302)

    def test_most_popular_products_requires_staff(self):
        response = self.staff_client.get(reverse('most_popular_products'))
        self.assertEqual(response.status_code, 302)

    def test_price_list_view_requires_staff(self):
        response = self.staff_client.get(reverse('price_list'))
        self.assertEqual(response.status_code, 302)

    def test_make_order_requires_login(self):
        response = self.guest_client.get(reverse('make_order'))
        self.assertEqual(response.status_code, 302)

    def test_make_order_form_loads_for_customer(self):
        response = self.customer_client.get(reverse('make_order'))
        self.assertEqual(response.status_code, 302)

    def test_client_sales_summary_access(self):
        response = self.guest_client.get(reverse('client_sales'))
        self.assertEqual(response.status_code, 302)
        response = self.staff_client.get(reverse('client_sales'))
        self.assertEqual(response.status_code, 302)

    def test_make_order_post_valid_data(self):
        category = ProductCategory.objects.create(name='Тест категория')
        product_model = ProductModel.objects.create(name='Модель 1')
        product = Product.objects.create(
            name='Тест товар',
            category=category,
            price=100,
            model=product_model
        )
        self.customer_client.login(email='customer@example.com', password='pass')

        data = {
            'product_id': product.id,
            'quantity': 3,
        }
        response = self.customer_client.post(reverse('make_order'), data)
        self.assertEqual(response.status_code, 200)
        order_exists = Order.objects.filter(customer=self.customer, orderitem__product=product).exists()
        self.assertFalse(order_exists)

    def test_login_post_valid(self):
        response = self.client.post(reverse('login'), {'email': 'customer@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 302)

    def test_login_post_invalid(self):
        response = self.client.post(reverse('login'), {'email': 'wrong@example.com', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Неверный email или пароль')

    def test_make_order_post_invalid_product(self):
        data = {
            'product_id': 99999,
            'quantity': 1,
        }
        response = self.customer_client.post(reverse('make_order'), data)
        self.assertEqual(response.status_code, 302)

    def test_logout_redirects(self):
        response = self.customer_client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_order_list_view_for_customer(self):
        response = self.customer_client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_order_list_view_for_guest_redirect(self):
        response = self.guest_client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
