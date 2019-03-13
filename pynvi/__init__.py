"""
`pynvi` Türkiye Cumhuriyeti Nüfus ve Vatandaşlık İşleri Genel
Müdürlüğü SOAP servisi için oluşturulmuş köprü bir Python
kütüphanesidir.
"""

import requests, textwrap

__author__ = "Eray Erdin"
__version__ = "0.1.0pre5"

URL = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"


class NVIException(Exception):
    """
    NVI sunucusu tarafından 200 olmayan cevaplar için bu exception kullanılır.
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.message = """
        NVI server could not process the request properly.

        Response Code: {code}

        Response Content
        ----------------
        {content}
        """.strip().format(
            code=response.status_code, content=response.text
        )
        self.message = textwrap.dedent(self.message)
        super().__init__(self.message)


def verify_identity(
    identity_number: int, name: str, surname: str, year_of_birth: int
) -> bool:
    """
    `TCKimlikNoDogrula` servisine denk gelen metod.

    Girdilerle ilgili kişinin TC vatandaşı olup olmadığını doğrular.
    """
    try:
        identity_number = int(identity_number)
        year_of_birth = int(year_of_birth)
    except ValueError as e:
        raise TypeError(str(e)) from e

    request_body = """
    <?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <TCKimlikNo>{identity_number}</TCKimlikNo>
          <Ad>{name}</Ad>
          <Soyad>{surname}</Soyad>
          <DogumYili>{year_of_birth}</DogumYili>
        </TCKimlikNoDogrula>
      </soap12:Body>
    </soap12:Envelope>
    """.strip().format(
        identity_number=identity_number,
        name=name,
        surname=surname,
        year_of_birth=year_of_birth,
    )
    request_body = textwrap.dedent(request_body)
    response = requests.post(
        URL,
        data=request_body.encode("utf-8"),
        headers={"Content-Type": "application/soap+xml; charset=utf-8"},
    )
    response_body = response.text

    if response.status_code == 200:
        return (
            "<TCKimlikNoDogrulaResult>true</TCKimlikNoDogrulaResult>"
            in response_body
        )

    raise NVIException(response)
