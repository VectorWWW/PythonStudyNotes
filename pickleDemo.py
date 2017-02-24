import pickle

# define the class before unpickle
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer       = Bird() 
fn     = 'a.pkl'
with open(fn, 'w') as f:                     # open file with write-mode
    picklestring = pickle.dump(summer, f)   # serialize and save object
with open(fn, 'r') as f:
    summer = pickle.load(f)   # read file and build object