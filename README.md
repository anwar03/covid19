# Coronavirus disease (COVID-19) Situation
Dockerizing Django rest framework with Postgres

## prerequisite

1. git
1. docker
1. docker-compose

## Install
### Want to use this project?

1. First clone repository:

    ```sh
    $ git clone https://github.com/anwar03/covid19.git
    ```

### Development

Uses the default Django development server.

1. Build the images and run the containers:

    ```sh
    $ docker-compose up
    ```
   
   ```sh
    $ docker-compose run web python project_base/manage.py import_covid19_data
    ```

    Test it out at [http://127.0.0.1:8000](http://127.0.0.1:8000). The "app" folder is mounted into the container.


# API
API for Current cases and more stuff about COVID-19 or the Novel Coronavirus Strain
http://127.0.0.1:8000

# Endpoints
|  GET Request  | Output  |
| ------------ | ------------ |
|  http://127.0.0.1:8000/api/covid19 | Returns data of all countries that has COVID-19 |
|  http://127.0.0.1:8080/api/covid19/newcase | Returns data of all countries of the new cases  |
|  http://127.0.0.1:8080/api/covid19/newcase/?country={country} | Returns data of each  country of the new cases by the parameter |
|  http://127.0.0.1:8080/api/covid19/countrydata | Returns data of all countries that has COVID-19 | 
|  http://127.0.0.1:8080/api/covid19/countrydata/?country={country} | Returns data of each country data by the parameter. |
|  http://127.0.0.1:8080/dashboard | Dashboard data total cases, recovery, and deaths. |
|  http://127.0.0.1:8080/dashboard/?country={country} | Returns the data of a country if it is equal to its country  |


### Sources: 

> https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
