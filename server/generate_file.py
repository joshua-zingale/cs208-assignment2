import random
import hashlib
from config import STORAGE_DIR

def main():
    nouns = ["men", "women", "dogs", "cats", "mysteries"]
    verbs = ["chase", "fear", "love", "want", "forget about"]

    with open(f"{STORAGE_DIR}/mydata.txt", "w") as f:

        for _ in range(30):
            subject = nouns[random.randrange(len(nouns))].capitalize()
            verb = verbs[random.randrange(len(verbs))]
            object = nouns[random.randrange(len(nouns))]
            f.write(f"{subject} {verb} {object}. ")

    with open(f"{STORAGE_DIR}/mydata.txt", "rb") as f:
        print( hash := hashlib.md5(f.read()).hexdigest())
    with open(f"{STORAGE_DIR}/checksum.txt", "w") as f:
        f.write(hash)

if __name__ == "__main__":
    main()