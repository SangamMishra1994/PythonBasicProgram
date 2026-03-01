class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# ---------------- MAIN FUNCTION ---------------- #

if __name__ == "__main__":

    trie = Trie()

    # Insert words
    trie.insert("apple")
    print("Inserted: apple")

    # Search full word
    print("Search 'apple':", trie.search("apple"))   # True

    # Search incomplete word
    print("Search 'app':", trie.search("app"))       # False

    # Check prefix
    print("StartsWith 'app':", trie.startsWith("app"))  # True

    # Insert another word
    trie.insert("app")
    print("Inserted: app")

    # Search again
    print("Search 'app':", trie.search("app"))       # True