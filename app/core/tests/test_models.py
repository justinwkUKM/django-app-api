from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_creat_user_email_successfull(self):
        '''test creating a new user with an email is successfull'''

        email = 'test@waqasobeidy.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test if the email for the new user is normalized'''

        email = 'test@GOOGLE.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_email_validation(self):
        '''test if the email for the new user is valid'''

        with self.assertRaises(ValueError):

            email = None
            password = '123456'
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_new_superuser(self):
        '''test to create a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
