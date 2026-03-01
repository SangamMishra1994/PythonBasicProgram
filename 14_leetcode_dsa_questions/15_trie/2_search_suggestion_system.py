from bisect import bisect_left


class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            start = bisect_left(products, prefix)
            suggestions = []

            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result


# ---------------- MAIN FUNCTION ---------------- #

if __name__ == "__main__":
    sol = Solution()

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"

    output = sol.suggestedProducts(products, searchWord)

    print("Suggestions after each character:")
    for i, suggestions in enumerate(output):
        print(f"After typing '{searchWord[:i+1]}': {suggestions}")
