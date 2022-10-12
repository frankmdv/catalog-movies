import json

class Film:
    def __init__(self, name, synopsis, director):
        self.name = name
        self.synopsis = synopsis
        self.director = director

class Catalog:
    CATALOG_FILM_PATH = './catalog_movies.json'

    @classmethod
    def add_film(cls, film):
        catalog_data = cls.fetch_catalog()
        catalog_data[film.name] = { 'synopsis': film.synopsis, 'director': film.director }
        cls.__modify_catalog(catalog_data)

    @classmethod
    def remove_film(cls, name):
        catalog_data = cls.fetch_catalog()
        del catalog_data[name]
        cls.__modify_catalog(catalog_data)

    @classmethod
    def remove_catalog(cls):
        pass

    @classmethod
    def fetch_catalog(cls):
        with open(cls.CATALOG_FILM_PATH, 'r', encoding='utf-8') as jf:
            catalog_data = json.load(jf)

        return catalog_data

    @classmethod
    def __modify_catalog(cls, catalog_data):
        with open(cls.CATALOG_FILM_PATH, 'w', encoding='utf-8') as jf:
            json.dump(catalog_data, jf)
