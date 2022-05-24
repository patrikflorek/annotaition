# __main__.py

import sys

from annotaition.annotation import Annotation


def get_annotation():
    a = Annotation()

    if len(sys.argv) > 1:
        json_file_path = sys.argv[0]
        a.load_json(json_file_path)
    else:
        a.load_json("annotaition/data/organic_annotation.json")

    return a


if __name__ == "__main__":
    annotation = get_annotation()
    print(annotation)
