from faker import Faker


class RandomGenerator:
    faker = Faker()

    @classmethod
    def uuid(cls) -> str:
        return cls.faker.uuid4()

    @classmethod
    def word(cls) -> str:
        return cls.faker.word()
