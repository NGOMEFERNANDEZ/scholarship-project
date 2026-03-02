from transformers import pipeline
 
# Load a small sentiment analysis model
classifier = pipeline('sentiment-analysis',
                      model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
 
result = classifier('The Generative AI Scholarship Program is amazing!')
print(result)
# Expected: [{'label': 'POSITIVE', 'score': 0.99...}]
