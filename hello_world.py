import logging

logging.basicConfig(
    filename='./hello_world_app.log', 
    encoding='utf-8', 
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s'
    )

logging.info('*** Started Hello World Reader App ***')
logging.debug('Importing JSON module...')
import json
logging.debug('Imported JSON module.')
logging.debug('Importing OS module...')
import os
logging.debug('Imported OS module.')

logging.info('Reading defined environment variables from vars/env_vars.json')
vars_file = open("vars/env_vars.json")
logging.debug('Parsing vars/env_vars.json into python dict')
env_vars = json.load(vars_file)
vars_file.close()

logging.debug('Start looping environment variables')
for var in env_vars["env_vars"]:
    logging.debug('Searching environment variables for: ' + var["key"])
    value = os.getenv(var["key"], default="null")
    if value != "null":
        logging.info(var["key"] + ' exists with value of: ' + value)
        print("Name: " + var["key"] + "    Value: " + value)
        logging.debug('Environment variable details outputted to console')
    else:
        logging.error(var["key"] + " environment variable does not exist")

logging.info('Exiting app')
logging.info('*** Stopped Hello World Reader App ***')
