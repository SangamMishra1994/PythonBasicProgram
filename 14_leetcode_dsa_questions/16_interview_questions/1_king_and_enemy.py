from collections import Counter


def count_possible_kings(powers):

    # step 1: CAlculate total power of all citizens
    total_power = sum(powers)

    # step 2: Create frequency map of powers
    freq = Counter(powers)

    count = 0

    # step 3: Check each citizen
    for power in powers:

        # Required power that another citizen must have
        required = total_power - power

        # check if required power exits
        if required in freq:
            if required == power:
                if freq[power] > 1:
                    count += 1
                else:
                    count += 1
    return count


# Main Program
def main():
    n = int(input("Enter number of citizen: "))

    powers = list(map(int, input("Enter power values: ").split()))

    if len(powers) != n:
        print("Error: Number of power values must equal n")
        return

    result = count_possible_kings(powers)

    print("NUmber of possible kings: ", result)


if __name__ == "__main__":
    main()
