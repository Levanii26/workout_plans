from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan, ExercisePlan, ExerciseInstance

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class ExercisePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlan
        fields = '__all__'

class ExerciseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInstance
        fields = '__all__'

class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = '__all__'

class UserFitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFitnessGoal
        fields = '__all__'