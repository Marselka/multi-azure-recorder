#from typing import Union

from fastapi import FastAPI

import subprocess
import os

this_file_path = os.path.dirname(os.path.abspath(__file__))
executable = os.path.join(this_file_path, 'Azure-Kinect-Sensor-SDK/build/bin/mrob_recorder')

processes = []
    
app = FastAPI()


@app.get("/get_connected_camera_list")
def get_connected_camera_list():
    connected_camera_list = subprocess.check_output([f'{executable}', '--list']).decode('utf-8') # Get connected camera list
    return {"connected_camera_list": connected_camera_list}
    #return connected_camera_list

@app.post("/launch_recorder")
async def launch_recorder(data: dict):

    # Create path
    path = os.path.join('records', file_base_name)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    os.chdir(path)

    print(data['cmd_line'].split())
    p = subprocess.Popen()
    processes.append(p)
    return 0

@app.get("/stop_recorder")
def stop_recorder():
    return 0


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {'govno' : 'adasdadsfdf d233242345 dfwe'}#{"item_id": item_id, "q": q}