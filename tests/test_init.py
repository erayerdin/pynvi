import pynvi, pytest


class TestVerifyIdentity:
    @classmethod
    def setup_class(cls):
        cls.id_number = 11111111111
        cls.name = "John"
        cls.surname = "Doe"
        cls.year_of_birth = 1994

    def test_callable(self):
        assert callable(pynvi.verify_identity)

    def test_has_doc(self):
        assert pynvi.verify_identity.__doc__ is not None

    def test_exists(self, mocker):
        mocker.patch("pynvi.requests.post")

        pynvi.requests.post.return_value.status_code = 200
        with open("resources/verified_identity.xml", "r") as f:
            pynvi.requests.post.return_value.text = f.read()

        val = pynvi.verify_identity(
            self.id_number, self.name, self.surname, self.year_of_birth
        )

        assert val

    def test_not_exists(self, mocker):
        mocker.patch("pynvi.requests.post")

        pynvi.requests.post.return_value.status_code = 200
        with open("resources/unverified_identity.xml", "r") as f:
            pynvi.requests.post.return_value.text = f.read()

        val = pynvi.verify_identity(
            self.id_number, self.name, self.surname, self.year_of_birth
        )

        assert not val

    def test_error(self, mocker):
        mocker.patch("pynvi.requests.post")

        pynvi.requests.post.return_value.status_code = 500
        with open("resources/error_verify_identity.xml", "r") as f:
            pynvi.requests.post.return_value.text = f.read()

        with pytest.raises(Exception):
            pynvi.verify_identity(self.id_number, self.name, self.surname, "0")
