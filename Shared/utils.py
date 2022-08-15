from pymongo.mongo_client import MongoClient
import Shared.conf as conf

userSection = F"{conf.database_user}:{conf.database_password}@" if conf.database_user else ""
dbSection = F"{conf.database_host}:{conf.database_port}/{conf.database_name}{'?authSource='+ conf.database_auth_source if conf.database_auth_source else ''}"

client = MongoClient(F"mongodb://{userSection}{dbSection}")