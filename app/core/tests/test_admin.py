from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        '''setup the client for django admin and user'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@GMAIL.com',
            password='123456'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='test@Gmail.com',
            password='123456',
            name="Tester Man"
        )

    def test_user_listed(self):
        '''test that the users are listed on the user page'''
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        '''test that the users edit page works'''
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/id
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add_user_page(self):
        '''test that the users edit page is added'''
        url = reverse('admin:core_user_add')
        # /admin/core/user/id
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
