import unittest
from datetime import datetime
from typing import Dict, Any, List
import os
import tempfile

import sales


def mk_row(
    id: str,
    date_str: str,
    reg: str,
    prod: str,
    qty: int,
    price: float,
) -> Dict[str, Any]:
    return {
        "id": id,
        "date": datetime.fromisoformat(date_str).date(),
        "reg": reg,
        "prod": prod,
        "qty": qty,
        "price": price,
    }


class TestSalesCore(unittest.TestCase):
    def setUp(self) -> None:
        self.rows: List[Dict[str, Any]] = [
            mk_row("o1", "2024-01-10", "NA", "A", 2, 10.0),
            mk_row("o2", "2024-01-11", "EU", "A", 1, 20.0),
            mk_row("o3", "2024-01-11", "NA", "B", 3, 5.0),
            mk_row("o4", "2024-02-01", "NA", "A", 0, 30.0),
        ]

    def test_tot_rev(self):
        self.assertAlmostEqual(sales.tot_rev(self.rows), 55.0)

    def test_reg_rev(self):
        res = sales.reg_rev(self.rows)
        self.assertAlmostEqual(res["NA"], 35.0)
        self.assertAlmostEqual(res["EU"], 20.0)
        self.assertEqual(set(res.keys()), {"NA", "EU"})

    def test_prod_rev(self):
        res = sales.prod_rev(self.rows)
        self.assertAlmostEqual(res["A"], 40.0)
        self.assertAlmostEqual(res["B"], 15.0)

    def test_avg_price(self):
        res = sales.avg_price(self.rows)
        self.assertAlmostEqual(res["A"], 40.0 / 3.0, places=2)
        self.assertAlmostEqual(res["B"], 5.0, places=2)

    def test_top_prod(self):
        top = sales.top_prod(self.rows, 1)
        self.assertEqual(top, ["A"])
        top2 = sales.top_prod(self.rows, 3)
        self.assertEqual(set(top2), {"A", "B"})

    def test_mon_rev(self):
        res = sales.mon_rev(self.rows)
        self.assertAlmostEqual(res["2024-01"], 55.0)
        self.assertAlmostEqual(res.get("2024-02", 0.0), 0.0)

    def test_empty(self):
        rows: List[Dict[str, Any]] = []
        self.assertEqual(sales.tot_rev(rows), 0.0)
        self.assertEqual(sales.reg_rev(rows), {})
        self.assertEqual(sales.prod_rev(rows), {})
        self.assertEqual(sales.avg_price(rows), {})
        self.assertEqual(sales.top_prod(rows, 3), [])
        self.assertEqual(sales.mon_rev(rows), {})


class TestLoadCsv(unittest.TestCase):
    def test_ld_csv_skips_bad(self):
        hdr = "order_id,date,region,product,qty,price\n"
        good1 = "1,2024-01-01,NA,A,2,10.0\n"
        bad_neg = "2,2024-01-01,NA,B,-1,5.0\n"
        bad_date = "3,not-a-date,NA,C,1,5.0\n"
        bad_missing = ",2024-01-02,NA,D,1,5.0\n"

        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "t.csv")
            with open(p, "w", newline="") as f:
                f.write(hdr)
                f.write(good1)
                f.write(bad_neg)
                f.write(bad_date)
                f.write(bad_missing)
            rows = sales.ld_csv(p)
        self.assertEqual(len(rows), 1)
        r = rows[0]
        self.assertEqual(r["id"], "1")
        self.assertEqual(r["reg"], "NA")
        self.assertEqual(r["prod"], "A")
        self.assertEqual(r["qty"], 2)
        self.assertAlmostEqual(r["price"], 10.0)


if __name__ == "__main__":
    unittest.main()
