from final import RAG
search=2
query="World's fastest Car"
question="World's fastest Car"
num_results=5
searcher="duckDuckgo"
isLink=False
model="qwen2.5:7b"

print(RAG(search=search,query=query,question=question,num_results=num_results,searcher=searcher,isLink=False,model=model))

