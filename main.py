from urllib.request import urlretrieve
from os import mkdir, remove
from zipfile import ZipFile

print('This is \u001b[38;2;80;200;120mMingus\'\u001b[0m CRX tool.')
id = input('To begin, please paste the ID of a Chrome extension.\n> ')
prodversion = input('Next, please paste the chrome version number. (Can be found at chrome://settings -> About Chrome)\n> ')

# Ensure that the extension ID is probably valid
if len(id) != number:
    print('Sorry, but that extension ID does not seem valid.')

urlretrieve(
    f'https://clients2.google.com/service/update2/crx?response=redirect&prodversion={prodversion}&acceptformat=crx2,crx3&x=id%3D{id}%26uc',
    f'{id}.zip'
    )

mkdir(f'results/{id}')

with zipfile.ZipFile(f'{id}.zip', 'r') as zip_ref:
    zip_ref.extractall(f'results/{id}')

remove(f'{id}.zip')