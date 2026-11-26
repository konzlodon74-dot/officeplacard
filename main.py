# Museum placard for an office relic; date, material, find-spot and donor in one line.
SENTENCE = "Ceremonial stapler, c. 2019 CE. Painted steel and plastic. Recovered from the Ruins of Cubicle Row, Level 3; gift of the Facilities Department, 2024."
LIMIT = 180


def main():
    assert SENTENCE.strip() != ""
    assert SENTENCE == SENTENCE.strip()
    assert "\n" not in SENTENCE and "\r" not in SENTENCE
    assert 1 <= len(SENTENCE) <= LIMIT
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(SENTENCE.encode("utf-8"))


if __name__ == "__main__":
    main()
