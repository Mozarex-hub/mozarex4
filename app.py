from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def search_scientific_literature(lifestyle_input):
    """
    این تابع به صورت نمونه، پیشنهاداتی را بر اساس سبک زندگی ورودی ارائه می‌دهد.
    همچنین می‌توان بخش‌های مرتبط با جستجو در PubMed را در آینده اضافه کرد.
    """
    # مثالی از یک جستجوی ساده در PubMed (تابع نمونه؛ در عمل می‌بایست
    # از API های رسمی PubMed استفاده شود):
    #
    # def search_pubmed(query):
    #     base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    #     params = {
    #         'db': 'pubmed',
    #         'term': query,
    #         'retmode': 'json',
    #         'retmax': 5
    #     }
    #     response = requests.get(base_url, params=params)
    #     if response.status_code == 200:
    #         data = response.json()
    #         id_list = data.get('esearchresult', {}).get('idlist', [])
    #         return id_list
    #     return []
    #
    # For now, we return a static list of suggestions:
    suggestions = [
        "ورزش منظم باعث بهبود عملکرد قلب و عروق می‌شود.",
        "رژیم غذایی متعادل و سرشار از آنتی‌اکسیدان‌ها برای سلامت مفید است.",
        "مدیریت استرس از طریق مدیتیشن و یوگا به افزایش طول عمر کمک می‌کند."
    ]
    return suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lifestyle = request.form.get('lifestyle')
        suggestions = search_scientific_literature(lifestyle)
        return render_template('result.html', lifestyle=lifestyle, suggestions=suggestions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
