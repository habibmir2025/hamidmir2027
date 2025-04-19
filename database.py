import json

GMAIL_FILE = "gmail_list.json"

def load_gmails():
    with open(GMAIL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_gmails(gmails):
    with open(GMAIL_FILE, "w", encoding="utf-8") as f:
        json.dump(gmails, f, indent=2, ensure_ascii=False)

def get_available_gmails():
    return load_gmails()

def remove_gmail(email):
    gmails = load_gmails()
    gmails = [g for g in gmails if g["email"] != email]
    save_gmails(gmails)