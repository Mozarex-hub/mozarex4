from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

# Function to search PubMed using NCBI E-utilities.
def search_pubmed(query):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5  # Limit to 5 articles for demonstration
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        id_list = data["esearchresult"].get("idlist", [])
        if id_list:
            # Now fetch article summaries
            summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            summary_params = {
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "json"
            }
            summary_response = requests.get(summary_url, params=summary_params)
            if summary_response.status_code == 200:
                summary_data = summary_response.json()
                articles = []
                for uid, article in summary_data["result"].items():
                    if uid == "uids":
                        continue
                    articles.append({
                        "title": article.get("title", "بدون عنوان"),
                        "pubdate": article.get("pubdate", "نامشخص")
                    })
                return articles
    return []

# Simulated AI-based function to analyze results and provide suggestions.
def analyze_results(articles):
    suggestions = []
    for art in articles:
        # For demonstration, simply provide a templated recommendation.
        recommendation = (
            "مطالعه مقاله '{}' می‌تواند نکات مفیدی برای افزایش طول عمر به شما ارائه دهد."
            .format(art["title"])
        )
        suggestions.append(recommendation)
    return suggestions

@app.route("/", methods=["GET", "POST"])
def index():
    articles = []
    suggestions = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        articles = search_pubmed(query)
        suggestions = analyze_results(articles)
    return render_template("index.html", articles=articles, suggestions=suggestions, query=query)

if __name__ == "__main__":
    app.run(debug=True)
