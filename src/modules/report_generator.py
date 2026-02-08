from datetime import datetime

class ReportGenerator:
    def save_report(self, text, score, suggestions):
        # Create a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.txt"
        
        # 'with open' is the safest way to handle files in Python
        with open(filename, "w", encoding="utf-8") as file:
            file.write("--- ARGUMENT QUALITY ANALYSIS REPORT ---\n")
            file.write(f"Timestamp: {datetime.now()}\n")
            file.write(f"Input Text: {text}\n")
            file.write(f"Final Score: {score}/100\n")
            file.write("-" * 40 + "\n")
            file.write("DETAILED FEEDBACK:\n")
            for tip in suggestions:
                file.write(f"{tip}\n")
            file.write("-" * 40 + "\n")
        
        return filename