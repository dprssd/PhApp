import psycopg2
import pandas as pd
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print(f"Server version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE panel(
    #             id serial PRIMARY KEY,
    #             name varchar(50) NOT NULL,
    #             power float NOT NULL,
    #             CPD float NOT NULL,
    #             square float NOT NULL,
    #             voltage_xx float NOT NULL,
    #             voltage_mppt float NOT NULL,
    #             operating_temp float NOT NULL,
    #             I_sc float NOT NULL,
    #             I_mmpt float NOT NULL,
    #             temp_coef_p float NOT NULL,
    #             temp_coef_i float NOT NULL,
    #             cost float NOT NULL)"""
    #     )
    #     print("[INFO] Table create successfull")

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE weather_data(
        #             id serial PRIMARY KEY,
        #             hours integer NOT NULL,
        #             wind_speed float NOT NULL,
        #             air_temp float NOT NULL,
        #             pressure float NOT NUll,
        #             direct_solar_rad float NOT NULL,
        #             scattered_solar_rad float NOT NULL,
        #             sum_solar_rad float NOT NULL
        #             )"""
        #     )
        #     print("[INFO] Table create successfull")

except Exception as ex:
    print(f"[INFO] Error while working with PostgreSQL", ex)

with pd.ExcelFile()

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL conncetion closed")