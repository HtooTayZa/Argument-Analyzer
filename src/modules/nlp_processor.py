import spacy

class NLPProcessor:
    def __init__(self):
        # Load the English model
        # If this fails, run: python -m spacy download en_core_web_sm
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text):
        return self.nlp(text)

    def get_sentences(self, doc):
        return [sent.text for sent in doc.sents]