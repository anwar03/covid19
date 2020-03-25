import csv
from django.core.management import BaseCommand
from contact.models import Country


class Command(BaseCommand):
    """ Import country data from countries csv to country table"""
    def ImportCountry(self):
        with open('countries.csv', encoding='utf-8') as country_file:
            countries = csv.reader(country_file)
            for country in countries:
                name = country[0]
                country_code = country[2]
                dialing_code = country[1]
                print(name, dialing_code, country_code)
                try:
                    country, created = Country.objects.get_or_create(
                        name=name,
                        country_code2=country_code,
                        dialing_code=dialing_code
                    )

                    if created:
                        country.save()
                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this Country: {}\n{}".format(name, str(ex))
                    print(msg)
                    return msg

    def handle(self, *args, **options):
        """Called ImportCountry function for import country from country csv file."""
        self.ImportCountry()
