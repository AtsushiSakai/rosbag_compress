# rosbag_compress
A Python comand line tool for multiple ROS bag files compression and decompression

This tool search bag files recrusively,

compress or compress them at same time.

It is executed in parallel process, so the task is done fastly.

This tool use the rosbag command line tool which is a default ROS tool.

[rosbag/Commandline - ROS Wiki](http://wiki.ros.org/rosbag/Commandline#compress "rosbag/Commandline - ROS Wiki")

## Usage

compress bag files under current dir.

> $ python rosbag_compress.py

compress bag files under /home/Desktop/bag

> $ rosrun common rosbag_compress -p /home/Desktop/bag

decompress bag files under /home/Desktop/bag

> $ rosrun common rosbag_compress -d -p /home/Desktop/bag

remove original files (*.orig.bag) under /home/Desktop/bag

> $ rosrun common rosbag_compress -r -p /home/Desktop/bag

# License

MIT
