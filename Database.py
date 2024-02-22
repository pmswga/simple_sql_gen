
class Table:
    def __init__(self, name: str = '', columns: list[dict] = []) -> None:
        self.name = name
        self.columns = columns

    def __str__(self) -> str:
        code = []

        code.append('CREATE TABLE {}'.format(self.name))
        code.append('(')

        for i in range(len(self.columns)):
            col = self.columns[i]
            col_code = []

            if 'name' in col.keys():
                col_code.append(col['name'])

            if 'type' in col.keys():
                col_code.append(col['type'])

            if 'indexes' in col.keys():
                col_code.append(col['indexes'])

            if i+1 != len(self.columns):
                code.append(' '.join(col_code) + ',')
                continue

            code.append(' '.join(col_code))


        code.append(')')

        return '\n'.join(code) + ';'


class Database:
    def __init__(self, name: str = '') -> None:
        self.name = name
        self.tables = []

    def __str__(self) -> str:
        code = []

        code.append('CREATE DATABASE {}'.format(self.name))

        return '\n'.join(code) + ';'


class SQLFile:
    def __init__(self, db: Database = None, tables: list[Table] = []) -> None:
        self.database = db
        self.tables = tables

    def __str__(self) -> str:
        code = []

        code.append(str(self.database))

        for t in self.tables:
            code.append('\n')
            code.append(str(t))

        return '\n'.join(code)



# db = Database('my_db')
# tb = Table('Users', [{'name': 'sn', 'type': 'int', 'indexes': 'primary key'}])

# sql_file = SQLFile(db, tb)

# print(sql_file)
