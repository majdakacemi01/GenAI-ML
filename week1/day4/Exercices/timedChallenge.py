def count_occurrences(string, character):
    count = 0
    for ch in string:
        if ch == character:
            count += 1
    print(f"String: {string}")
    print(f"Character: {character}")
    print(f"Count: {count}")

count_occurrences("Programming is cool!", "o")
