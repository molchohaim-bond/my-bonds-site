import httpx
from supabase import create_client, Client

# פרטי החיבור
URL = "https://nmxpfzjkbdejifddkwtpk.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5teHBmemprYmVqaWZkZGt3dHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwODQwNDAsImV4cCI6MjA4MTY2MDA0MH0.8TaOQDXTDp-wXY5SBhD6yMr_MM6UPkvovoe3q1XzFz0"

# יצירת לקוח
supabase: Client = create_client(URL, KEY)

def send_data(name, yield_val, risk):
    data = {
        "bond_name": name,
        "bond_type": "אג״ח",
        "yield_percent": yield_val,
        "duration": 4.0,
        "risk_level": risk,
        "recommendation_reason": "נשלח אוטומטית מהענן"
    }
    try:
        supabase.table("bonds").insert(data).execute()
        print(f"✅ Success: {name}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    send_data("ממשלתי שקלי 0131", 4.2, "נמוך")
    send_data("לאומי אג״ח י׳", 5.1, "בינוני")
