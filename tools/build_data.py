# -*- coding: utf-8 -*-
"""museums_raw.json (공공데이터포털 전국박물관미술관정보표준데이터)
+ museums_extra.json (표준데이터 누락분 수동 보강)
-> assets/js/data.js 생성

- 국립·공립만 사용 (사립·대학 제외)
- 지역(17개 시도)·시군구 파싱, 정규화 이름+지역+시군구 기준 중복 제거(기준일 최신 우선)
  (정규화: 공백·'광역' 제거 — "부산광역시립미술관" == "부산시립미술관")
- 요금(무료 판정)·관람시간·휴관정보 정리
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TOOLS = Path(__file__).resolve().parent
BASE = TOOLS.parent
RAW = TOOLS / "museums_raw.json"
EXTRA = TOOLS / "museums_extra.json"
OUT = BASE / "assets" / "js" / "data.js"


def norm_name(name):
    return re.sub(r"\s|광역", "", name)

REGION_PREFIX = [
    ("서울특별시", "서울"), ("서울시", "서울"), ("서울", "서울"),
    ("부산광역시", "부산"), ("부산", "부산"),
    ("대구광역시", "대구"), ("대구", "대구"),
    ("인천광역시", "인천"), ("인천", "인천"),
    ("광주광역시", "광주"), ("광주", "광주"),
    ("대전광역시", "대전"), ("대전", "대전"),
    ("울산광역시", "울산"), ("울산", "울산"),
    ("세종특별자치시", "세종"), ("세종특별시", "세종"), ("세종", "세종"),
    ("경기도", "경기"), ("경기", "경기"),
    ("강원특별자치도", "강원"), ("강원도", "강원"), ("강원", "강원"),
    ("충청북도", "충북"), ("충북", "충북"),
    ("충청남도", "충남"), ("충남", "충남"),
    ("전북특별자치도", "전북"), ("전라북도", "전북"), ("전북", "전북"),
    ("전라남도", "전남"), ("전남", "전남"),
    ("경상북도", "경북"), ("경북", "경북"),
    ("경상남도", "경남"), ("경남", "경남"),
    ("제주특별자치도", "제주"), ("제주도", "제주"), ("제주", "제주"),
]

REGION_ORDER = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

# 시군구 정규식: 지역 접두어 제거 후 첫 시/군/구 토큰
DISTRICT_RE = re.compile(r"^\s*([가-힣]{1,8}?(?:시|군|구))(?=\s|[가-힣])")

METRO = {"서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종"}


def parse_region_district(addr):
    if not addr:
        return None, None
    addr = addr.strip()
    for prefix, region in REGION_PREFIX:
        if addr.startswith(prefix):
            rest = addr[len(prefix):].strip()
            m = DISTRICT_RE.match(rest)
            district = m.group(1) if m else None
            # "수원시 팔달구" 같은 경우 시 단위 유지, 광역시는 구/군 단위
            return region, district
    return None, None


def clean_fee(v):
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    if re.fullmatch(r"\d+", s):
        return int(s)
    return s  # 문자 요금 정보는 그대로


def fee_display(n):
    if n is None:
        return ""
    if isinstance(n, int):
        return "무료" if n == 0 else format(n, ",") + "원"
    return str(n)


def hours_str(o, c):
    o = (o or "").strip()
    c = (c or "").strip()
    if not o or not c or (o in ("00:00", "0:00") and c in ("00:00", "0:00")):
        return ""
    return o + " ~ " + c


def trim(s, n):
    if not s:
        return ""
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def kind_of(name):
    if "미술관" in name or "갤러리" in name or "아트" in name:
        return "미술관"
    if "과학관" in name or "천문" in name or "생태" in name or "생물자원" in name:
        return "과학·생태"
    if "박물관" in name or "뮤지엄" in name:
        return "박물관"
    if "문학관" in name or "문학" in name:
        return "문학관"
    if ("기념관" in name or "역사" in name or "유적" in name or "사료관" in name
            or "민속" in name or "향토" in name or "유물" in name):
        return "역사·민속"
    return "전시·기타"


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    recs = [r for r in raw["records"] if r.get("FCLTY_TYPE") in ("국립", "공립")]
    print("공공(국립+공립) 원본:", len(recs))

    items = {}
    skipped = []
    for r in recs:
        addr = (r.get("RDNMADR") or "").strip() or (r.get("LNMADR") or "").strip()
        region, district = parse_region_district(addr)
        if not region:
            skipped.append((r["FCLTY_NM"], addr))
            continue
        try:
            lat = round(float(r["LATITUDE"]), 6)
            lng = round(float(r["LONGITUDE"]), 6)
        except (TypeError, ValueError):
            skipped.append((r["FCLTY_NM"], "좌표없음"))
            continue
        if not (33.0 < lat < 38.7 and 124.5 < lng < 131.9):
            skipped.append((r["FCLTY_NM"], "좌표범위밖"))
            continue

        name = re.sub(r"\s+", " ", r["FCLTY_NM"]).strip()
        key = (norm_name(name), region, district or "")
        ref = r.get("REFERENCE_DATE") or ""
        if key in items and items[key]["_ref"] >= ref:
            continue

        adult = clean_fee(r.get("ADULT_CHRGE"))
        youth = clean_fee(r.get("YNGBGS_CHRGE"))
        child = clean_fee(r.get("CHILD_CHRGE"))
        # 요금 셋 다 비어 있으면 '정보 없음'(None), 아니면 전부 0/빈값일 때 무료
        if all(f is None for f in (adult, youth, child)):
            is_free = None
        else:
            is_free = all((f is None) or f == 0 for f in (adult, youth, child))

        fee_parts = []
        for label, f in (("어른", adult), ("청소년", youth), ("어린이", child)):
            if f is not None:
                fee_parts.append(label + " " + fee_display(f))
        fee_info = " · ".join(fee_parts)

        homepage = (r.get("HOMEPAGE_URL") or "").strip()
        if homepage and not homepage.startswith("http"):
            homepage = "http://" + homepage

        items[key] = {
            "_ref": ref,
            "name": name,
            "type": r["FCLTY_TYPE"],
            "kind": kind_of(name),
            "region": region,
            "district": district or "",
            "address": addr,
            "lat": lat,
            "lng": lng,
            "phone": (r.get("OPER_PHONE_NUMBER") or r.get("PHONE_NUMBER") or "").strip(),
            "homepage": homepage,
            "hoursWeek": hours_str(r.get("WEEKDAY_OPER_OPEN_HHMM"), r.get("WEEKDAY_OPER_COLSE_HHMM")),
            "hoursHol": hours_str(r.get("HOLIDAY_OPER_OPEN_HHMM"), r.get("HOLIDAY_CLOSE_OPEN_HHMM")),
            "closed": trim(r.get("RSTDE_INFO"), 90),
            "isFree": is_free,
            "feeInfo": fee_info,
            "feeEtc": trim(r.get("ETC_CHRGE_INFO"), 120),
            "intro": trim(r.get("FCLTY_INTRCN"), 220),
            "transport": trim(r.get("TRNSPORT_INFO"), 160),
            "facility": trim(r.get("FCLTY_INFO"), 90),
            "operOrg": trim(r.get("OPER_INSTITUTION_NM"), 40),
            "refDate": ref,
        }

    # ---------- 수동 보강분 병합 (표준데이터에 없는 시설만) ----------
    survey = date.today().isoformat()
    existing_names = {k[0] for k in items}
    added_extra = 0
    if EXTRA.exists():
        extra = json.load(open(EXTRA, encoding="utf-8"))
        for e in extra["items"]:
            if norm_name(e["name"]) in existing_names:
                print("  보강 건너뜀(이미 있음):", e["name"])
                continue
            region, district = parse_region_district(e["address"])
            if not region:
                print("  보강 건너뜀(주소 파싱 실패):", e["name"])
                continue
            key = (norm_name(e["name"]), region, district or "")
            items[key] = {
                "_ref": survey,
                "name": e["name"],
                "type": e["type"],
                "kind": kind_of(e["name"]),
                "region": region,
                "district": district or "",
                "address": e["address"],
                "lat": e["lat"],
                "lng": e["lng"],
                "phone": e.get("phone", ""),
                "homepage": e.get("homepage", ""),
                "hoursWeek": e.get("hoursWeek", ""),
                "hoursHol": e.get("hoursHol", ""),
                "closed": e.get("closed", ""),
                "isFree": e.get("isFree"),
                "feeInfo": e.get("feeInfo", ""),
                "feeEtc": e.get("feeEtc", ""),
                "intro": e.get("intro", ""),
                "transport": e.get("transport", ""),
                "facility": e.get("facility", ""),
                "operOrg": e.get("operOrg", ""),
                "refDate": survey,
            }
            added_extra += 1
    print("수동 보강 추가:", added_extra)

    out = []
    ordered = sorted(items.values(), key=lambda x: (REGION_ORDER.index(x["region"]), x["district"], x["name"]))
    for i, it in enumerate(ordered, 1):
        it.pop("_ref")
        it["id"] = i
        out.append(it)

    print("정제 후:", len(out), "| 제외:", len(skipped))
    for s in skipped[:10]:
        print("  제외:", s)

    from collections import Counter
    print("지역별:", dict(Counter(x["region"] for x in out)))
    print("종류별:", dict(Counter(x["kind"] for x in out)))
    print("무료:", sum(1 for x in out if x["isFree"] is True),
          "유료:", sum(1 for x in out if x["isFree"] is False),
          "정보없음:", sum(1 for x in out if x["isFree"] is None))

    meta = {
        "surveyDate": date.today().isoformat(),
        "source": "공공데이터포털 전국박물관미술관정보표준데이터",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// 자동 생성 파일 — tools/build_data.py 가 생성. 직접 수정하지 마세요.\n")
        f.write("window.DATA_META = " + json.dumps(meta, ensure_ascii=False) + ";\n")
        f.write("window.MUSEUMS = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print("저장:", OUT, "|", OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
