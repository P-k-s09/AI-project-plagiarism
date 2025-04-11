from plagiarism import detect_plagiarism

def main():
    print("Welcome to the Plagiarism Detection Tool!")
    input_text = input("Please enter the text to check for plagiarism:\n")
    
    if not input_text:
        print("No text entered. Please provide some text to check.")
        return
    
    result = detect_plagiarism(input_text)
    
    print(f"\nOverall Score: {result['score']}")
    print("Matches:")
    for match in result['matches']:
        print(f"- {match['text']} - Similarity: {match['similarity']}%")

if __name__ == "__main__":
    main()
