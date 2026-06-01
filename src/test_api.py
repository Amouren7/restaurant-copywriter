"""
Test the Flask server API end-to-end with real DeepSeek key
"""
import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

SERVER = "http://127.0.0.1:5000"

def test(name, endpoint, method="GET", data=None):
    print(f"\n=== {name} ===")
    try:
        if method == "GET":
            resp = requests.get(f"{SERVER}{endpoint}", timeout=10)
        else:
            resp = requests.post(f"{SERVER}{endpoint}", json=data, timeout=60)
        print(f"  HTTP {resp.status_code}")
        result = resp.json()
        if result.get("success"):
            print(f"  [OK] success")
            if "copies" in result:
                copies = result["copies"]
                print(f"  -> {len(copies)} copies generated:")
                for c in copies:
                    text = c['text'][:100].replace('\n',' ')
                    print(f"    [{c['id']}] {text}")
        else:
            print(f"  [FAIL] {result.get('error', 'unknown')}")
        return result
    except Exception as e:
        print(f"  [ERROR] {e}")
        return None

# 1. Health check
test("Health check", "/api/health")

# 2. Categories
test("Categories", "/api/categories")

# 3. Scenes
test("Scenes", "/api/scenes")

# 4. Generate - daily special
test("Generate: daily_special", "/api/generate", "POST", {
    "category": "fast_food",
    "scene": "daily_special",
    "params": {"dish": "红烧排骨盖饭", "price": "15元", "extra": "限50份，炖了3小时"}
})

# 5. Generate - weather
test("Generate: weather", "/api/generate", "POST", {
    "category": "hotpot",
    "scene": "weather",
    "params": {"weather": "降温到5度", "dish": "热黄酒+烤羊肉串"}
})

# 6. Generate - takeaway desc
test("Generate: takeaway_desc", "/api/generate", "POST", {
    "category": "noodle",
    "scene": "takeaway_desc",
    "params": {"dish": "招牌牛肉面", "features": "牛腱子肉，手工拉面，汤底熬6小时", "price": "28元"}
})

# 7. Validation - empty required field
test("Validation: missing field", "/api/generate", "POST", {
    "category": "fast_food",
    "scene": "daily_special",
    "params": {}
})

print("\n========== ALL DONE ==========")
