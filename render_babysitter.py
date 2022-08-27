import subprocess
import os

class RenderBabysitter:
    def __init__(self, path_to_blend, output_path, frame_start: int, frame_end:int) -> None:
        self.path_to_blend = path_to_blend
        self.output_path = output_path
        self.frame_start = frame_start
        self.frame_end = frame_end
    
    def get_num_files_in_output_path(self):
        return len([name for name in os.listdir(self.output_path) if os.path.isfile(os.path.join(self.output_path, name))])


    def babysit(self):
        while self.get_num_files_in_output_path() < (self.frame_end - self.frame_start) + 1: # Plus 1 because it's inclusive
            current_start_frame = self.frame_start + self.get_num_files_in_output_path

            command = "blender " + self.path_to_blend
            command += " --frame-start " + str(current_start_frame)
            command += " --frame-end " + str(self.frame_end)
            command += " --render-format " + "PNG "
            command += " --render-output " + self.output_path
            command += " --use-extension 1"
            command += " --render-anim"

            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            process.wait()

