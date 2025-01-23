import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

def simple_summarize(text, sentence_limit=3):
    """
    Summarize the text by selecting the top-ranked sentences
    based on word frequency.
    """
    # Download NLTK resources if not already installed
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

    sentences = sent_tokenize(text)
    if len(sentences) <= sentence_limit:
        return text  # If it's already short, return the entire text

    # Frequency table of words
    stop_words = set(stopwords.words('english'))
    freq_table = {}
    for word in word_tokenize(text.lower()):
        if word in stop_words or word in string.punctuation:
            continue
        freq_table[word] = freq_table.get(word, 0) + 1

    # Score each sentence by summing frequencies of words in that sentence
    sentence_scores = {}
    for sentence in sentences:
        word_count_in_sentence = 0
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                word_count_in_sentence += freq_table[word]
        sentence_scores[sentence] = word_count_in_sentence

    # Sort sentences by score in descending order
    sorted_sentences = sorted(
        sentence_scores, key=sentence_scores.get, reverse=True
    )

    # Pick the top sentences as the summary
    summary_sentences = sorted_sentences[:sentence_limit]
    summary = " ".join(summary_sentences)
    return summary
