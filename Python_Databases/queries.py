from models import Challenge

all_challenges = Challenge.select()  # selects all challenges from the database

new_challenge = Challenge.create(language='Ruby', name='Booleans')

sorted_challenges = Challenge.select().order_by(Challenge.steps)