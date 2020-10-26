import h5py
import numpy as np
import easygui

class read_h5_file:    
    def load(self):
        file_path = easygui.fileopenbox(filetypes = "*.h5", multiple=False)
        if file_path is not None:
            file_path = easygui.fileopenbox(filetypes = "*.h5", multiple=False)
            hdf5 = h5py.File(file_path, 'r')
            h5_file = hdf5.get('Matrix')
            scale = h5_file.attrs.__getitem__('IGORWaveScaling')
            note = h5_file.attrs.__getitem__('IGORWaveNote')
            units = h5_file.attrs.__getitem__('IGORWaveUnits')
            matrix = np.array(h5_file)
            hdf5.close()

            if len(matrix.shape)>2:
                v_data = matrix
                x_data = np.linspace(scale[2][1],scale[2][1]+v_data.shape[1]*scale[2][0],v_data.shape[1])
                y_data = np.linspace(scale[1][1],scale[1][1]+v_data.shape[0]*scale[1][0],v_data.shape[0])
                z_data = np.linspace(scale[3][1],scale[3][1]+v_data.shape[2]*scale[3][0],v_data.shape[2])
            else:
                v_data = np.zeros([matrix.shape[0],matrix.shape[1],1])
                v_data[:,:,0] = matrix
                x_data = np.linspace(scale[2][1],scale[2][1]+v_data.shape[1]*scale[2][0],v_data.shape[1])
                y_data = np.linspace(scale[1][1],scale[1][1]+v_data.shape[0]*scale[1][0],v_data.shape[0])
                z_data = 0;

            self.x_data = x_data
            self.y_data = y_data
            self.z_data = z_data
            self.v_data = v_data
            self.note = note
            self.units = units
            