# -*- coding: utf-8 -*-
"""museums_extra.json 좌표를 Nominatim으로 검증·정밀화
- 시설명 검색 → 실패 시 주소 검색
- 결과가 기존 추정 좌표에서 30km 이상 벗어나면 무시(오매칭 방지)
"""
import json
import math
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
EXTRA = Path(__file__).resolve().parent / "museums_extra.json"

def query(q):
    url = ("https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=kr&q="
           + urllib.parse.quote(q))
    req = urllib.request.Request(url, headers={"User-Agent": "museum-map-builder/1.0 (personal blog project)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        res = json.load(r)
    return (float(res[0]["lat"]), float(res[0]["lon"])) if res else None

def dist_km(a, b):
    return math.dist(a, b) * 111  # 근사

data = json.load(open(EXTRA, encoding="utf-8"))
for it in data["items"]:
    guess = (it["lat"], it["lng"])
    hit = None
    for q in (it["name"].split("(")[0], it["address"]):
        try:
            hit = query(q)
        except Exception as e:
            print("  조회 실패:", q, e)
            hit = None
        time.sleep(1.1)  # Nominatim rate limit
        if hit:
            break
    if hit and dist_km(guess, hit) <= 30:
        it["lat"], it["lng"] = round(hit[0], 6), round(hit[1], 6)
        print(f"OK  {it['name']}: {hit} (이동 {dist_km(guess, hit):.1f}km)")
    elif hit:
        print(f"SKIP {it['name']}: 결과 {hit} 가 추정치에서 {dist_km(guess, hit):.0f}km 벗어남 — 추정치 유지")
    else:
        print(f"MISS {it['name']}: 결과 없음 — 추정치 유지")

json.dump(data, open(EXTRA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("저장:", EXTRA)
