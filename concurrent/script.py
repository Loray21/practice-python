import os
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

ACCESS_TOKEN = "EAAOa6ZCeudw8BP6BxEvZA49lHCeZBUcbit5yPF6b7Wv4EVpH6JGTAbVtuBmsXjT83gAbwmjxGno4LZAQqttsnu1DZB5hUsIQe3vN1BSKqYWLsSWPAgJFYyh7ULDy70xgMKFx298GriYrvxUfoPffPkaustibpJJDWIcQqwCTNIU7wqx5xrZCjyL5K8xhJvS2l6bUVV5ficb0DWA6MfHbfk5nNQuv4ZCuGf1NiDDJwV54buvWgkOB2XYyvl4Yxl8RokTWxBEugzJfZB1nndZAqGZBp2RN7Jvb9wHQnvQJuB"

BASE_URL = "https://graph.facebook.com/v22.0"
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def fetch(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    if params is None:
        params = {}
    params["access_token"] = ACCESS_TOKEN
    try:
        resp = requests.get(url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
    except Exception as e:
        print(f"Error calling {endpoint}: {e}")
        return None


def get_adaccounts():
    data = fetch("me/adaccounts", {"fields": "id,name,created_time"})
    return data.get("data", []) if data else []


def task_call(i):
    try:
        accounts = get_adaccounts()
        print(f"[{i}] llamada ok - {len(accounts)} cuents")
        return {"i": i, "status": True, "count": len(accounts)}
    except Exception as e:
        return {"i": i, "status": False, "err": str(e)}
        

def run_many_call(total_calls=50000, max_workers=100):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(task_call, i) for i in range(1, total_calls + 1)]
        for fut in as_completed(futures):
            results.append(fut.result())    
    return results


result = run_many_call()
print(result)
# accounts = get_adaccounts()
# retries = 0 
# while retries <= 5000:
#     accounts = get_adaccounts()
#     print("una llamda")
#     retries +=1

#     for acc in accounts:
#         print(f"Cuenta: {acc['name']} ({acc['id']})")


        