from mp4file.mp4file import Mp4File

def find_metadata_atom(file, name):
    atom = file.find('.//%s//data' % name)
    return atom.get_attribute('data')