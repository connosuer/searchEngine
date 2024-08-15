from ruamel.yaml import YAML

CRED_FILE_PATH = '/Users/samys/searchEngine.yaml'
COUNTRY = "US"

SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&gl=" + COUNTRY
RESULT_COUNT = 20

def get_credentials():
    creds = None
    with open(CRED_FILE_PATH) as stream:
        yaml = YAML(typ = 'safe')
        creds = yaml.load(stream)
    return creds