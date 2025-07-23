from faker import Faker


class RandomGenerator:
    faker = Faker()

    @classmethod
    def uuid(cls) -> str:
        return cls.faker.uuid4()

    @classmethod
    def word(cls) -> str:
        return cls.faker.word()


    @classmethod
    def positive_integer(cls, minimum: int = 0, maximum: int = 100) -> int:
        return cls.faker.pyint(min_value=minimum, max_value=maximum)
