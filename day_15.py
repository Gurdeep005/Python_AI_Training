# Loading documents from different sources — PDF, text, CSV, folders, and websites — into LangChain's Document format.--

# Document Loaders (LangChain)--

# ----------------------------------------------------------------------
# PDF Loader
# ----------------------------------------------------------------------

from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader("book.pdf")
pdf_docs = pdf_loader.load()

print("=== PDF Loader ===")
print(f"Pages loaded: {len(pdf_docs)}")
print(pdf_docs[0].page_content[:300])
print(pdf_docs[0].metadata)


# ----------------------------------------------------------------------
# Text Loader
# ----------------------------------------------------------------------

from langchain_community.document_loaders import TextLoader

text_loader = TextLoader("notes.txt", encoding="utf-8")
text_docs = text_loader.load()

print("\n=== Text Loader ===")
print(f"Docs loaded: {len(text_docs)}")
print(text_docs[0].page_content)
print(text_docs[0].metadata)


# ----------------------------------------------------------------------
# CSV Loader
# ----------------------------------------------------------------------

from langchain_community.document_loaders import CSVLoader

csv_loader = CSVLoader(file_path="data.csv")
csv_docs = csv_loader.load()

print("\n=== CSV Loader ===")
for doc in csv_docs[:5]:
    print(doc.page_content)
    print(doc.metadata)


# ----------------------------------------------------------------------
# Directory Loader (loads multiple files at once)
# ----------------------------------------------------------------------

from langchain_community.document_loaders import DirectoryLoader

dir_loader = DirectoryLoader(
    "my_folder/",
    glob="**/*.txt",
    loader_cls=TextLoader
)
dir_docs = dir_loader.load()

print("\n=== Directory Loader ===")
print(f"Loaded {len(dir_docs)} documents")


# ----------------------------------------------------------------------
# Web Loader (loads content from a URL)
# ----------------------------------------------------------------------

from langchain_community.document_loaders import WebBaseLoader

web_loader = WebBaseLoader("https://example.com")
web_docs = web_loader.load()

print("\n=== Web Loader ===")
print(web_docs[0].page_content[:500])

