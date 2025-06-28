# summarizer_backend.py
import sklearn
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
def extractive_summarizer(text, num_sentences=3):
    # Import necessary libraries
    import nltk
    import string
    from nltk.corpus import stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    import networkx as nx

    # Download necessary NLTK data
    nltk.download('punkt')       # For sentence and word tokenization
    nltk.download('stopwords')   # For filtering common stopwords

    # Define set of stopwords
    stop_words = set(stopwords.words('english'))

    # Function to clean and preprocess each sentence
    def clean_sentence(sentence):
        # Tokenize the sentence into words and convert to lowercase
        words = nltk.word_tokenize(sentence.lower())
        # Remove stopwords and punctuation
        words = [w for w in words if w not in stop_words and w not in string.punctuation]
        # Return cleaned sentence as a string
        return ' '.join(words)

    # Tokenize the input text into individual sentences
    original_sentences = nltk.sent_tokenize(text)
    # Filter out very short sentences (less than 6 words)
    sentences = [s for s in original_sentences if len(s.split()) > 5]

    # If number of valid sentences is less than or equal to required summary length, return the original text
    if len(sentences) <= num_sentences:
        return ' '.join(sentences)

    # Create TF-IDF vector representation of the cleaned sentences
    tfidf = TfidfVectorizer(tokenizer=lambda x: clean_sentence(x).split())
    tfidf_matrix = tfidf.fit_transform(sentences)

    # Compute cosine similarity matrix between all sentence vectors
    sim_matrix = cosine_similarity(tfidf_matrix)

    # Convert similarity matrix into a graph structure (nodes = sentences, edges = similarities)
    nx_graph = nx.from_numpy_array(sim_matrix)
    # Apply PageRank algorithm to rank sentence importance
    scores = nx.pagerank(nx_graph)

    # Sort sentences by PageRank score in descending order
    ranked = sorted(((score, i) for i, score in scores.items()), reverse=True)
    # Extract indices of top-ranked sentences
    top_indices = [i for (_, i) in ranked[:num_sentences]]
    # Arrange the selected sentences in their original order
    summary = [sentences[i] for i in sorted(top_indices)]

    # Return the final summary as a single string
    return ' '.join(summary)

# Example usage (optional test)
if __name__ == "__main__":
    sample_text = """Artificial Intelligence (AI) is transforming industries rapidly. 
    From self-driving cars to intelligent assistants, AI is everywhere. 
    The rise of machine learning and deep learning has changed how we interact with technology. 
    However, ethical concerns are also growing. 
    The future of AI depends on responsible development and deployment."""
    
    summary = extractive_summarizer(sample_text, num_sentences=3)
    print("Summary:\n", summary)
#-----------------------------------------------------------------------------------------------------
