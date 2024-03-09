from django.contrib import admin
from .models import Exercise, WorkoutPlan, ExercisePlan, ExerciseInstance, UserWeight, UserFitnessGoal

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(ExercisePlan)
admin.site.register(ExerciseInstance)
admin.site.register(UserWeight)
admin.site.register(UserFitnessGoal)