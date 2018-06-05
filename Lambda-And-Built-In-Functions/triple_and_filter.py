def triple_and_filter(nums):
    return list(
        map(
            lambda n: n * 3,
            filter(
                lambda n: n % 4 == 0,
                nums)
            )
        )