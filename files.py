with open("readme.md") as f:
    for line in f:
        print(line.strip())
        with open("readme.md") as f:
            text = f.read()
            print(text)
            with open("readme.md", "w") as f:
                f.write("update the insertion with a new note")
                with open("readme.md", "a") as f:
                    f.write("Ai\n")