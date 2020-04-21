#!/usr/bin/env python
"""sandman2ctl is a wrapper around the sandman2 library, which creates REST API
services automatically from existing databases."""

import argparse
from sandman2 import get_app
import tkinter as tk
from tkinter import filedialog
import os
import json

current_path = os.path.dirname(os.path.realpath(__file__))

def browse_file_path(title_text="Choose File"):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes =(("json files", "*.json"),("All Files","*.*")),
                           title = title_text)
    return file_path


def copy_file_to(copyto,replace_file = False,title_text = 'Choose File'):
    already_exist = os.path.exists(copyto)
    if already_exist and not replace_file:
        print("File already exists")
    else:
        c_driver = browse_file_path(title_text=title_text)
        cdriver = None
        with open(c_driver,'rb') as f:
            cdriver = f.read()
        with open(copyto,'wb') as f:
            f.write(cdriver)
        print(f'copied {c_driver} to {copyto}')

copy_file_to(current_path +r'\dbdata.json')

def pgconnstring():
    connstring = None
    dbdata_file = os.path.join(current_path,'dbdata.json')
    with open(dbdata_file,'r',encoding='utf-8') as f:
        jobj = json.load(f)[0]
        user = jobj['user']
        password = jobj['password']
        host = jobj['host']
        dbname = jobj['dbname']
        connstring = f'postgresql+psycopg2://{user}:{password}@{host}/{dbname}'
    return connstring





def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='Auto-generate a RESTful API service '
        'from an existing database.'
        )

    #uri here
    URI = pgconnstring()

    # parser.add_argument(
    #     'URI',
    #     help='Database URI in the format '
    #          'postgresql+psycopg2://user:password@host/database')
    
    parser.add_argument(
        '-d',
        '--debug',
        help='Turn on debug logging',
        action='store_true',
        default=False)

    parser.add_argument(
        '-p',
        '--port',
        help='Port for service to listen on',
        default=5000)
    parser.add_argument(
        '-l',
        '--local-only',
        help='Only provide service on localhost (will not be accessible'
             ' from other machines)',
        action='store_true',
        default=False)
    parser.add_argument(
        '-r',
        '--read-only',
        help='Make all database resources read-only (i.e. only the HTTP GET method is supported)',
        action='store_true',
        default=False)
    parser.add_argument(
        '-s',
        '--schema',
        help='Use this named schema instead of default',
        default=None)

    parser.add_argument(
        '-e',
        '--enable-cors',
        help='Enable Cross Origin Resource Sharing (CORS)',
        default=False)


    args = parser.parse_args()
    app = get_app(URI, read_only=args.read_only, schema=args.schema)
    if args.enable_cors:
        from flask_cors import CORS
        CORS(app)
    if args.debug:
        app.config['DEBUG'] = True
    if args.local_only:
        host = '127.0.0.1'
    else:
        host = '0.0.0.0'
    app.config['SECRET_KEY'] = '42'
    app.run(host=host, port=int(args.port))


if __name__ == '__main__':
    main()
