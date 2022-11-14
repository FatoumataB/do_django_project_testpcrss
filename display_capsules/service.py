import os
import requests
import sqlite3
import json


from django.shortcuts import render
from django.http.response import JsonResponse

def get_capsules():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    capsules = r.json()
    capsule_list = []
    for i in range(len(capsules['capsules'])):
        capsule_list.append(capsules['capsules'][i])
    return capsule_list
    conn = sqlite3.connect('web_scrapy')
    capsuledata= json.load(capsules)
    
    columns = []
    column = []
    for data in capsuledata:
        column = list(data.keys())
        for col in column:
            if col not in columns:
                columns.append(col)


    value = []
    values = []
    for data in newegg_json:
        for i in columns:
            value.append(str(dict(data).get(i)))
    values.append(list(value))
    value.clear()

    create_query = 'create table if not exists capsules (flight_number, mission_name, launch_year,launch_date_unix,launch_date_utc, launch_date_local,rocket,second_stage)'
    insert_query = 'insert into capsules values (?,?,?,?,?,?,?,?)'
    c = conn.cursor()
    c.execute(create_query)
    c.executemany(insert_query, values)
    conn.commit()
    c.close()