import random
import sys

DICE = {
    "d3": 3, "d4": 4, "d6": 6, "d8": 8,
    "d10": 10, "d12": 12, "d20": 20, "d100": 100
}

def roll(die, times=1):
    max_val = DICE.get(die)
    if not max_val:
        return None
    results = [random.randint(1, max_val) for _ in range(times)]
    return results

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("用法: python dice.py <表达式>")
        print("示例: python dice.py 2d20+3")
        print("      python dice.py d20")
        print("      python dice.py 3d6")
        sys.exit(1)

    expr = args[0].lower().replace(" ", "")
    parts = expr.split("+")
    total = 0
    detail = []

    for part in parts:
        if part.isdigit():
            total += int(part)
            detail.append(part)
        elif part in DICE:
            r = roll(part)[0]
            total += r
            detail.append(f"{part}({r})")
        elif "d" in part:
            count, die_name = part.split("d")
            count = int(count) if count else 1
            die_name = f"d{die_name}"
            if die_name in DICE:
                rs = roll(die_name, count)
                s = sum(rs)
                total += s
                detail.append(f"{count}{die_name}({'+'.join(map(str, rs))}={s})")

    print(f"{expr} = {' + '.join(detail)} = {total}")
