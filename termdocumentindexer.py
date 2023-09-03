from pathlib import Path
from documents import DocumentCorpus, DirectoryCorpus
from indexing import Index, TermDocumentIndex
from text import BasicTokenProcessor, englishtokenstream

"""This basic program builds a term-document matrix over the .txt files in 
the same directory as this file."""

def index_corpus(corpus : DocumentCorpus) -> Index:
    
    token_processor = BasicTokenProcessor()
    vocabulary = set()
    
    for d in corpus:
        print(f"Found document {d.title}")
        print(f"Document: {d.title} is {d.id}")
        temp = englishtokenstream.EnglishTokenStream(d.get_content())
        for i in temp:
            term = token_processor.process_token(i)
            vocabulary.add(term)

    object = TermDocumentIndex(vocabulary, len(corpus))
    for documents in corpus:
        temp = englishtokenstream.EnglishTokenStream(documents.get_content())
        for i in temp:
            term = token_processor.process_token(i)
            object.add_term(term, documents.id)
    return object

if __name__ == "__main__":
    corpus_path = Path()
    d = DirectoryCorpus.load_text_directory(corpus_path, ".txt")
    
    # Build the index over this directory.
    index = index_corpus(d)
    

    query = input(str("What word/term would you like to search for?\nEnter 'quit' to exit: "))
    while query != "quit":
        for p in index.get_postings(query):
            print(f"Word/Term is in Document ID: {d.get_document()}")
        query = input(str("What word/term would you like to search for?\nEnter 'quit' to exit: "))
