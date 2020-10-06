from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Project
from users.models import CustomUser
from rest_framework import status
from rest_framework.views import APIView

class ProjectTest(APITestCase):
    def setUp(self):
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")

        self.test_user = CustomUser.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.token = Token.objects.create(user=self.test_user)

        payload = {
                    "id": 1,
                    "title": "Project one",
                    "category": "Cake",
                    "description": "The first project.",
                    "goal": 150,
                    "project_image": "https://via.placeholder.com/300.jpg",
                    "is_open": True,
                    "owner_id": '1',
                    "date_created": "2020-09-11T11:30:51",
            }
        # We want to go ahead and originally create a user. 
        self.test_project = Project.objects.create(**payload)


        self.create_url = '/projects/1/'

    def test_edit_project(self):
        payload = {
                    "id": 1,
                    "title": "Project one",
                    "category": "Cake",
                    "description": "The first project.",
                    "goal": 150,
                    "project_image": "https://via.placeholder.com/300.jpg",
                    "is_open": True,
                    "owner_id": '1',
                    "date_created": "2020-09-11T11:30:51",
            }
        """
        Ensure we can edit a test project
        """
        
        response = self.client.put(self.create_url , payload, format='json', HTTP_AUTHORIZATION=self.token)
        print(self.token)
        print(response)
        print(Project.objects.values_list())
        # We want to make sure we have two users in the database..
        self.assertEqual(CustomUser.objects.count(), 2)
        # And that we're returning a 201 created code.
