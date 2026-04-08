# https://contest.yandex.ru/contest/26133/run-report/160080647/
#
# --- ПРИНЦИП РАБОТЫ
# Создадим префиксное дерево, в котором отразим длину слова для терминального узла (или узлов).
# Далее - для каждого индекса текста (исходной строки) узнаем,
# можно ли составить данную строку из слов, используя динамическое программирование.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(n ** 2) для прохода префиксного дерева, где n - кол-во символов в тексте (исходной строке).
# O(h) для построения префиксного дерева, где h - общая длина всех слов.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n) для динамического массива, где n - количество символов в тексте (исходной строке).
# O(h) для хранения префиксного дерева, где h - общая длина всех слов.


class Node:
    def __init__(self, value, next=None, terminal=False):
        self.value = value

        if next is None:
            self.next = {}
        else:
            self.next = next

        self.terminal = terminal


def create_prefix_tree(words):
    root = Node("")

    for word in words:
        node = root

        for char in word:
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]

        node.terminal = len(word)

    return root


def can_be_composed(text, words):
    dp = [True] + [False for _ in range(len(text))]
    root = create_prefix_tree(words)

    for i in range(len(text)):
        node = root

        if dp[i]:
            for j in range(i, len(text) + 1):
                if node.terminal:
                    dp[j] = True
                if (j == len(text)) or (not node.next.get(text[j], False)):
                    break

                node = node.next[text[j]]

    return dp[-1]


def solve():
    T = input()
    words = tuple(input() for _ in range(int(input())))

    if can_be_composed(T, words):
        return "YES"
    return "NO"


if __name__ == "__main__":
    print(solve())
