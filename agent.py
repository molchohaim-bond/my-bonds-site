import httpx
from supabase import create_client, Client

# פרטי החיבור המדויקים שלך
URL = "https://nmxpfzjkbdejifddkwtpk.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5teHBmemprYmVqaWZkZGt3dHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwODQwNDAsImV4cCI6MjA4MTY2MDA0MH0.8TaOQDXTDp-wXY5SBhD6yMr_MM6UPkvovoe3q1XzFz0"

supabase: Client = create_client(URL, KEY)

def send_data():
    # נתונים לדוגמה שיופיעו באתר שלך
    data = [
        {
            "bond_name": "ממשלתי שקלי 0131",
            "bond_type": "אג״ח ממשלתי",
            "yield_percent": 4.25,
            "duration": 4.1,
            "risk_level": "נמוך",
            "recommendation_reason": "תשואה יציבה בתנאי שוק נוכחיים"
        },
        {
            "bond_name": "לאומי אג״ח י׳",
            "bond_type": "אג״ח קונצרני",
            "yield_percent": 5.12,
            "duration": 3.5,
            "risk_level": "בינוני",
            "recommendation_reason": "מרווח אטרקטיבי מעל הממשלתי"
        }
    ]
    try:
        # ניסיון להכניס את הנתונים לטבלה
        response = supabase.table("bonds").insert(data).execute()
        print("✅ הנתונים נשלחו בהצלחה ל-Supabase!")
    except Exception as e:
        print(f"❌ שגיאה: {e}")

if __name__ == "__main__":
    send_data()
