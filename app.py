from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# PubMed API endpoint
PUBMED_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

def fetch_pubmed_studies(query):
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 1,
        "retmode": "json"
    }
    response = requests.get(PUBMED_API, params=params)
    data = response.json()
    if 'esearchresult' in data and 'idlist' in data['esearchresult']:
        pmids = data['esearchresult']['idlist']
        if pmids:
            return f"https://pubmed.ncbi.nlm.nih.gov/{pmids[0]}/"
    return "https://pubmed.ncbi.nlm.nih.gov/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
    data = request.json
    suggestions = []
    
    if data['diet'] == 'ناسالم':
        suggestions.append({
            "text": "مصرف بیشتر میوه‌ها و سبزیجات می‌تواند خطر بیماری‌های قلبی را کاهش دهد.",
            "link": fetch_pubmed_studies("diet health longevity")
        })
    if data['exercise'] == 'کم':
        suggestions.append({
            "text": "افزایش فعالیت بدنی هفتگی به بهبود طول عمر کمک می‌کند.",
            "link": fetch_pubmed_studies("physical activity longevity")
        })
    if data['sleep'] == 'ضعیف':
        suggestions.append({
            "text": "خواب کافی (۷-۸ ساعت) با کاهش التهاب مرتبط است.",
            "link": fetch_pubmed_studies("sleep health longevity")
        })
    if data['stress'] == 'زیاد':
        suggestions.append({
            "text": "مدیتیشن روزانه می‌تواند استرس را کاهش داده و سلامت روان را بهبود بخشد.",
            "link": fetch_pubmed_studies("stress reduction longevity")
        })
    if data['smoking'] == 'بله':
        suggestions.append({
            "text": "ترک سیگار می‌تواند خطر بیماری‌های ریوی را به طور قابل توجهی کاهش دهد.",
            "link": fetch_pubmed_studies("smoking cessation longevity")
        })
    if data['alcohol'] == 'زیاد':
        suggestions.append({
            "text": "کاهش مصرف الکل می‌تواند به بهبود سلامت کبد کمک کند.",
            "link": fetch_pubmed_studies("alcohol moderation health")
        })
    if data['social'] == 'کم':
        suggestions.append({
            "text": "افزایش تعاملات اجتماعی می‌تواند سلامت روان و طول عمر را بهبود بخشد.",
            "link": fetch_pubmed_studies("social interaction health longevity")
        })
    
    if not suggestions:
        suggestions.append({
            "text": "سبک زندگی شما متعادل است، به حفظ آن ادامه دهید!",
            "link": ""
        })
    
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
