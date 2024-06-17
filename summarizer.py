from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_article(article):
    summary = summarizer(article['content'], max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']
