from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, f"Sum of parts {sum(split_integer(17, 4))} is not equal to value {17}"

def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], f"Parts {split_integer(6, 2)} is not equal to value {[3, 3]}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], f"Part {split_integer(8, 1)} is not equal to value {[8]}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], f"Division of parts {split_integer(32, 6)} is not equal to value {[5, 5, 5, 5, 6, 6]}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 6) == [0, 0, 0, 0, 0, 1], f"Division of parts {split_integer(1, 6)} is not equal to value {[0, 0, 0, 0, 0, 1]}"

def test_verify_returns_exactly_number_of_parts_elements() -> None:
    assert len(split_integer(17, 7)) == 7, f"Number of parts {len(split_integer(17, 7))} is not equal to expected {7}"

def test_verifying_the_required_invariant() -> None:
    assert max(split_integer(17, 7)) - min(split_integer(17, 7)) <= 1, f"Difference between max and min parts {max(split_integer(17, 7)) - min(split_integer(17, 7))} is greater than 1"
