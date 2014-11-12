#!/usr/bin/env python 

import urllib2
import json

tomatoe_api = 'krzzdufmpnnbcv4evzufshcd'


def tomatoe_search(query): 
	api_key = tomatoe_api
	movie = query.replace(' ', '+')
	url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + api_key + '&q=' + movie + '&page_limit=1'
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)
	critic = data['movies'][0]['ratings']['critics_score']
	synopsis = data['movies'][0]['synopsis']
	poster = data['movies'][0]['posters']['profile']
	release_date = data['movies'][0]['release_dates']['theater']
	cast = ''
	for item in data['movies'][0]['abridged_cast']:
		cast = cast + item['name'] + ' '
	print critic, synopsis, poster, release_date, cast

tomatoe_search('Skyfall')


