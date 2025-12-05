import csv
import os
from datetime import datetime
from typing import List, Dict, Any, Iterable
from collections import defaultdict


Row = Dict[str, Any]


def ld_csv(path: str) -> List[Row]:
    rows: List[Row] = []
    with open(path, newline="") as f:
        rd = csv.DictReader(f)
        for raw in rd:
            if not raw.get("order_id") or not raw.get("date") or not raw.get("region") or not raw.get("product"):
                continue
            try:
                qty = int(raw.get("qty", "0"))
                price = float(raw.get("price", "0") or "0")
                if qty < 0 or price < 0:
                    continue
                dt = datetime.fromisoformat(raw["date"]).date()
            except Exception:
                continue
            rows.append(
                {
                    "id": raw["order_id"],
                    "date": dt,
                    "reg": raw["region"],
                    "prod": raw["product"],
                    "qty": qty,
                    "price": price,
                }
            )
    return rows


def tot_rev(rows: Iterable[Row]) -> float:
    return sum(r["qty"] * r["price"] for r in rows)


def reg_rev(rows: Iterable[Row]) -> Dict[str, float]:
    res: Dict[str, float] = defaultdict(float)
    for r in rows:
        res[r["reg"]] += r["qty"] * r["price"]
    return dict(res)


def prod_rev(rows: Iterable[Row]) -> Dict[str, float]:
    res: Dict[str, float] = defaultdict(float)
    for r in rows:
        res[r["prod"]] += r["qty"] * r["price"]
    return dict(res)


def avg_price(rows: Iterable[Row]) -> Dict[str, float]:
    sum_p: Dict[str, float] = defaultdict(float)
    sum_q: Dict[str, int] = defaultdict(int)
    for r in rows:
        sum_p[r["prod"]] += r["price"] * r["qty"]
        sum_q[r["prod"]] += r["qty"]
    return {p: (sum_p[p] / sum_q[p]) for p in sum_p if sum_q[p] > 0}


def top_prod(rows: Iterable[Row], n: int = 3) -> List[str]:
    rev = prod_rev(rows)
    return [p for p, _ in sorted(rev.items(), key=lambda x: x[1], reverse=True)[:n]]


def mon_rev(rows: Iterable[Row]) -> Dict[str, float]:
    res: Dict[str, float] = defaultdict(float)
    for r in rows:
        key = f"{r['date'].year:04d}-{r['date'].month:02d}"
        res[key] += r["qty"] * r["price"]
    return dict(res)


def main() -> None:
    base = os.path.dirname(__file__)
    path = os.path.join(base, "sales.csv")
    rows = ld_csv(path)
    print("rows:", len(rows))
    print("tot_rev:", round(tot_rev(rows), 2))
    print("reg_rev:", {k: round(v, 2) for k, v in reg_rev(rows).items()})
    print("prod_rev:", {k: round(v, 2) for k, v in prod_rev(rows).items()})
    print("avg_price:", {k: round(v, 2) for k, v in avg_price(rows).items()})
    print("top_prod:", top_prod(rows, 3))
    print("mon_rev:", {k: round(v, 2) for k, v in mon_rev(rows).items()})


if __name__ == "__main__":
    main()
