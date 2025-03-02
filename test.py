from final import RAG
search=2
question="What is Extended Reality?"
num_results=5
searcher="duckDuckgo"
isLink=False
model="qwen2.5:7b"

print(RAG(question=question,num_results=num_results,searcher=searcher,isLink=False,model=model))

