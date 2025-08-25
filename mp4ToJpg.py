# ##### BEGIN GPL LICENCE BLOCK #####
#  Copyright (C) 2025  Arthur Langlard
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENCE BLOCK #####


# Start of the project: 27-10-2024
# Last modification: 25-10-2025


import av
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*', help="Files")
args = parser.parse_args()
print(args.files)
filenames = [filename for filename in args.files if filename[-4:]==".avi" or filename[-4:]==".mp4"]


for filename in filenames:
    container  = av.open(filename)
    directory_name = filename[:-4] + "-frames"

    # Create the directory
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        pass

    for index, frame in enumerate(container.decode(video=0)):
            frame.to_image().save(directory_name + f'\\frame-{index:04d}.jpg')
