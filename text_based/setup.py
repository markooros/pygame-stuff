from distutils.core import setup

setup(
    name="text_based_rpg",
    version="trunk",
    description="Ein text basiertes RPG",
    author="Marko Oros",
    author_email="markooros@googlemail.com",
    license="BSD-like",
    packages=["modules"],
    scripts=["game.py"],
)