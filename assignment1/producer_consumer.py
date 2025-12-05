import threading
import time
from typing import Any, List


class BQueue:
    def __init__(self, cap: int) -> None:
        if cap <= 0:
            raise ValueError("cap must be > 0")
        self.cap = cap
        self.q: List[Any] = []
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def put(self, v: Any) -> None:
        with self.cond:
            while len(self.q) >= self.cap:
                self.cond.wait()
            self.q.append(v)
            self.cond.notify_all()

    def get(self) -> Any:
        with self.cond:
            while not self.q:
                self.cond.wait()
            v = self.q.pop(0)
            self.cond.notify_all()
            return v

    def size(self) -> int:
        with self.lock:
            return len(self.q)


class Prod(threading.Thread):
    def __init__(self, src: List[Any], q: BQueue, end: Any, dly: float = 0.0) -> None:
        super().__init__()
        self.src = src
        self.q = q
        self.end = end
        self.dly = dly

    def run(self) -> None:
        for v in self.src:
            if self.dly:
                time.sleep(self.dly)
            self.q.put(v)
        self.q.put(self.end)


class Cons(threading.Thread):
    def __init__(self, q: BQueue, end: Any, dst: List[Any], dly: float = 0.0) -> None:
        super().__init__()
        self.q = q
        self.end = end
        self.dst = dst
        self.dly = dly

    def run(self) -> None:
        while True:
            v = self.q.get()
            if v == self.end:
                break
            if self.dly:
                time.sleep(self.dly)
            self.dst.append(v)


def demo() -> None:
    src = list(range(10))
    dst: List[int] = []
    end = object()
    q = BQueue(3)
    p = Prod(src, q, end, 0.01)
    c = Cons(q, end, dst, 0.01)
    p.start()
    c.start()
    p.join()
    c.join()
    print(dst)


if __name__ == "__main__":
    demo()
