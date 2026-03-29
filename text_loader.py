from langchain_community.document_loaders import TextLoader
loader = TextLoader('circket.txt')
docs=loader.load()
print(docs[0].page_content)#just the whole content of the file
#print(docs)#[Document(metadata={'source': 'circket.txt'}, page_content=')]
#print(docs[0].metadata)#{'source': 'circket.txt'}
#print(type(docs[0]))#<class 'langchain_core.documents.base.Document'>
#print(len(docs))#prints 1