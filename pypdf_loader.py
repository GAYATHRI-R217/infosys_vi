from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('mlbook.pdf')
docs=loader.load()
print(docs[0])
print(len(docs))#181
print(docs[0].metadata)