from difflib import SequenceMatcher

def detect_plagiarism(input_text):
    # Sample known texts for comparison
    known_texts = [
        "This is a sample text for plagiarism detection.",
        "Another example of text that could be used for comparison."
    ]
    
    results = []
    for known_text in known_texts:
        similarity = SequenceMatcher(None, input_text, known_text).ratio()
        if similarity > 0.5:  # Threshold for plagiarism
            results.append({
                'text': known_text,
                'similarity': round(similarity * 100, 2)
            })
    
    return {
        'score': len(results),
        'matches': results
    }
