-- INFO 430 GROUP PROJECT 
-- TABLE CREATION SCRIPTS

CREATE TABLE USER_PROFILES (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(200) NOT NULL,
    location VARCHAR(200) NOT NULL
)

CREATE TABLE CHALLENGES (
    challenge_id INT IDENTITY(1,1) PRIMARY KEY,
    challenge_based_on VARCHAR(50) NOT NULL,
    challenge_name VARCHAR(200) NOT NULL,
    challenge_descriptions VARCHAR(MAX)
)

CREATE TABLE WORKOUT_GOALS (
    workout_goal_id INT IDENTITY(1,1) PRIMARY KEY,
    workout_goal VARCHAR(200) NOT NULL,
    workout_goal_description VARCHAR(MAX)
)

CREATE TABLE UW_RECREATION_DATA (
    uw_recreation_id INT IDENTITY(1,1) PRIMARY KEY,
    uw_recreation_event VARCHAR(200) NOT NULL,
    uw_recreation_event_date DATE NOT NULL,
    uw_recreation_event_location VARCHAR(200) NOT NULL 
)

CREATE TABLE WEATHER_DATA (
    weather_id INT IDENTITY(1,1) PRIMARY KEY,
    weather_location VARCHAR(200) NOT NULL,
    weather_high_temperature INT NOT NULL,
    weather_low_temperature INT NOT NULL,
    weather_precipitation INT NOT NULL,
    weather_type VARCHAR(50) NOT NULL
)

CREATE TABLE USER_INPUTS (
    user_input_id INT IDENTITY(1,1) PRIMARY KEY,
    workout_goal_id INT FOREIGN KEY REFERENCES WORKOUT_GOALS(workout_goal_id),
    user_input_timestamp DATETIME NOT NULL,
    user_id INT FOREIGN KEY REFERENCES USER_PROFILES(user_id)
)

-- associate tables
CREATE TABLE CHALLENGES_USER_PROFILES (
    challenge_user_profile_id INT IDENTITY(1,1) PRIMARY KEY,
    challenge_id INT FOREIGN KEY REFERENCES CHALLENGES(challenge_id),
    user_id INT FOREIGN KEY REFERENCES USER_PROFILES(user_id)
)

CREATE TABLE CHALLENGES_UW_RECREATION (
    challenge_uw_recreation_id INT IDENTITY(1,1) PRIMARY KEY,
    challenge_id INT FOREIGN KEY REFERENCES CHALLENGES(challenge_id),
    uw_recreation_id INT FOREIGN KEY REFERENCES UW_RECREATION_DATA(uw_recreation_id)
)

CREATE TABLE CHALLENGES_WEATHER (
    challenge_weather_id INT IDENTITY(1,1) PRIMARY KEY,
    challenge_id INT FOREIGN KEY REFERENCES CHALLENGES(challenge_id),
    weather_id INT FOREIGN KEY REFERENCES WEATHER_DATA(weather_id)
)

CREATE TABLE WORKOUT_GOALS_CHALLENGES (
    workout_goal_challenge_id INT IDENTITY(1,1) PRIMARY KEY,
    workout_goal_id INT FOREIGN KEY REFERENCES WORKOUT_GOALS(workout_goal_id),
    challenge_id INT FOREIGN KEY REFERENCES CHALLENGES(challenge_id)
)

CREATE TABLE WORKOUT_GOALS_USER_PROFILES (
    workout_goal_user_profile_id INT IDENTITY(1,1) PRIMARY KEY,
    workout_goal_id INT FOREIGN KEY REFERENCES WORKOUT_GOALS(workout_goal_id),
    user_id INT FOREIGN KEY REFERENCES USER_PROFILES(user_id)
)

CREATE TABLE USER_PROFILE_WEATHER (
    user_profile_weather_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES USER_PROFILES(user_id),
    weather_id INT FOREIGN KEY REFERENCES WEATHER_DATA(weather_id)
)

CREATE TABLE UW_RECREATION_WEATHER (
    uw_recreation_weather_id INT IDENTITY(1,1) PRIMARY KEY,
    uw_recreation_id INT FOREIGN KEY REFERENCES UW_RECREATION_DATA(uw_recreation_id),
    weather_id INT FOREIGN KEY REFERENCES WEATHER_DATA(weather_id)
)
