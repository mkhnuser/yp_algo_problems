# https://contest.yandex.ru/contest/24414/run-report/155899676/
#
# --- ПРИНЦИП РАБОТЫ
#     Концептуально, вначале мы строим индекс, а затем отвечаем на запросы.
#
#     Для построения индекса, мы соотносим конкретное слово к уникальному идентификатору документа,
#     которой его содержит, а также к весу этого слова. Т.е. получаем следующее отношение:
#
#     Слово -> (документ, вес слова).
#
#     Как только мы построили соотношение выше, мы готовы отвечать на запросы путём ранжирования документов.
#     Пусть на вход дана строка, по которой необходимо выдать релевантные документы.
#     Тогда для каждого уникального слова этой строки мы узнаем уникальный идентификатор документа, а также запомним его вес.
#     Затем отсортируем документы по весу от большего к меньшему, т.е. от самого релевантного к менее релевантному.
#
#
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
#     O(n ^ 2), где n - количество документов.
#
#
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
#     O(m) - где m - количество слов, которые содержатся в документах.


from collections import Counter
from collections import defaultdict


DEFAULT_LIMIT = 5


def create_search_index(documents: list[list[str]]):
    search_index = defaultdict(dict)

    for document_number, words in enumerate(documents, start=1):
        for word, weight in Counter(words).items():
            search_index[word][document_number] = weight

    return search_index


def query_search_index(search_index: dict, query_string: str):
    scores = defaultdict(int)

    for word in set(query_string.split()):
        for doc_id, weight in search_index.get(word, {}).items():
            scores[doc_id] += weight

    return (
        doc_id
        for doc_id, weight in sorted(
            scores.items(),
            key=lambda pair: (-pair[1], pair[0]),
        )[:DEFAULT_LIMIT]
        if weight > 0
    )


if __name__ == "__main__":
    n = int(input())
    documents = [input().strip().split() for _ in range(n)]
    search_index = create_search_index(documents)

    m = int(input())
    for _ in range(m):
        print(*query_search_index(search_index, input()))
