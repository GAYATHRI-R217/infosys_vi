from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\Admin\OneDrive\infosys_vi\mlbook.pdf')
docs=loader.lazy_load()
docs = loader.load()
for documents in docs:
    print(documents.metadata)
print(len(docs))
#mam code 
#from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

#loader = DirectoryLoader(
 #   path=r'C:\Users\Admin\OneDrive\infosys_vi\mlbook',
  #  glob='*.pdf',
   # loader_cls=PyPDFLoader
#)

#docs = loader.load()
#print(len(docs))  # 181