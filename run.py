# run.py
# Side-by-side execution of structured vs unstructured approaches

import unstructured
import structured


def main():
    x_unstructured = unstructured.run()
    x_structured = structured.run()

    print("Unstructured result:", x_unstructured)
    print("Structured result:  ", x_structured)
    print("Difference:         ", abs(x_unstructured - x_structured))


if __name__ == "__main__":
    main()

