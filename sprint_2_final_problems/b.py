# https://contest.yandex.ru/contest/22781/run-report/153169404/

# --- ПРИНЦИП РАБОТЫ
# Алгоритм всегда оперирует над двумся последними операндами как только находит операцию.
# После выполнения операции мы кладём результат обратно на стек, т.к. результат может быть
# переиспользован в последующих операциях.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# В рамках алгоритма всего один цикл, нет рекурсии и вызовов внешних рутин.
# В рамках цикла выполняются константные операции.
# Временная сложность: O(n), где n - длина строки, которая подаётся на входе.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n), где n - длина строки, которая подаётся на входе.


def solve():
    chars = input().split()
    stack = []

    for char in chars:
        if str.isnumeric(char.lstrip("+-")):
            stack.append(int(char))
        elif char == "+":
            last = stack.pop()
            prev = stack.pop()
            stack.append(prev + last)
        elif char == "-":
            last = stack.pop()
            prev = stack.pop()
            stack.append(prev - last)
        elif char == "*":
            last = stack.pop()
            prev = stack.pop()
            stack.append(prev * last)
        elif char == "/":
            last = stack.pop()
            prev = stack.pop()
            stack.append(prev // last)

    return stack[-1]


if __name__ == "__main__":
    print(solve())
