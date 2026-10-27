
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be greater than zero")

        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(character) for character in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        # Update a contact if the name already exists.
        while current is not None:
            if current.key == key:
                current.value.number = value
                return
            current = current.next

        # Otherwise, add a new contact to the linked list.
        contact = Contact(key, value)
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end=" ")
            current = self.data[index]

            if current is None:
                print("Empty")
                continue

            while current is not None:
                print(f"- {current.value}", end=" ")
                current = current.next

            print()


if __name__ == "__main__":
    table = HashTable(10)

    print("INITIAL TABLE")
    table.print_table()

    print("\nADDING CONTACTS")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("Aym", "222-333-1111")
    table.print_table()

    print("\nSEARCHING FOR JOHN")
    print("Search result:", table.search("John"))

    print("\nTESTING DUPLICATE CONTACT")
    table.insert("Rebecca", "999-444-9999")
    print("Updated contact:", table.search("Rebecca"))

    print("\nTESTING MISSING CONTACT")
    print("Chris:", table.search("Chris"))

    print("\nFINAL TABLE")
    table.print_table()
