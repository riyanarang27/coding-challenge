import time
import unittest
from typing import List
from producer_consumer import BQueue, Prod, Cons


class TestBQ(unittest.TestCase):
    def test_cap_bad(self):
        with self.assertRaises(ValueError):
            BQueue(0)
        with self.assertRaises(ValueError):
            BQueue(-1)

    def test_basic(self):
        q = BQueue(3)
        q.put(1)
        q.put(2)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.size(), 0)

    def test_fifo(self):
        q = BQueue(20)
        src = list(range(10))
        for v in src:
            q.put(v)
        out = [q.get() for _ in src]
        self.assertEqual(out, src)

    def test_1p1c(self):
        src = list(range(30))
        end = object()
        q = BQueue(4)
        dst: List[int] = []
        p = Prod(src, q, end, 0.001)
        c = Cons(q, end, dst, 0.001)
        p.start()
        c.start()
        p.join()
        c.join()
        self.assertEqual(dst, src)

    def test_cap1(self):
        src = [1, 2, 3, 4, 5]
        end = object()
        q = BQueue(1)
        dst: List[int] = []
        p = Prod(src, q, end, 0.0)
        c = Cons(q, end, dst, 0.005)
        t0 = time.time()
        p.start()
        c.start()
        p.join()
        c.join()
        t1 = time.time()
        self.assertEqual(dst, src)
        self.assertGreater(t1 - t0, 0.01)

    def test_many(self):
        src = list(range(100))
        end = object()
        q = BQueue(5)
        dst: List[int] = []
        p = Prod(src, q, end, 0.0)
        c = Cons(q, end, dst, 0.0)
        p.start()
        c.start()
        p.join()
        c.join()
        self.assertEqual(dst, src)


if __name__ == "__main__":
    unittest.main()
