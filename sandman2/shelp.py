import os

from pathlib import Path
configfilepath = os.path.join(Path.home(),'recenttables.txt')


def config_file():
    if os.path.exists(configfilepath):
        uinput = input('load recent/new :')
        if uinput =='recent':
            with open(configfilepath,'r',encoding='utf-8') as f:
                recent_tables = f.read()
                return list(set(recent_tables.split(',')))
        if uinput =='new':
            tablename = input('input new tbale name :')
            with open(configfilepath,'a',encoding='utf-8') as f:
                f.write(f',{tablename}')
            return [tablename]
    else:
        tablename = input('input new tbale name :')
        with open(configfilepath,'a',encoding='utf-8') as f:
            f.write(tablename)
        return [tablename]



if __name__ == "__main__":
    print(config_file())
