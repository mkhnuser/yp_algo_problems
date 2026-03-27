# https://contest.yandex.ru/contest/25597/run-report/159350179/
#
# --- ПРИНЦИП РАБОТЫ
# Считается сумма всех элементов.
#
# Если она нечётная, тогда нельзя разделить поровну.
# Если чётная, то продолжает алгоритм.
#
# Цель — найти подмножество с суммой summation // 2.
# Используется динамическое программирование:
# dp[j] = True означает, что сумму j можно собрать из некоторых элементов.
#
# Изначально dp[0] = True.
# Для каждого числа обновляется dp с конца к началу (чтобы не переиспользовать элемент дважды):
# dp[j] = dp[j] or dp[j - grade]
#
# Если в какой-то момент удаётся получить half_summation, тогда сразу возвращаем истину.
# В конце возвращается, достижима ли половина суммы.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(n * summation), где n - кол-во элементов массива, summation - размер суммы.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(summation), где summation - размер суммы.


def solve():
    n = int(input())
    grades = list(map(int, input().split()))

    summation = sum(grades)

    half_summation = summation // 2
    dp = [True] + [False for _ in range(half_summation)]

    if summation % 2 != 0:
        return False

    for grade in grades:
        for j in range(half_summation, grade - 1, -1):
            dp[j] = dp[j - grade] or dp[j]

            if j == half_summation and dp[j]:
                return True

    return dp[-1]


if __name__ == "__main__":
    print(solve())
