from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    current = sum(split_integer(17, 7))
    expert = 17
    assert current == expert, f"Sum of parts {current} is not equal to value {expert}"

def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    current = split_integer(18, 2)
    expert = [9, 9]
    assert current == expert, f"Parts {current} is not equal to value {expert}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    current = split_integer(8, 1)
    expert = [8]
    assert current == expert, f"Part {current} is not equal to value {expert}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    current = split_integer(32, 6)
    expert = [5, 5, 5, 5, 6, 6]
    assert current == expert, f"Division of parts {current} is not equal to value {expert}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    current = split_integer(1, 6)
    expert = [0, 0, 0, 0, 0, 1]
    assert current == expert, f"Division of parts {current} is not equal to value {expert}"
