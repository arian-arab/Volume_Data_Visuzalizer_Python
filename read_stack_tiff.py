import numpy as np
import easygui
from pims import ImageSequence

class read_stack_tiff:            
    def load(self):
        file_path = easygui.fileopenbox(filetypes = "*.tiff", multiple=False)
        images = ImageSequence(file_path)
    
        v_data = np.zeros((images.frame_shape[1],images.frame_shape[2],images.frame_shape[0]))
        for i in range(images.frame_shape[0]):
            v_data[:,:,i] = images[0][i,:,:]
        
        y_data = np.linspace(1,1+v_data.shape[0],v_data.shape[0])
        x_data = np.linspace(1,1+v_data.shape[1],v_data.shape[1])
        z_data = np.linspace(1,1+v_data.shape[2],v_data.shape[2])
        self.x_data = x_data
        self.y_data = y_data
        self.z_data = z_data
        self.v_data = v_data