import re
import networkx as nx

current_dir = '/'

# RE to extract the last work after cd 
cd_pattern = r'\$ cd (\w+)$'

def cd(to):
    '''CD from current dir to the specified sub-folder.'''


with open('input.txt', 'r') as f:
    for line in f:
        command = line.strip()
        cd_match = re.search(cd_pattern, command)
        if cd_match:
            to = cd_match.group(1)
            cd(to)
