import feedparser
from summarizer import simple_summarize

def fetch_news(feed_url="https://feeds.bbci.co.uk/news/rss.xml"):
    """
    Fetches news articles from an RSS feed URL (default is BBC News).
    Returns a list of article dicts with title, link, and summary.
    """
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:5]:  # Limit to the first 5 for demo
        title = entry.title
        link = entry.link
        # Some feeds include a 'summary' or 'description' — let's use that if available:
        description = entry.summary if 'summary' in entry else ""
        articles.append({"title": title, "link": link, "description": description})
    return articles

def main():
    print("Fetching news from BBC RSS...")
    articles = fetch_news()

    for i, article in enumerate(articles, start=1):
        title = article["title"]
        link = article["link"]
        description = article["description"]

        # Summarize the description (if it's non-empty)
        summary_text = simple_summarize(description, sentence_limit=2) if description else "No summary available."
        
        print(f"\nArticle #{i}")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Summary: {summary_text}")

if __name__ == "__main__":
    main()
