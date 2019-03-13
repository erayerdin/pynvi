from setuptools import setup

import pynvi

with open("README.md", "r") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    DEPS = f.readlines()

with open("dev.requirements.txt", "r") as f:
    DEPS_TEST = f.readlines()

GIT_URL = "https://github.com/erayerdin/pynvi/archive/{}.tar.gz"

setup(
    name="pynvi",
    version=pynvi.__version__,
    description="pynvi Türkiye Cumhuriyeti Nüfus ve Vatandaşlık İşleri Genel"
    " Müdürlüğü SOAP servisi için köprü bir Python kütüphanesidir.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/erayerdin/pynvi",
    download_url=GIT_URL.format(pynvi.__version__),
    packages=["pynvi"],
    include_package_data=True,
    keywords="pynvi nvi nüfus vatandaşlık işleri türkiye",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ],
    author=pynvi.__author__,
    author_email="eraygezer.94@gmail.com",
    license="Apache License 2.0",
    tests_require=DEPS_TEST,
    install_requires=DEPS,
    zip_safe=False,
)
