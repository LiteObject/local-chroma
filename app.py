import chromadb
from chromadb.config import Settings

chroma_client = chromadb.HttpClient(host="chroma", port = 8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
documents = [
    "Mars, often called the 'Red Planet', has captured the imagination of scientists and space enthusiasts alike.",
    "The Hubble Space Telescope has provided us with breathtaking images of distant galaxies and nebulae.",
    "The concept of a black hole, where gravity is so strong that nothing can escape it, was first theorized by Albert Einstein's theory of general relativity.",
]
metadatas = [{'source': "Space"}, {'source': "Space"}, {'source': "Space"}]
ids = ["1", "2", "3"]

collection_status = False
while collection_status != True:
    try:
        document_collection = chroma_client.get_or_create_collection(name="sample_collection")
        collection_status = True
    except Exception as e:
        pass

document_collection.add(documents=documents, metadatas=metadatas, ids=ids)

results = document_collection.query(query_texts="Give me some facts about space", n_results=3)
result_documents = results["documents"][0]
for doc in result_documents:
    print(doc)