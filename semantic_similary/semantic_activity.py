import os
import chromadb
from chromadb.config import Settings

# Load sentences from a .txt file
def load_sentences(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# Print results 
def print_results(query, results):
    print("\n======================================")
    print(f"QUERY: {query}")
    print("Top 3 results:")
    for doc in results["documents"][0]:
        print(f" - {doc}")
    print("======================================\n")


# Main code
def main():

    print("\n=== ChromaDB Semantic Similarity Activity ===\n")

    DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(DIR, 'data')

   # Create the Persistent Client

    # Create the collection for the activity



    # Load base dataset (sentences.txt)
    sentences_path = os.path.join(DIR, "sentences.txt")
    base_sentences = load_sentences(sentences_path)

    print(f"Loaded {len(base_sentences)} base sentences.")

    # insert base_sentences data into chromadb collection
    

    print("Inserted base sentences.\n")

    # Run Required Queries return and print top 3 results
    required_queries = [
       
    ]

    print("\n=== Running Required Queries ===")
   


    # Load YOUR own Custom Sentences into new_sentences.txt
    print(f"Loaded NEW student sentences.")


    # Insert your new sentences into chromadb collection

    print("Inserted student custom sentences.\n")
 
    #  Run YOUR Custom queries return and print top 3 results
    print("\n=== Running Student Custom Queries ===")


if __name__ == "__main__":
    main()
