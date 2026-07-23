with open("readme.md") as f:
    for line in f:
        print(line.strip())
        with open("readme.md") as f:
            text = f.read()
            print(text)