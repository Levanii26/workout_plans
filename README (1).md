
# Personalized Workout Plan RESTful API

This is a RESTful API for a Personalized Workout Plan system that allows users to create and manage customized workout plans and track their fitness goals. The system provides various features including user authentication, predefined exercises database, personalized workout plans, and tracking of fitness goals.


## Core Features

# 1. User Authentication
 - Secure user registration, login, and logout functionality.
 - Implementation of JWT for session management and secure API access.

 # 2. Predefined Exercises Database
 - A database of exercises, each with descriptions, instructions for execution, target muscles, etc.
 - Initial population with at least 20 diverse predefined exercises.
 # 3. Personalized Workout Plans
 - Functionality for users to create tailored workout plans.
 - Specifications include workout frequency, goals, exercise types, and daily session duration.
 - Ability for users to select exercises from the predefined list and customize their workout by setting repetitions, sets, duration, or distance.
 # 4.Tracking and Goals
 - Features for users to track their weight over time.
 -Ability to set personal fitness goals, including weight objectives and exercise-specific achievements.
 # 5. API Documentation 
 - Use of tools like Swagger for easy endpoint testing and interaction.

 # API Endpoints
 # Authentication
 - POST /api/register/: Register a new user.
 - POST /api/login/: Log in an existing user and receive JWT token. 
 - POST /api/logout/: Log out the currently authenticated user.

 # Exercises
- GET /api/exercises/: Retrieve a list of predefined exercises.
- GET /api/exercises/<exercise_id>/: Retrieve details of a specific exercise.
- POST /api/exercises/: Create a new exercise (admin only).
- PUT /api/exercises/<exercise_id>/: Update details of an exercise (admin only).
- DELETE /api/exercises/<exercise_id>/: Delete an exercise (admin only).

# Workout Plans
- GET /api/workout-plans/: Retrieve a list of user's workout plans.
- GET /api/workout-plans/<plan_id>/: Retrieve details of a specific workout plan.
- POST /api/workout-plans/: Create a new workout plan.
- PUT /api/workout-plans/<plan_id>/: Update details of a workout plan.
- DELETE /api/workout-plans/<plan_id>/: Delete a workout plan.

# Tracking and Goals
- GET /api/weight-tracker/: Retrieve weight tracking data for the authenticated user.
- POST /api/weight-tracker/: Add a new weight tracking record for the authenticated user.
- GET /api/fitness-goals/: Retrieve fitness goals for the authenticated user.
- POST /api/fitness-goals/: Set fitness goals for the authenticated user.

# API Documentation
Swagger or other API documentation tools will be used to provide detailed documentation of all API endpoints, including request and response schemas, authentication requirements, and usage examples.

# Usage
- Make sure to authenticate using JWT token for protected endpoints.
- Refer to the API documentation for detailed usage instructions.
