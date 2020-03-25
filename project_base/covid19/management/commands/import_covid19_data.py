import math
from django.core.management import BaseCommand
from datetime import date, timedelta, datetime
import pandas as pd
from covid19.models import Covid
from contact.models import Country

class Command(BaseCommand):

    def ImportCovid19Data(self):
        """ Import covid19 data from GitHub repository to covid19 table that manipulates everyday data."""

        confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
        deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
        recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

        confirmed_df = pd.read_csv(confirmed_url)
        deaths_df = pd.read_csv(deaths_url)
        recovered_df = pd.read_csv(recovered_url)

        DateList = self.dateParse(list(confirmed_df.columns))

        for tempCountry in confirmed_df['Country/Region']:

            for item in DateList:
                lat = confirmed_df[confirmed_df['Country/Region']==tempCountry]['Lat'][list(confirmed_df[ confirmed_df['Country/Region'] == tempCountry ].index)[0]]
                long = confirmed_df[confirmed_df['Country/Region']==tempCountry]['Long'][list(confirmed_df[ confirmed_df['Country/Region'] == tempCountry ].index)[0]]

                print(tempCountry, item, lat, long)

                temp_confirm = confirmed_df[ confirmed_df['Country/Region'] == tempCountry ][ item ][list(confirmed_df[ confirmed_df['Country/Region'] == tempCountry ].index)[0]]
                temp_death = deaths_df[ deaths_df['Country/Region'] == tempCountry ][ item ][list(deaths_df[ deaths_df['Country/Region'] == tempCountry ].index)[0]]
                temp_recover = recovered_df[ recovered_df['Country/Region'] == tempCountry ][ item ][list(recovered_df[ recovered_df['Country/Region'] == tempCountry ].index)[0]]

                confirm = 0 if math.isnan(float(temp_confirm)) else int(temp_confirm)
                death = 0 if math.isnan(float(temp_death)) else int(temp_death)
                recover = 0 if math.isnan(float(temp_recover)) else int(temp_recover)

                try:
                    country, created = Country.objects.get_or_create(
                        name=tempCountry,
                    )
                    if created:
                        country.save()
                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this Country: {}\n{}".format(tempCountry, str(ex))
                    print(msg)
                    return msg


                try:
                    covid, created = Covid.objects.get_or_create(
                        country = country,
                        confirmed = confirm,
                        death = death,
                        recovered = recover,
                        created_at = self.dateValidation(item),
                        latitude = lat,
                        longitude = long,
                    )
                    if created:
                        covid.save()
                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this Country: {}\n{}".format(tempCountry, str(ex))
                    print(msg)
                    return msg

    def handle(self, *args, **options):
        """Called ImportCovid19Data function for import covid 19 data from  github repository."""
        self.ImportCovid19Data()

    def dateParse(self, Dates):
        """" parse """
        dateList = list()
        for item in Dates:
            if self.dateValidation(item):
                dateList.append(item)
        return dateList

    def dateValidation(self, date_text ):
        try:
            dat = datetime.strptime(date_text, "%m/%d/%y").strftime('%Y-%m-%d')
            return dat
        except ValueError:
            return False
