import json
from Shared.utils import client


class infoModel:

	@classmethod
	def from_dict(cls, dict):
		return cls(dict["id"], dict["name"], dict["description"], dict["homepage"], dict["resourceTypes"],
		           dict["apiVersions"])

	def __init__(self, id, name, description, homepage, resourceTypes, apiVersions):
		"""
		Take in info about a dataset
		check to see if the dataset exists within mongoDB
		if it does exist then check for any updates, if there are updates then update the DB accordingly
		if it does not exist then add it in to the DB
		:param response_json:
		"""
		self.id = id
		self.name = name
		self.description = description
		self.homepage = homepage
		self.resourceTypes = resourceTypes
		self.apiVersions = apiVersions
		self.exists = self.check_db_existence()
		if self.exists:
			if self.changes_found():
				# differences found between /info response and DB, update DB
				client.beacon.datasets.update_one({"id": self.id}, {"$set": self.to_dict()})
		else:
			# entry does not exist in the DB so create it
			client.beacon.datasets.insert_one(self.to_dict())

	def check_db_existence(self):
		response = client.beacon.datasets.find({"id": self.id})
		return True if len(list(response)) else False

	def changes_found(self):
		"""
		Check to see if there are differences between the info provided by the endpoint/SS and the stored info in the DB
		:return:
		"""
		try:
			stored = client.beacon.datasets.find({"id": self.id}, {"_id": 0})
			return json.dumps(stored[0]) != self.to_json()
		except:
			# if anything goes wrong such as no EJP-ID defined in the beacon's /info or there are no results within
			# mongoDB then return True so the Beacon's info is scraped
			return True

	def to_json(self):
		"""
		return this object as a JSON structure
		:return: JSON
		"""
		return json.dumps(self.to_dict())

	def to_dict(self):
		"""
		return this object as a python dict structure
		deletes the 'exists' key as this does not form part of the model
		:return: JSON
		"""
		base = dict(self.__dict__)
		del base['exists']
		return base
