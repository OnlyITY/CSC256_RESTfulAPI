import pytest
import requests


def test_ddg0():
    # A list of all the last names of the Presidents of the US.
    presidentLastName = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren',
                         'Harrison', 'Tyler', 'Polk', 'Taylor', 'Filmore', 'Pierce', 'Buchanan', 'Lincoln',
                         'Johnson', 'Grant', ' Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland',
                         'McKinley', 'Roosevelt' 'Taft', 'Wilson', ' Harding', 'Coolidge', 'Hoover', 'Roosevelt',
                         'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
                         'Clinton', 'Bush']

    # url to search query via DuckDuckGo API for the Presidents of the United States
    url = 'https://api.duckduckgo.com/?q="presidents of the united states"&format=json'

    # Sends GET request and saves response via resp variable
    resp = requests.get(url)

    # resp then gets formatted into a JSON and saved via rsp_data variable
    rsp_data = resp.json()

    # Saves relatedtopics from rsp_data into related variable
    related = rsp_data["RelatedTopics"]

    # Searches through related for Text entries and adds it into search_result
    search_result = ""
    for results in related:
        search_result += results["Text"]

    # Assert statement
    for president in presidentLastName:
        assert president in search_result
