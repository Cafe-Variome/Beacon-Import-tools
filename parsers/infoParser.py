import json


class responseParser:

	def __init__(self, response_json):
		self.id = self.get_ejp_id(response_json)
		self.name = self.get_name(response_json)
		self.description = self.get_description(response_json)
		self.homepage = self.get_homepage(response_json)
		self.resourceTypes = self.get_resourceTypes(response_json)
		self.apiVersions = self.get_apiVersions(response_json)

	def get_ejp_id(self, response_json):
		"""
		Returns the EJP ID associated with a resource
		The ID is gathered from a resources /info endpoint or from the existing mongoDB
		:param response_json: JSON formatted /info contents
		:return: id
		"""
		return response_json["response"]["info"]["EJP-id"]

	def get_name(self, response_json):
		"""
		returns the resources name, this is a required field within Beacon so should exist
		:param response_json: JSON formatted /info contents
		:return: string
		"""
		return response_json["response"]["name"]

	def get_description(self, response_json):
		"""
		returns description
		:param response_json: JSON formatted /info contents
		:return: string
		"""
		return response_json["response"]["description"]

	def get_homepage(self, response_json):
		"""
		returns main URL of resource
		:param response_json: JSON formatted /info contents
		:return: string
		"""
		return response_json["response"]["welcomeUrl"]

	def get_resourceTypes(self, response_json):
		"""
		returns a list of resourceTypes
		:param response_json: JSON formatted /info contents
		:return: list
		"""
		return response_json["response"]["info"]["resourceTypes"]

	def get_apiVersions(self, response_json):
		"""
		returns all apiVersions as a dict
		:param response_json: JSON formatted /info contents
		:return: dict
		"""
		return response_json["response"]["info"]["apiVersions"]

	def to_json(self):
		"""
		return this object as a JSON structure
		:return: JSON
		"""
		return json.dumps(self.to_dict())

	def to_dict(self):
		"""
		return this object as a python dict structure
		OPTIONAL: delete keys before returning (none added here)
		:return: JSON
		"""
		base = dict(self.__dict__)
		return base
