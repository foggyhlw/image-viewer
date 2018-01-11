import glob
import re
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cbook as cbook
import matplotlib
from shutil import copyfile
import subprocess

torrent_name=1
torrent_dir=''

def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)

def save_torrent():
    global torrent_name
    global torrent_dir
    print(type(torrent_name))
    print(type(torrent_dir))
    if len(torrent_dir)!=0:
        copyfile(torrent_dir[0],os.path.join\
                 ('E:\\new','{}.torrent'.format(str(torrent_name))))
    torrent_name=torrent_name+1

def kill_py():
    subprocess.call("tskill pythonw")

import keyboard
keyboard.add_hotkey('d',save_torrent)
keyboard.add_hotkey('x',kill_py)
##keyboard.wait('esc')
#filename=os.path.join(os.getcwd(),'1.jpg')

#img=io.imread(filename)
#viewer=ImageViewer(img)
#viewer.show()

#os.chdir("E:/自编程序/github/Temp/sis/torrent/1")

import os
for root, dirs, files in os.walk("E:\\自编程序\\github\\Temp\\sis\\3", topdown=True):
##for root, dirs, files in os.walk("E:\\new", topdown=True):
    if len(files)!=0 :
        print('pics number:  '+str(len(files)-1))
        n=0
        for name in files:
            n=n+1
            print(n)
            if name[-3:]=='jpg':
                torrent_dir=glob.glob(os.path.join(root,'*.torrent'))
                #print(torrent_dir)
                flag=False
                imgname=os.path.join(root,name)
                image_file=cbook.get_sample_data(imgname)
##                img=io.imread(imgname)
##                viewer=ImageViewer(img)
##                viewer.show()
                print(matplotlib.get_backend())
                fig=plt.figure()
                mng = plt.get_current_fig_manager()
                mng.window.state('zoomed')
                move_figure(fig,0,0)
                ax=fig.add_subplot(1,1,1)
                ax.axes.get_xaxis().set_visible(False)
                ax.axes.get_yaxis().set_visible(False)
                img=mpimg.imread(image_file)
                imgplot=plt.imshow(img)
                fig.show()
                keyboard.wait('n')
                plt.close('all')
                
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
