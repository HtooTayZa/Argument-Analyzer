# We import weights from our config file to keep the math adjustable
from config import WEIGHT_CLAIM, WEIGHT_PREMISE

class Scorer:
    def calculate_score(self, features):
        score = 0
        feedback = []

        if features['claims']:
            score += 30
            feedback.append("Great job stating a clear claim.")
        else:
            feedback.append("Your argument is missing a clear 'should' or 'must' statement.")

        if features['premises']:
            score += 25
            feedback.append("You provided reasoning using logical connectives.")
        else:
            feedback.append("Try adding a 'because' to explain your reasoning.")

        if features['evidence']:
            score += 25
            feedback.append("You backed up your point with data or research.")
        else:
            feedback.append("Missing evidence! Try adding a percentage or mentioning a study.")

        if features['refutations']:
            score += 10
            feedback.append("You showed balanced thinking by acknowledging another side.")
        
        if features['claims'] and features['premises'] and features['evidence']:
            score += 10 # Structural bonus

        return min(score, 100), feedback