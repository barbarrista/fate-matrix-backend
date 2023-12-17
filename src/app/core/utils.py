from datetime import UTC, datetime


def utc_now() -> datetime:
    return datetime.now(tz=UTC)


def sum_of_number(number: int) -> int:
    """
    Returns the sum of all numbers of the passed number. If the sum is greater than 22,
    then the resulting number continues to be summed until the result is a number <= 22
    """
    max_archetypes_count = 22

    if number <= max_archetypes_count:
        return number

    sum_ = 0
    while number != 0:
        sum_ += number % 10
        number //= 10

    if sum_ > max_archetypes_count:
        return sum_of_number(number=sum_)

    return sum_
