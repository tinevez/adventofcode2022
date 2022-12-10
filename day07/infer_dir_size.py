import re
from termcolor import colored
from anytree import Node, RenderTree, PreOrderIter

# RE to extract the last work after cd 
cd_pattern = r'\$ cd (\w+)$'

# RE to extract a file with its size
file_pattern = r'(\d+)\s+(.+)'

def cd(to):
    '''CD from current dir to the specified sub-folder.'''
    global current_dir

    # Detect if not already exsits.
    for c in current_dir.children:
        if c.name == to:
            current_dir = c
            return
    to_node = Node(to, parent=current_dir)
    current_dir = to_node

def store_file(file_name, file_size):
    '''Add specified file to the file tree.'''
    global current_dir
    for c in current_dir.children:
        if c.name == file_name and c.file_size:
            return
    file_node = Node(file_name, parent=current_dir, file_size=file_size)

def cd_root():
    global current_dir
    current_dir = root_node

def cd_parent():
    global current_dir
    current_dir = current_dir.parent

def print_tree():
    for pre, fill, node in RenderTree(root_node):
        if not hasattr(node, 'file_size'):
            if not hasattr(node, 'folder_size'):
                print('%s%s' % (pre, colored( node.name, 'green', attrs=['bold'])))
            else:
                print('%s%s - %s' % (pre, colored( node.name, 'green', attrs=['bold']), colored( str(node.folder_size), 'green')))
        else:
            print('%s%s - %d' % (pre, colored(node.name, 'blue'), node.file_size))

def get_node_size(node):
    '''*Recursively* computes the size of a node.'''

    # Is it a file?
    if hasattr(node, 'file_size'):
        return int(node.file_size)

    # It's folder.
    total_size = 0
    for c in node.children:
       total_size += get_node_size(c)
    node.folder_size = total_size
    return total_size


#------------------------------------------------------

# Folder tree structure stored as a tree.
root_node = Node('root')
current_dir = root_node

with open('input.txt', 'r') as f:
    for line in f:
        command = line.strip()

        # CD to root?
        if command == '$ cd /':
            cd_root()
            continue

        # CD to parent?
        if command == '$ cd ..':
            cd_parent()
            continue

        # CD to a subolfer?
        cd_match = re.search(cd_pattern, command)
        if cd_match:
            to = cd_match.group(1)
            cd(to)
            continue
        
        # Listing files after dir?
        file_match = re.search(file_pattern, command)
        if file_match:
            file_size = int(file_match.group(1))
            file_name = file_match.group(2)
            store_file(file_name, file_size)
        

# Compute sum size.
get_node_size(root_node)
print('\n\n\n\n\n------------------------------------------')
print('File system with total size:')
print_tree()
print('------------------------------------------')

# Get all the folders and sort them by size.
all_folders = [node for node in PreOrderIter(root_node) if hasattr(node, 'folder_size') ]
all_folders.sort(key=lambda x : x.folder_size)

# Iterate to find dirs with max size = 100000
max_folder_size = 100000
total_small_folder_size = 0
print('\n\n\n------------------------------------------')
print('           QUESTION 1')
print('------------------------------------------')
print('Folders with size at most %d:' % max_folder_size)
for node in all_folders:
    if node.folder_size > max_folder_size:
        continue
    print(' %10s - %d' % (node.name, node.folder_size ))
    total_small_folder_size += node.folder_size
print('\nSmall size for small folders: %d' % total_small_folder_size)



print('\n\n\n------------------------------------------')
print('           QUESTION 2')
print('------------------------------------------')

# Smallest node with size at least ....
total_disk_space    = 70000000
desired_free_space  = 30000000
total_used_space    = root_node.folder_size
current_free_space  = total_disk_space - total_used_space
space_to_free       = desired_free_space - current_free_space
print(' - %20s: %10d' % ('total disk space', total_disk_space))
print(' - %20s: %10d' % ('total used space', total_used_space))
print(' - %20s: %10d' % ('current free space', current_free_space))
print(' - %20s: %10d' % ('desired free space', desired_free_space))
print(' - %20s: %10d' % ('space to free', space_to_free))

# Find folder of size just above space to free
for node in all_folders:
    if node.folder_size > space_to_free:
        break
print('Best folder to delete: %s' % node)
