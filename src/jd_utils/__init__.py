from typing import TypeVar

T = TypeVar("T")


def split_risks(risks: list[T]) -> list[list[T]]:
    n: int = len(risks)
    if n % 3 == 0:
        section_len: int = n // 3
        return [risks[i * section_len:(i + 1) * section_len] for i in range(3)]

    truncate_pos: int = n // 3 * 3
    risks_head: list[T] = risks[:truncate_pos]
    split_truncated_risks: list[list[T]] = split_risks(risks_head)

    for i, extra in enumerate(risks[truncate_pos:]):
        split_truncated_risks[i].append(extra)

    return split_truncated_risks
