# Splitting text into chunks, converting them into embeddings using HuggingFace models, and preparing documents with metadata for vector storage in chroma db.--

# how to find distance betweeen two vectors--
# 1. euclidean distance
# 2. cosine similarity-----  cos theta = a.b

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# str = '''In a quiet valley surrounded by rolling hills, a small village thrived beside a winding river. The people of the village lived simple yet fulfilling lives, spending their days farming, crafting, and sharing stories around evening fires. Every season brought new challenges and opportunities, shaping the traditions that had been passed down through generations.

# One autumn morning, a traveler arrived carrying an old leather journal filled with observations from distant lands. The villagers welcomed the traveler and listened eagerly as tales unfolded about towering mountains, bustling cities, vast deserts, and oceans that stretched beyond the horizon. Children gathered around, fascinated by descriptions of places they had never imagined.

# The journal contained detailed notes about weather patterns, wildlife behavior, and cultural customs. It described how merchants exchanged goods across continents and how scholars preserved knowledge through libraries and manuscripts. The traveler explained that curiosity was one of humanity's greatest strengths, allowing people to learn from one another and adapt to changing circumstances.

# As winter approached, the village prepared for colder days. Farmers stored crops, craftsmen repaired tools, and families collected firewood. During long evenings indoors, people discussed ideas inspired by the traveler's stories. Some dreamed of exploring the world, while others sought ways to improve life within the village itself.

# One young inventor became particularly inspired. Using scraps of metal, wood, and rope, the inventor began creating devices that could simplify daily tasks. Although many early attempts failed, each mistake revealed valuable lessons. Persistence gradually transformed rough concepts into practical solutions. The inventor's success encouraged others to experiment and share their own innovations.

# Years passed, and the village became known as a center of learning and creativity. Visitors arrived from neighboring regions to exchange knowledge and collaborate on projects. New farming techniques increased harvests, improved irrigation systems conserved water, and better transportation methods connected communities that had once been isolated.

# The spirit of cooperation strengthened relationships among the villagers. People recognized that progress often resulted from collective effort rather than individual achievement alone. Teachers mentored students, experienced workers trained apprentices, and community leaders encouraged open discussion about challenges and opportunities.

# As technology evolved, the village adopted tools that enhanced communication and productivity. Information could be shared more quickly, enabling faster decision-making and broader access to education. Despite these advancements, the villagers remained committed to values such as honesty, respect, curiosity, and kindness.

# The story of the village demonstrates how knowledge, perseverance, and collaboration can transform communities over time. Whether through exploration, innovation, or education, individuals contribute to a larger network of shared progress. By remaining open to new ideas while preserving meaningful traditions, societies can continue to grow and adapt in an ever-changing world.'''

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 200,
#     chunk_overlap = 2
# )

# chunks = splitter.split_text(str)

# for i, chunk in enumerate(chunks):
#     print(f"chunk {i}, \n{chunk}, \n{"-"*50}")

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

documents = [
    Document(page_content='''
Langchain is a framework for building LLM applications.
It supports RAG, agents, memory and tools.
''')
]

if __name__ == '__main__':
    # create splitter and split the text of each document
    splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=5)
    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc.page_content))

    print('Chunks:')
    for i, c in enumerate(chunks):
        print(i, repr(c))

    # create embeddings (this will download the model when run)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    # example: embed the chunks
    vectors = embeddings.embed_documents(chunks)
    print(f'Created {len(vectors)} embeddings')

#------------------------------------------------------------------------------------------------------------------------------------

with open("temp.txt", "r") as file:
    str = file.read()

#print(str)    

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

documents = [
    Document(page_content="""
    LangChain is a framework for building LLM applications.
    It supports RAG, agents, memory, and tools.
    """)
]


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)
print(chunks)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
val = [chunk.page_content for chunk in chunks]
print(val)
vecti = embeddings.embed_query(
    val[0]
)
print(f"Embedding dimension: {len(vecti)}")
vectors = embeddings.embed_documents(
    val
)

# print(f"Chunks: {len(chunks)}")
print(f"Embedding dimension: {len(vectors[0])}")


#------------------------------------------------------------------------------------------------------------------------------------


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
model_name="sentence-transformers/all-mpnet-base-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

vector = embeddings.embed_query("Hello world")
print(len(vector))

# in chroma DB--- we add vectors , chunks(page_content), metadata

doc = Document(page_content="Hello world", metadata={"type": "test"})
