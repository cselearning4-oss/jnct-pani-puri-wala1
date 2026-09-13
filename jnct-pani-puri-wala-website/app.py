from flask import Flask, render_template, request, jsonify
from pathlib import Path

app = Flask(__name__)

BUSINESS_NAME = "JNCT Pani Puri Wala"
PHONE = "9580092528"
DISCOUNT = 20

MENU = [
    {"id": 1, "name": "Classic Pani Puri", "price": 60, "desc": "Crispy puris with spicy green pani, aloo and chutneys."},
    {"id": 2, "name": "Meetha Pani Puri", "price": 70, "desc": "A sweet & tangy twist with fresh chutneys."},
    {"id": 3, "name": "Masala Pani Puri", "price": 80, "desc": "Extra masala, crunchy puris and bold street-style flavour."},
    {"id": 4, "name": "Special JNCT Pani Puri", "price": 100, "desc": "Our signature loaded pani puri plate."},
]

REVIEWS = [
    {"name": "Aarav", "rating": 5, "text": "Super crispy puris and amazing spicy pani!"},
    {"name": "Priya", "rating": 5, "text": "Fresh, tasty and the JNCT special is excellent."},
    {"name": "Rahul", "rating": 4, "text": "Great street-food taste and good portions."},
]

@app.get("/")
def home():
    return render_template(
        "index.html",
        business_name=BUSINESS_NAME,
        phone=PHONE,
        discount=DISCOUNT,
        menu=MENU,
        reviews=REVIEWS,
    )

@app.post("/api/order")
def order():
    data = request.get_json(silent=True) or {}
    items = data.get("items", [])
    customer = str(data.get("customer", "")).strip()
    total = float(data.get("total", 0) or 0)
    return jsonify({
        "ok": True,
        "message": f"Thanks {customer or 'customer'}! Your order request is ready.",
        "phone": PHONE,
        "total": round(total, 2),
        "items": items,
    })

@app.get("/health")
def health():
    return {"status": "ok", "service": BUSINESS_NAME}

if __name__ == "__main__":
    # 0.0.0.0 is required for deployment and phone/LAN access.
    app.run(host="0.0.0.0", port=5000, debug=True)
