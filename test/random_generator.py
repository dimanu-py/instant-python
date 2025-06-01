from faker import Faker


class RandomGenerator:
    fake = Faker()

    @classmethod
    def word(cls) -> str:
        return cls.fake.word()

    @classmethod
    def description(cls) -> str:
        return cls.fake.sentence()

    @classmethod
    def version(cls) -> str:
        return cls.fake.pystr_format(string_format="#{0}.#{0}.#{0}")

    @classmethod
    def name(cls) -> str:
        return cls.fake.name()

    @classmethod
    def email(cls) -> str:
        return cls.fake.email()
