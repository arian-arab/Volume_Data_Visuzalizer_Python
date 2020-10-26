import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider

class volume_data:
    def __init__(self,data):
        self.x_data = data.x_data
        self.y_data = data.y_data
        self.z_data = data.z_data
        self.v_data = data.v_data    

    def permute(self):
        """ permutes x,y and z in right-order """
        x_data = self.x_data
        y_data = self.y_data
        z_data = self.z_data
        v_data = self.v_data
        if v_data.shape[2]>1:
            self.v_data = np.transpose(v_data, (1,2,0))
            self.x_data = z_data
            self.y_data = x_data
            self.z_data = y_data
        volume_data.plot(self)

    def transpose(self):
        """ transpose color data (transpose image)"""
        x_data = self.x_data
        y_data = self.y_data
        z_data = self.z_data
        v_data = self.v_data
        self.v_data = np.transpose(v_data, (1,0,2))
        self.x_data = y_data
        self.y_data = x_data
        self.z_data = z_data
        volume_data.plot(self)

    def plot(self):
        """ to visualize 3d data set """
        x_data = self.x_data
        y_data = self.y_data
        z_data = self.z_data
        v_data = self.v_data

        fig, ax = plt.subplots(nrows = 2, ncols = 2)
        plt.tight_layout()

        c_data = np.flipud(v_data[:,:,0])
        cdata_plot = ax[1][0].imshow(c_data, extent = [x_data[0],x_data[-1],y_data[0],y_data[-1]], cmap = cm.bwr, vmin = np.min(c_data), vmax = np.max(c_data))
        ax[1][0].set_xlim([np.min(x_data), np.max(x_data)])
        ax[1][0].set_ylim([np.min(y_data), np.max(y_data)])
        ax[1][0].set_aspect('auto')
        ax[1][0].axes.tick_params(direction='in', labelright = False, labeltop = False)
        ax[1][0].axes.set_position([0.1, 0.1, 0.65, 0.65])
        ax[1][0].axvline(0, color = 'b', lw = 0.5, linestyle="--")
        ax[1][0].axhline(0, color = 'r', lw = 0.5, linestyle="--")
        ax_10_position =  ax[1][0].axes.get_position()

        int_along_y_data = np.sum(c_data,0)
        int_along_y_plot = ax[0][0].plot(x_data,int_along_y_data,'r', lw = 1)
        ax[0][0].axes.set_position([ax_10_position.x0,ax_10_position.y0+ax_10_position.height,ax_10_position.width,0.2])
        ax[0][0].axes.tick_params(direction='in', labelbottom=False, labelleft=False, labelright = False, labeltop = False)
        ax[0][0].axes.set_facecolor((255/255,204/255,204/255))
        ax[0][0].set_xlim([np.min(x_data), np.max(x_data)])
        ax[0][0].set_ylim([np.min(int_along_y_data), np.max(int_along_y_data)])

        int_along_x_data = np.sum(c_data,1)
        int_along_x_plot = ax[1][1].plot(int_along_x_data,y_data,'b', lw = 1)
        ax[1][1].axes.set_position([ax_10_position.x0+ax_10_position.width,ax_10_position.y0,0.2,ax_10_position.height])
        ax[1][1].tick_params(direction='in', labelleft=False, labelbottom = False)
        ax[1][1].axes.set_facecolor((204/255,229/255,255/255))
        ax[1][1].set_xlim(np.min(int_along_x_data), np.max(int_along_x_data))
        ax[1][1].set_ylim(np.max(y_data), np.min(y_data))

        ax[0][1].axes.set_position([ax_10_position.x0+ax_10_position.width,ax_10_position.y0+ax_10_position.height,0.2,0.2])
        ax[0][1].tick_params(direction='in', labelleft=False, labelright = False, labeltop = False, labelbottom = False)
        ax[0][1].axes.set_facecolor((225/255,225/255,225/255))
        if v_data.shape[2]>1:
            int_along_z_data = np.sum(np.sum(v_data,0),0)
            ax[0][1].plot(z_data,int_along_z_data,'k', lw = 1)
            ax[0][1].set_xlim(np.min(z_data), np.max(z_data))
            ax[0][1].set_ylim(np.min(int_along_z_data), np.max(int_along_z_data))
            slider_vertical_line = ax[0][1].axvline(z_data[0])

            slider_ax = plt.axes([0, 0.01, 0.9, 0.03], facecolor='w')
            slider = Slider(ax = slider_ax, label = '', valmin = z_data[0], valmax = z_data[-1], valinit = z_data[0], valstep=z_data[1]-z_data[0])
            def slider_callback(val):
                slider_value = np.argmin(np.abs(z_data-slider.val)).astype(int)

                c_data = np.flipud(v_data[:,:,slider_value])
                cdata_plot.set_data(c_data)
                cdata_plot.set_clim(np.min(c_data), np.max(c_data))

                int_along_x_data = np.sum(c_data,1)
                int_along_x_plot[0].set_xdata(int_along_x_data)
                int_along_x_plot[0].axes.set_xlim(np.min(int_along_x_data), np.max(int_along_x_data))

                int_along_y_data = np.sum(c_data,0)
                int_along_y_plot[0].set_ydata(int_along_y_data)
                int_along_y_plot[0].axes.set_ylim(np.min(int_along_y_data), np.max(int_along_y_data))

                slider_vertical_line.set_xdata(slider.val)
            slider.on_changed(slider_callback)
        plt.show()