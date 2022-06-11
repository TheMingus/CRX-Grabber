from urllib.request import urlretrieve
from os import mkdir, remove, rename, listdir
from zipfile import ZipFile
from json import load

print('This is \u001b[38;2;80;200;120mMingus\'\u001b[0m CRX tool.')
id = input('To begin, please paste the ID of a Chrome extension.\n> ')
prodversion = input('Next, please paste the chrome version number. (Can be found at chrome://settings -> About Chrome)\n> ')

# Ensure that the extension ID is probably valid
if len(id) != 32 or len([i for i in id if i.isnumeric()]) != 0:
    print('Sorry, but that extension ID does not seem valid.')
    quit()

urlretrieve(f'https://clients2.google.com/service/update2/crx?response=redirect&prodversion={prodversion}&acceptformat=crx2,crx3&x=id%3D{id}%26uc', f'results/{id}.zip')

mkdir('results/temp')

with ZipFile(f'results/{id}.zip', 'r') as zip_ref:
    zip_ref.extractall(f'results/temp')

with open(f'results/temp/manifest.json') as f:
    version = load(f).get('version')

for i in listdir('results'):
    if id in i and i.split('_')[1].split('.zip')[0] == version:
        print('The latest version of this extension has already been downloaded.')
        remove('results/temp')
        remove(f'{id}.zip')
        quit()

rename(f'results/{id}.zip', f'results/{id}_{version}.zip')

remove('results/temp')

print('Extension grabbed!')
