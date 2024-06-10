from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            creator=self.user,
            place="Gym",
            time="07:00:00",
            action="Workout",
            is_pleasant=False,
            periodicity=2,
            duration="00:30:00",
            is_public=True,
        )

    def test_get_public_habits(self):
        url = "/api/habits/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_habit(self):
        data = {
            "creator": self.user.id,
            "time": "06:00:00",
            "action": "Jogging",
            "periodicity": 2,
        }
        response = self.client.post("/api/habits/", data=data, format="json")
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_habit_missing_fields(self):
        data = {
            "creator": self.user.id,
            "time": "06:00:00",
            "action": "Jogging",
        }
        response = self.client.post("/api/habits/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_habit(self):
        url = f"/api/habits/{self.habit.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.habit.id)

    def test_update_habit(self):
        url = f"/api/habits/{self.habit.id}/"
        data = {"place": "Home", "action": "Yoga", "periodicity": 2}
        response = self.client.patch(url, data, format="json")
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, "Home")
        self.assertEqual(self.habit.action, "Yoga")

    def test_delete_habit(self):
        url = f"/api/habits/{self.habit.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
