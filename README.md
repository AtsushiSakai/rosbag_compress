# rosbag_compress
A python command line tool for compression or decompression of multiple ROS bag files

This tool searchs bag files recrusively,

compress or compress them at same time.

It is executed in parallel process, so the task is done fastly.

This tool uses the rosbag command line tool which is a default ROS tool.

[rosbag/Commandline - ROS Wiki](http://wiki.ros.org/rosbag/Commandline#compress "rosbag/Commandline - ROS Wiki")

## Usage

compress bag files under current dir.

> $ python rosbag_compress.py

compress bag files under /home/Desktop/bag

> $ python rosbag_compress.py -p /home/Desktop/bag

decompress bag files under /home/Desktop/bag

> $ python rosbag_compress.py -d -p /home/Desktop/bag

remove original files (*.orig.bag) under /home/Desktop/bag

> $ python rosbag_compress.py -r -p /home/Desktop/bag

# License

MIT
