import nltk
import os 

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "uzzinator", "nltk_data"))

# nltk.download('cmudict')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
print("done")
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import cmudict
from nltk.tokenize import PunktTokenizer
import re

class Uzzinator:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('averaged_perceptron_tagger')
        except LookupError:
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('cmudict')
        
        # Initialize CMU dictionary for syllable counting
        self.d = cmudict.dict()
    
    def count_syllables(self, word):
        """Count syllables in a word using CMU dictionary."""
        word = word.lower()
        try:
            print(f"syllable count: {len([x for x in self.d[word][0] if x[-1].isdigit()])}")
            return len([x for x in self.d[word][0] if x[-1].isdigit()])
        except KeyError:
            # If word not in dictionary, estimate syllables based on vowel groups
            print(f"syllable count: {len(re.findall('[aeiouy]+', word))}")
            return len(re.findall('[aeiouy]+', word))
    
    def drop_last_syllable(self, word):
        """Attempt to drop the last syllable of a word."""
        syllables = self.count_syllables(word)
        # if syllables <= 1:
        #     return word
        
        # Find all vowel groups
        vowel_groups = list(re.finditer('[aeiouy]+', word.lower()))
        
        if not vowel_groups:  # No vowels found
            return word
            
        # For single syllable words or when we can't detect multiple syllables,
        # cut before the last vowel group
        if syllables <= 1 or len(vowel_groups) <= 1:
            last_vowel = vowel_groups[-1]
            return word[:last_vowel.start()]
        
        if len(vowel_groups) > 1:
            last_vowel = vowel_groups[-1]
            print(word[:last_vowel.start()])
            return word[:last_vowel.start()]
        return word
    
    def uzzify_word(self, word, pos):
        """Transform a word based on its part of speech."""
        # Skip small functional words
        skip_pos = {'DT', 'UZ', 'IN', 'PRP', 'PRP$', 'TO', 'WDT', 'WP', 'WP$', 'WRB','VB'}
        if pos in skip_pos or word == "i":
            return word
        
        # Always uzzify nouns
        should_uzzify = pos.startswith('NN')
        
        # Optionally uzzify adjectives and emphasized verbs
        if pos.startswith('JJ'):
        # or pos.startswith('VB'):
            # You could add more sophisticated logic here to determine emphasis
            should_uzzify = len(word) > 4  # Simple heuristic
        
        if should_uzzify:
            print(f"uzzifiying {word}")
            # Handle multisyllabic words
            # if self.count_syllables(word) > 1:
                # print("has morethan 1 syllable")
            base = self.drop_last_syllable(word)
            # else:
            #     print("no")
            #     base = word
            
            # Add 'uzz' suffix
            return base + "uzz"
        
        return word
    
    def transform(self, text):
        """Transform input text according to Uzzinator rules."""
        # Tokenize and POS tag the text
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        
        # Transform each word based on its POS tag
        transformed = [self.uzzify_word(word, pos) for word, pos in tagged]
        
        # Reconstruct the sentence while preserving spacing
        result = ''
        for i, word in enumerate(transformed):
            if i > 0 and not word.startswith(('.', ',', '!', '?', ':', ';')):
                result += ' '
            result += word
        
        return result

# Example usage
def main():
    uzzinator = Uzzinator()
    
    # Test cases
    test_sentences = [
        "When you walk in the club with bros and see fine hoes.",
        "The beautiful butterfly landed on the colorful flower.",
        "My friend from London visited yesterday.",
    ]
    
    for sentence in test_sentences:
        transformed = uzzinator.transform(sentence)
        print(f"\nInput: {sentence}")
        print(f"Output: {transformed}")

# if __name__ == "__main__":
#     main()