import cmd
from JsonLoader import JsonLoader, SQLFile

class CmdController(cmd.Cmd):
    init = 'Welcome to simple SQL generator for PostgreSQL'
    prompt = 'sql-gen> '
    __generated = ''

    def do_json2sql(self, arg):
        'Generate SQL code from json file'

        filename = arg
        sql_file = JsonLoader.parseJson(JsonLoader.loadFile(filename))

        CmdController.__generated = str(sql_file)

    def do_show(self, arg):
        'Show sql generated code'

        print(CmdController.__generated)
        


    def do_save(self, arg):
        'Save current generated SQL'
        if CmdController.__generated == '':
            print('No sql generated')
            return

        filename = arg

        if filename == '':
            print('Please, typing filename where SQL code will be saved')
            return

        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(CmdController.__generated)
        


