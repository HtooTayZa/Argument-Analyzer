# Argument Quality Analyzer 

A Python-based NLP tool that evaluates the structural integrity of written arguments. It uses Natural Language Processing to detect claims, premises, evidence, and balanced perspectives.

## Features
* **Claim Detection:** Identifies core arguments using linguistic indicators.
* **Logical Mapping:** Finds supporting premises ("because", "since").
* **Evidence Recognition:** Uses Named Entity Recognition (NER) to find statistics and dates.
* **Nuance Detection:** Recognizes counter-arguments for a balanced score.
* **Auto-Reporting:** Generates a timestamped `.txt` report with actionable feedback.

## 🛠️ Tech Stack
* **Python 3.12**
* **spaCy:** For industrial-strength Natural Language Processing.
* **Git:** For version control.

## 📦 Installation & Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
