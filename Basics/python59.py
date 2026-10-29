
import numpy as np
import time

TOTAL = 1_000_000_000
BATCH_SIZE = 10_000_000
MAX_VALUE = 1_000_000_000

rng = np.random.default_rng()
start_time = time.perf_counter()
added = 0

with open("random_numbers.txt", "w") as f:
    while added < TOTAL:
        count = min(BATCH_SIZE, TOTAL - added)

        print(f"Generating {count:,} elements...")
        numbers = rng.integers(
            1, MAX_VALUE + 1,
            size=count,
            dtype=np.uint32
        )

        print("Writing file...")
        np.savetxt(f, numbers, fmt="%d")

        added += count
        remaining = TOTAL - added
        elapsed = time.perf_counter() - start_time

        print(
            f"Added: {added:,} | "
            f"Remaining: {remaining:,} | "
            f"Time: {elapsed:.2f}s"
        )

print("Completed!")
