import json
import progressbar
import requests

from Shared.conf import endpoints

from parsers.infoParser import responseParser

from Shared.info import infoModel


def handle_instance(url):
	"""
	Take a single Beacon instance, scrape the /info endpoint for relevant info and then store within mongoDB
	:param url:
	:return: null
	"""
	instance_response = requests.get(F"{url}/info")
	if instance_response.ok:
		infoModel.from_dict(responseParser(json.loads(instance_response.text)).to_dict())


def main():
	for instance in progressbar.progressbar(endpoints):
		handle_instance(instance)


if __name__ == "__main__":
	main()
