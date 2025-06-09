from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    age = request.form.get("age")
    gender = request.form.get("gender")
    activity = request.form.get("activity")
    diet = request.form.get("diet")
    sleep = request.form.get("sleep")
    
    suggestions = []

    # پیشنهادات بر اساس فعالیت بدنی
    if activity == "کم":
        suggestions.append("فعالیت بدنی خود را افزایش دهید؛ پیاده‌روی منظم یا ورزش‌های سبک می‌تواند مفید باشد.")
    elif activity == "متوسط":
        suggestions.append("با افزایش فعالیت بدنی، سلامت قلب و عروق خود را تقویت کنید.")
    elif activity == "زیاد":
        suggestions.append("فعالیت بدنی شما مناسب است؛ اطمینان حاصل کنید که به اندازه کافی استراحت می‌کنید.")

    # پیشنهادات بر اساس رژیم غذایی
    if diet == "نامتعادل":
        suggestions.append("رژیم غذایی خود را بهبود دهید؛ مصرف میوه، سبزیجات و غلات کامل توصیه می‌شود.")
    elif diet == "متعادل":
        suggestions.append("رژیم غذایی شما نسبتا مناسب است؛ کمی تغییرات می‌تواند به بهبود سلامت شما کمک کند.")
    elif diet == "سالم":
        suggestions.append("رژیم غذایی سالم شما را تحسین می‌کنیم؛ ادامه دهید.")

    # پیشنهادات بر اساس کیفیت خواب
    if sleep == "ضعیف":
        suggestions.append("کیفیت خواب خود را بهبود دهید؛ محیط خواب آرام و منظم داشته باشید.")
    elif sleep == "متوسط":
        suggestions.append("کیفیت خواب متوسط است؛ با تنظیم ساعات خواب می‌توانید از استراحت بهتری بهره‌مند شوید.")
    elif sleep == "خوب":
        suggestions.append("کیفیت خواب شما عالی است؛ سعی کنید این روند را حفظ کنید.")

    # پیشنهاد کلی برای سبک زندگی
    suggestions.append("مدیریت استرس و تمرکز بر آرامش ذهنی نقشی کلیدی در افزایش طول عمر دارد.")

    return render_template(
        "result.html",
        age=age,
        gender=gender,
        activity=activity,
        diet=diet,
        sleep=sleep,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)
