def get_data():
    rows = []

    f = open('./train.txt', 'r')
    rows = f.readlines()
    f.close()

    return rows[0]

class Node:
    children_count = 0
    metadata_count = 0

    children = None
    metadata = None

def read_header(data):
    return int(data[0]), int(data[1]), data[2:]

def read_metadata(data, length):
    return data[-length:], data[0:-length]

def process_tree(tree, metadata):
    if tree:
        # Read header from left of tree
        children_count, metadata_count, header_tree = read_header(tree)

        if children_count == 0:
            new_metadata = header_tree[0:metadata_count]
            to_process = header_tree[metadata_count:]
        if children_count == 1:
            # Read metadata from right of tree
            new_metadata, to_process = read_metadata(header_tree, metadata_count)

        metadata.append(new_metadata)
        
        process_tree(to_process, metadata)

    return metadata


data = get_data()

tree = data.split(' ')

processed = process_tree(tree, [])

print(processed)
print(len(processed))

flat_list = [int(item) for sublist in processed for item in sublist]

print(sum(flat_list))