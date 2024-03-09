from django.contrib.auth.models import User
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ExercisePlan(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

class ExerciseInstance(models.Model):
    exercise_plan = models.ForeignKey(ExercisePlan, on_delete=models.CASCADE)
    completed_repetitions = models.IntegerField(default=0)
    completed_sets = models.IntegerField(default=0)

class UserWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s weight on {self.date}"

class UserFitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100)
    target = models.FloatField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s fitness goal: {self.goal}"