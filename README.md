# pynvi

[![PyPI](https://img.shields.io/pypi/v/pynvi.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI - Status](https://img.shields.io/pypi/status/pynvi.svg?style=flat-square)][pypi_url]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pynvi.svg?style=flat-square&logo=python&logoColor=white)][pypi_url]
[![PyPI - License](https://img.shields.io/pypi/l/pynvi.svg?style=flat-square)](LICENSE.txt)
[![Style Black](https://img.shields.io/badge/style-black-black.svg?style=flat-square)](https://black.readthedocs.io/)
[![Telegram](https://img.shields.io/badge/telegram-%40erayerdin-%2332afed.svg?style=flat-square&logo=telegram&logoColor=white)](https://t.me/erayerdin)

[pypi_url]: https://pypi.org/project/pynvi/

|             | Build | Coverage |
|-------------|-------|----------|
| master      | [![Travis (.org) master](https://img.shields.io/travis/com/erayerdin/pynvi/master.svg?style=flat-square&logo=travis&logoColor=white)][travis_url]           | [![Codecov master](https://img.shields.io/codecov/c/github/erayerdin/pynvi/master.svg?style=flat-square&logo=codecov&logoColor=white)][codecov_url]      |
| development | [![Travis (.org) development](https://img.shields.io/travis/com/erayerdin/pynvi/development.svg?style=flat-square&logo=travis&logoColor=white)][travis_url] | [![Codecov development](https://img.shields.io/codecov/c/github/erayerdin/pynvi/development.svg?style=flat-square&logo=codecov&logoColor=white)][codecov_url] |

[travis_url]: https://travis-ci.org/erayerdin/pynvi
[codecov_url]: https://codecov.io/gh/erayerdin/pynvi

`pynvi` Türkiye Cumhuriyeti Nüfus ve Vatandaşlık İşleri Genel
Müdürlüğü SOAP servisi için oluşturulmuş köprü bir Python
kütüphanesidir.

# Neler Yapılabilir?

Bu kütüphane ile Türkiye Cumhuriyeti Nüfus ve Vatandaşlık İşleri
Genel Müdürlüğü'nün SOAP servisinin verdiği hizmetlerden
yararlanılabilir. Neler yapılacağına dair bir fikir edinmek için
[ilgili bağlantıya gözatın](https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx).

Her ne kadar resmi kaynaklarda kullanımın sınırları ([throttling](https://en.wikipedia.org/wiki/Throttling_process_(computing) gibi)) belirtilmemişse de geliştirici servise fazla yüklenmemeyi göz önünde
bulundurmalıdır.

# Yükleme

`pip` ile yükleme yapabilirsiniz.

    pip install pynvi

# Kullanım

## Vatandaş Sorgulama

`pynvi.verify_identity` metodu ile vatandaş sorgusu yapabilirsiniz.

| Argüman | Tür | Varsayılan |
|---------|-----|------------|
| identity_number | int | - |
| name            | str | - |
| surname         | str | - |
| year_of_birth   | int | - |

### Örnekler

```python
pynvi.verify_identity(11111111111, "ERAY", "ERDİN", 1994)
# True
```

 > #### Uyarı
 > NVİ, `name` ve `surname` değerlerini hepsi büyük harf olarak kabul
 > etmektedir. Ad ve soyadın hepsinin büyük harf olmaması durumunda
 > ise `False` döndürmektedir. Bu kütüphane, `name` ve `surname`
 > değerlerinizi otomatik olarak büyük harfe döndürmeyecektir. Bunu
 > sizin sağlamanız beklenmektedir.

```python
# Eğer yukarıdaki örnek doğruysa
pynvi.verify_identity(11111111111, "Eray", "Erdin", 1994)
# False
pynvi.verify_identity(11111111111, "eray", "erdin", 1994)
```

 > #### Uyarı
 > Sunuucu tarafından bir hata geldiğinde bu size klasik bir
 > `Exception` ile yansıtılacaktır.

```python
try:
    pynvi.verify_identity(11111111111, "ERAY", "ERDİN", 1994)
except Exception as e:
    # bir hata var ise buradayız
    # birçok sebepten sunucu hata verebilir
    # sunucu meşgul ya da düşmüş olabilir
    print(e)
```
