from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # دریافت اطلاعات پایه و تکمیلی از کاربر
    age = request.form.get("age")
    gender = request.form.get("gender")
    activity = request.form.get("activity")
    diet = request.form.get("diet")
    sleep = request.form.get("sleep")
    weight = request.form.get("weight")
    height = request.form.get("height")
    stress = request.form.get("stress")
    smoking = request.form.get("smoking")
    alcohol = request.form.get("alcohol")
    
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
        suggestions.append("کیفیت خواب متوسط است؛ تنظیم ساعات خواب می‌تواند به بهبود استراحت شما کمک کند.")
    elif sleep == "خوب":
        suggestions.append("کیفیت خواب شما عالی است؛ سعی کنید این روند را حفظ کنید.")
    
    # پیشنهادات بر اساس سطح استرس
    if stress == "بالا":
        suggestions.append("سطح استرس بالاست؛ استفاده از تکنیک‌های آرامش‌بخش مانند مدیتیشن یا یوگا توصیه می‌شود.")
    elif stress == "متوسط":
        suggestions.append("مدیریت استرس خود را بهبود دهید؛ تمرین‌های آرامش‌بخش می‌تواند مفید باشد.")
    elif stress == "پایین":
        suggestions.append("سطح استرس شما مناسب است؛ ادامه دهید.")
      
    # پیشنهادات بر اساس مصرف سیگار
    if smoking == "دارد":
        suggestions.append("قطع مصرف سیگار برای بهبود سلامت کلی ضروری است.")
    elif smoking == "ندارد":
        suggestions.append("عدم مصرف سیگار به سلامتی شما کمک می‌کند.")

    # پیشنهادات بر اساس مصرف الکل
    if alcohol == "دارد":
        suggestions.append("کاهش یا قطع مصرف الکل می‌تواند به بهبود سلامت کلی شما کمک کند.")
    elif alcohol == "ندارد":
        suggestions.append("عدم مصرف الکل به سلامتی شما کمک می‌کند.")
    
    # محاسبه شاخص توده بدنی (BMI) و پیشنهادات مرتبط
    try:
        weight_val = float(weight)
        height_val = float(height)
        if height_val > 0:
            bmi = weight_val / ((height_val / 100) ** 2)
            if bmi < 18.5:
                suggestions.append("شاخص توده بدنی شما پایین است؛ ممکن است نیاز به افزایش وزن داشته باشید.")
            elif 18.5 <= bmi <= 24.9:
                suggestions.append("شاخص توده بدنی شما در محدوده نرمال است؛ عالی است!")
            else:
                suggestions.append("شاخص توده بدنی شما بالا است؛ توجه به رژیم غذایی و افزایش فعالیت ورزشی ضروری است.")
    except ValueError:
        suggestions.append("خطا در محاسبه شاخص توده بدنی؛ لطفاً مقادیر وزن و قد را بررسی کنید.")

    # پیشنهاد کلی برای سبک زندگی
    suggestions.append("مدیریت استرس و تمرکز بر آرامش ذهنی نقش مهمی در افزایش طول عمر دارد.")

    return render_template(
        "result.html",
        age=age,
        gender=gender,
        activity=activity,
        diet=diet,
        sleep=sleep,
        weight=weight,
        height=height,
        stress=stress,
        smoking=smoking,
        alcohol=alcohol,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)
