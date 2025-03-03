from read_stack_tiff import read_stack_tiff
from volume_data import volume_data
from read_h5_file import read_h5_file

reader = read_stack_tiff()  
reader.load() 

# reader = read_h5_file()  
# reader.load() 

data = volume_data(reader)
data.plot()

data.permute()