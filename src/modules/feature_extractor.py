import sys
import os

#  Add the parent 'src' folder to the path so we can find config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import CLAIM_INDICATORS, PREMISE_INDICATORS

class FeatureExtractor:
    def __init__(self):
        self.claims = []
        self.premises = []

    def extract_features(self, doc):
        self.claims = []
        self.premises = []
        self.evidence = []
        self.refutations = [] 

        #  import COUNTER_INDICATORS at the top of the file
        from config import COUNTER_INDICATORS 

        evidence_keywords = ["study", "research", "report", "percent", "statistics"]

        for sent in doc.sents:
            text = sent.text.lower()
            
            # 1. Claim/Premise
            if any(ind in text for ind in CLAIM_INDICATORS):
                self.claims.append(sent.text)
            if any(ind in text for ind in PREMISE_INDICATORS):
                self.premises.append(sent.text)
            
            # 2. Evidence
            has_numbers = any(ent.label_ in ["CARDINAL", "PERCENT", "DATE"] for ent in sent.ents)
            has_keywords = any(word in text for word in evidence_keywords)
            if has_numbers or has_keywords:
                self.evidence.append(sent.text)

            # 3. Counter-Arguments (The Nuance)
            if any(ind in text for ind in COUNTER_INDICATORS):
                self.refutations.append(sent.text)
        
        return {
            "claims": self.claims, 
            "premises": self.premises, 
            "evidence": self.evidence,
            "refutations": self.refutations
        }
