import pynvi


class TestVerifyIdentity:
    @classmethod
    def setup_class(cls):
        cls.id_number = "11111111111"
        cls.name = "John"
        cls.surname = "Doe"
        cls.year_of_birth = "1994"

    def test_callable(self):
        assert callable(pynvi.verify_identity)

    def test_has_doc(self):
        assert pynvi.verify_identity.__doc__ is not None
