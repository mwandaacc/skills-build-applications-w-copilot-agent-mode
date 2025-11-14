from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.user = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Medium')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300, date='2025-11-14')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=1000, rank=1)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'ironman@marvel.com')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.user.email, 'ironman@marvel.com')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Pushups')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team.name, 'Marvel')
        self.assertEqual(self.leaderboard.rank, 1)
