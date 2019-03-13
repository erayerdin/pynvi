import requests

"""
`pynvi` Türkiye Cumhuriyeti Nüfus ve Vatandaşlık İşleri Genel
Müdürlüğü SOAP servisi için oluşturulmuş köprü bir Python
kütüphanesidir.
"""

__author__ = "Eray Erdin"
__version__ = "0.1.0pre3"

URL = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx"


def verify_identity(
    identity_number: int, name: str, surname: str, year_of_birth: int
) -> bool:
    """
    `TCKimlikNoDogrula` servisine denk gelen metod.

    Girdilerle ilgili kişinin TC vatandaşı olup olmadığını doğrular.
    """
    identity_number = int(identity_number)
    name = str(name)
    surname = str(surname)
    year_of_birth = int(year_of_birth)

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

    raise Exception(response_body)
