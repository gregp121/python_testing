import pytest

from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client
from django.contrib import auth
from django.contrib.auth.views import LoginView

@pytest.mark.django_db
def test_login_route():

    client = Client()

#Register user using the ‘signup’ view and store details in the database
    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = client.post(reverse('signup'), credentials)

    #Log user in using the `login` view
    response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    #Check that page redirects to home page
    assert response.status_code == 302
    assert response.url == reverse('home')

    #Check that user has been authenticated
    user = auth.get_user(client)
    assert user.is_authenticated