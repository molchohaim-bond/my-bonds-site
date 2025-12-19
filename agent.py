url = "https://nmxpfzjkbdejifddkwtpk.supabase.co"
import os
from supabase import create_client

# הגדרות חיבור
url = "https://nmxpfzjkbdejifddkwtpk.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5teHBmemprYmVqaWZkZGt3dHBrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwODQwNDAsImV4cCI6MjA4MTY2MDA0MH0.8TaOQDXTDp-wXY5SBhD6yMr_MM6UPkvovoe3q1XzFz0"

def run():
    client = create_client(url, key)
    data = [
        {"bond_name": "ממשלתי שקלי 0131", "bond_type": "אג״ח ממשלתי", "yield_percent": 4.25, "risk_level": "נמוך"},
        {"bond_name": "לאומי אג״ח י׳", "bond_type": "אג״ח קונצרני", "yield_percent": 5.12, "risk_level": "בינוני"}
    ]
    try:
        # מחיקת ישנים והכנסת חדשים
        client.table("bonds").delete().neq("id", -1).execute()
        client.table("bonds").insert(data).execute()
        print("✅ SUCCESS")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    run()
