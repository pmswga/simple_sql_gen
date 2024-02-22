import json
import os

from Database import SQLFile, Database, Table

class JsonLoader:
    
    @staticmethod
    def loadFile(filename: str) -> str:
        data = None

        with open(filename, 'r', encoding='UTF-8') as fp:
            data = fp.read()

        return data


    @staticmethod
    def parseJson(json_string: str) -> SQLFile:
        json_dump = dict(json.loads(json_string))

        database = Database()

        if 'name' in json_dump.keys():
            database.name = json_dump['name']


        tables = []

        if 'tables' in json_dump.keys():
            for _t in json_dump['tables']:
                tables.append(
                    Table(_t['name'], _t['columns'])
                )


        return SQLFile(database, tables)
