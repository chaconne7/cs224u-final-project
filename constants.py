import sys 
sys.path.append('..')
# import env

# Global constants.
DATA_FOLDER = 'data/'

DATA_PATH = 'data'
SOURCE_PATH = DATA_PATH + '/CLOTH'
DATA_TYPES = ['/high', '/middle']

DATA_SPLITS = ['/train', '/test', '/valid']
DEST_PATH = DATA_PATH + '/cleaned'
TRAIN_DEST_PATH = DEST_PATH + '/train'
TEST_DEST_PATH = DEST_PATH + '/test'
VALID_DEST_PATH = DEST_PATH + '/valid'