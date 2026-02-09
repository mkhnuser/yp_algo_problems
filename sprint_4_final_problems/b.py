# https://contest.yandex.ru/contest/24414/run-report/155902101/
#
# --- ПРИНЦИП РАБОТЫ
#     Объект HashTable реализует стандартный набор операций, которые поддерживает хеш таблица.
#     Коллизии разрешаются методом открытой адресации.
#
#     Концептуально, работу объекта HashTable можно представить так:
#
#     1. Находим позицию для ключа.
#     2. Ассоциируем данные, на которые ссылается ключ, с самим ключём:
#
#     Ключ <-> хеш -> данные.
#
#     Коллизии разрешаются методом открытой адресации.
#
#
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
#     O(1) в среднем. O(n) в случае коллизий, где n - максимальный размер хеш таблицы.
#
#
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
#     O(n) - где n - размер хеш таблицы.


DEFAULT_HASH_TABLE_SIZE = 10**5


class HashTable:
    def __init__(self, size: int = DEFAULT_HASH_TABLE_SIZE):
        self.size = size
        self.data: list[int | None] = [None] * self.size
        self.positions: list[int | None] = [None] * self.size

    def put(self, key: int, data: int | None):
        hash_value = self.hash(key)

        if self.positions[hash_value] is None:
            self.positions[hash_value] = key
            self.data[hash_value] = data
        elif self.positions[hash_value] == key:
            self.data[hash_value] = data
        else:
            # NOTE: Collision has happened.
            next_pos = self.find_position(
                self.obtain_new_hash_from_old_hash(hash_value),
                key,
            )

            if self.positions[next_pos] is None:
                self.positions[next_pos] = key
                self.data[next_pos] = data
            else:
                self.data[next_pos] = data

    def get(self, key):
        pos = self.find_position(self.hash(key), key)
        return self.data[pos] if self.positions[pos] == key else None

    def delete(self, key):
        data = self.get(key)

        if data is not None:
            self.put(key, None)

        return data

    def hash(self, key):
        return hash(key) % self.size

    def obtain_new_hash_from_old_hash(self, old_hash):
        return hash(old_hash + 1) % self.size

    def find_position(self, hash_value, key):
        while (
            self.positions[hash_value] is not None and self.positions[hash_value] != key
        ):
            hash_value = self.obtain_new_hash_from_old_hash(hash_value)
        # NOTE: When we break, self.positions[hash_value] is None or self.positions[hash_value] == key.
        # That is, we've found an empty spot or the key has already been present in the hash table.
        return hash_value


if __name__ == "__main__":
    n = int(input())
    hash_table = HashTable(n)

    for _ in range(n):
        command = input()

        if command.startswith("get"):
            _, key = command.split()
            print(hash_table.get(int(key)))
        elif command.startswith("put"):
            _, key, value = command.split()
            hash_table.put(int(key), int(value))
        elif command.startswith("delete"):
            _, key = command.split()
            print(hash_table.delete(int(key)))
        else:
            raise RuntimeError("Invalid Command has been received!")
