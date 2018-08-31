from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


from django.contrib.auth import get_user_model
from articles.models import Post
from rest_framework.reverse import reverse as api_reverse


User = get_user_model()


class PostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testUser', email="test@test.com")
        user_obj.set_password("somerandompassword")
        user_obj.save()
        post = Post.objects.create(
            user=user_obj,
            title='test title',
            post_slug='test-slug',
            short_description='short_description',
            body='Awesome Post')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = Post.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-posts:post-listcreate")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_list(self):
        data = {'title': 'Some random title', "body": "Awesome Post"}
        url = api_reverse("api-posts:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        post = Post.objects.first()
        data = {}
        url = post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item(self):
        post = Post.objects.first()
        url = post.get_api_url()
        data = {'title': 'Some random title', "body": "Awesome Post"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        # test the get list
        blog_post = Post.objects.first()
        # print(blog_post.content)
        url = blog_post.get_api_url()
        data = {"title": "Some rando title", 'post_slug': 'some-rando_title', 'short_description': 'awesome stuff', "body": "some more content"}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_with_user(self):
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        data = {"title": "Some rando title", 'post_slug': 'some-rando_title', 'short_description': 'awesome stuff', "body": "some awesome", }
        url = api_reverse("api-posts:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_ownership(self):
        # test the get list
        owner = User.objects.create(username='testuser22222')
        blog_post = Post.objects.create(
            user=owner,
            title='test title',
            post_slug='test-slug-1',
            short_description='short_description',
            body='Awesome Post'
        )

        user_obj = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        url = blog_post.get_api_url()
        data = {"title": "Some rando title", 'post_slug': 'some-rando_title', 'short_description': 'awesome stuff', "body": "some more content"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_and_update(self):
        data = {
            'username': 'testUser',
            'password': 'somerandompassword'
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token")
        if token is not None:
            blog_post = Post.objects.first()
            # print(blog_post.content)
            url = blog_post.get_api_url()
            data = {"title": "Some rando title", 'post_slug': 'some-rando_title', 'short_description': 'awesome stuff', "body": "some more content"}
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)  # JWT <token>
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
