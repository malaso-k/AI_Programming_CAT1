import json
from pathlib import Path
from difflib import get_close_matches

JSON_FILE = Path("students.json")
TEXT_FILE = Path("students.txt")

ALLOWED_TOOLS = {
    "chatgpt", "bard", "claude", "copilot", "gpt-4", "gpt-3.5", "llama",
    "stable diffusion", "dall-e", "midjourney", "huggingface", "anthropic",
    "bing chat", "perplexity", "vscode", "pycharm", "jupyter", "colab",
    "replit", "git", "github", "gitlab", "bitbucket", "docker", "postman",
    "intellij", "sublime", "vim", "emacs","python", "cloud"
}

def normalize_record(rec):
    if not isinstance(rec, dict):
        return {}
    if "favorite_tool" in rec:
        return rec
    for alt in ("favorite_AI_tool", "favorite_AI_tool ", "favorite_AI_tool_name",
                "favorite tool", "favorite-tool", "favorite_AI"):
        if alt in rec:
            rec["favorite_tool"] = rec.pop(alt)
            return rec
    rec["favorite_tool"] = rec.get("favorite_tool", "")
    return rec

def load_existing():
    if not JSON_FILE.exists():
        return []
    try:
        with JSON_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []
    normalized = []
    for item in data:
        if isinstance(item, dict):
            normalized.append(normalize_record(item))
    return normalized

def save_json(students):
    with JSON_FILE.open("w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def save_text(new_students):
    with TEXT_FILE.open("a", encoding="utf-8") as f:
        for s in new_students:
            name = s.get("name", "")
            sid = s.get("student_id", "")
            tool = s.get("favorite_tool", "")
            f.write(f"Name: {name}, ID: {sid}, Favorite Tool: {tool}\n")

def validate_tool(user_input):
    key = (user_input or "").strip().lower()
    if key in ALLOWED_TOOLS:
        return key
    suggestions = get_close_matches(key, sorted(ALLOWED_TOOLS), n=3, cutoff=0.6)
    if suggestions:
        print("Did you mean one of these?")
        for i, s in enumerate(suggestions, 1):
            print(f"{i}. {s}")
        choice = input("Enter number to accept suggestion or press Enter to retry: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(suggestions):
                return suggestions[idx]
    print("Tool not recognized. Try one of:", ", ".join(sorted(ALLOWED_TOOLS)[:8]) + ", ...")
    return None

def collect_students():
    students = []
    while True:
        name = input("Name: ").strip()
        student_id = input("Student ID: ").strip()
        while True:
            fav = input("Favorite AI or coding tool: ").strip()
            valid = validate_tool(fav)
            if valid:
                break
        students.append({"name": name, "student_id": student_id, "favorite_tool": valid})
        more = input("Add another? yes/no: ").strip().lower()
        if more != "yes":
            break
    return students

def print_students(all_students):
    total = len(all_students)
    print(f"\nTotal students: {total}\n")
    for i, s in enumerate(all_students, 1):
        name = s.get("name", "")
        sid = s.get("student_id", "")
        tool = s.get("favorite_tool", "")
        print(f"Student {i}")
        print(f"  Name: {name}")
        print(f"  ID  : {sid}")
        print(f"  Tool: {tool}\n")

def main():
    existing = load_existing()
    new = collect_students()
    # ensure new records are normalized too
    new = [normalize_record(r) for r in new]
    all_students = existing + new
    print_students(all_students)
    save_text(new)
    save_json(all_students)
    print("Saved_to_students.txt and students.json")

if __name__ == "__main__":
    main()
