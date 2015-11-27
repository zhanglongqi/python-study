#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 27/Nov/15 11:19

"""
import json
import urllib.parse
import urllib.request

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid=2460286"

yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"

result = urllib.request.urlopen(yql_url).read()
data = json.loads(str(result, encoding='utf8'))
print(data['query']['results'])
