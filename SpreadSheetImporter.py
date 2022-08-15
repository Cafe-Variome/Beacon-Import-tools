from Shared.utils import client

import argparse

from parsers.xlsxParser import responseParser

from Shared.info import infoModel


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", help="path to the spreadsheet to be imported", required=True)
	args = parser.parse_args()
	if args.f is None:
		print("need to provide F")
		quit()
	infoModel.from_dict(responseParser(args.f).to_dict())


if __name__ == "__main__":
	main()