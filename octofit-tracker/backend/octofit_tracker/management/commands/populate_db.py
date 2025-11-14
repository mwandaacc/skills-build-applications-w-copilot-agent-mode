from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Clear existing data in correct order, deleting objects individually
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()
        for obj in User.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users and save immediately
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captainamerica = User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc)

        # Create workouts and save immediately
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Medium')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Easy')

        # Create activities and save immediately
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-11-14')
        Activity.objects.create(user=captainamerica, type='Pushups', duration=20, calories=150, date='2025-11-13')
        Activity.objects.create(user=batman, type='Running', duration=40, calories=400, date='2025-11-12')
        Activity.objects.create(user=wonderwoman, type='Pushups', duration=25, calories=200, date='2025-11-11')

        # Create leaderboard and save immediately
        Leaderboard.objects.create(team=marvel, points=1000, rank=1)
        Leaderboard.objects.create(team=dc, points=900, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated.'))
