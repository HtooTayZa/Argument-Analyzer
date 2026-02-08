import sys
import os

# --- CRITICAL FIX ---
# This forces Python to look inside the 'src' folder for modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
# --------------------

from modules.nlp_processor import NLPProcessor
from modules.feature_extractor import FeatureExtractor
from modules.scorer import Scorer
from modules.report_generator import ReportGenerator # NEW IMPORT

def main():
    try:
        # Initialize
        print("Initializing System...")
        nlp = NLPProcessor()
        extractor = FeatureExtractor()
        scorer = Scorer()  # <--- NEW WORKER

        # Test Data
        text = "We should switch to electric cars because they reduce emissions, although the initial cost is higher for most families."
        
        # Process
        print(f"\nAnalyzing: {text}")
        doc = nlp.process_text(text)
        features = extractor.extract_features(doc)

        # Score
        final_score, suggestions = scorer.calculate_score(features)
        
# 5. Output Results
        print("\n--- REPORT ---")
        print(f"FINAL SCORE: {final_score} / 100")
        print("\nSUGGESTIONS FOR IMPROVEMENT:")
        for tip in suggestions:
            print(tip)
        print("----------------")
        
    except Exception as e:
        print(f"An error occurred: {e}")


    # After printing the report to the screen:
    reporter = ReportGenerator()
    file_path = reporter.save_report(text, final_score, suggestions)
    
    print(f"\n📁 Report successfully exported to: {file_path}")

if __name__ == "__main__":
    main()

    