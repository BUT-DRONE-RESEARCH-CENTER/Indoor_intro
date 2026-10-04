# DRC Entry Task: Processing and Visualization of Sensor Data in ROS 2

Welcome to the entry task for newcomers to DRC! The goal of this task is to verify (or teach you) the basics of working with the Robot Operating System (ROS 2), which is an absolute standard in modern robotics. You will try working with recorded data (rosbag), creating your own script (node), and visualization.

**You can find this assignment, including the code template, at** [GitHub - BUT-DRONE-RESEARCH-CENTER/Indoor_intro · GitHub](https://github.com/BUT-DRONE-RESEARCH-CENTER/Indoor_intro)

---

## 💻 Are you running Windows? No problem!

If you do not have native Linux on your computer (dual boot), we recommend using one of the following options:

1. **WSL 2 (Windows Subsystem for Linux)** – *Recommended for performance:*

   - An improved terminal environment in Windows that allows Ubuntu to run directly.

   - In Windows 11, graphics (GUI) work automatically in WSL2 (WSLg), so you can run RViz2 in it without any problems. Simply enable WSL in the Windows command line (`wsl --install -d Ubuntu-22.04`) and install ROS 2 inside it.

   - **📁 How do you transfer files such as a rosbag (drone data) or the template script into WSL?**  
     In the WSL terminal, navigate to the folder where you want to store the files and enter the command:

     ```
     explorer.exe .
     ```

     *(The dot at the end is important!)* The command opens a standard Windows File Explorer window connected to Linux. You can simply drag and drop the downloaded file or template into it.

2. **Virtual machine (VirtualBox / VMware)** – *Easier to set up:*

   - Download [VirtualBox](https://www.virtualbox.org/) and install **Ubuntu Desktop (22.04 LTS)** in it.

   - Do not forget to allocate enough RAM to the virtual machine (ideally 4–8 GB), at least 2–4 CPU cores, and **enable 3D acceleration** in the graphics settings so that RViz2 runs smoothly.

---

## 🛠️ What you will need

- **Installed ROS 2** (e.g. Humble, Iron, or Jazzy) on Linux (Ubuntu 22.04 / 24.04).

- **RViz2** – visualization tool (part of the `ros-<distro>-desktop` package).

- Basic knowledge of Python.

- Basic familiarity with the Linux terminal.

---

## 📝 Task Assignment

## 0. Prepare the Python environment and ROS2

First, you need to set up a basic environment for Python to work properly on your PC. Python can run without an environment, but it will clutter (cause so-called pollution of) the overall system, making the work less organized.

https://docs.python.org/3/library/venv.html

Next, you need to add/install the ROS2 packages into this environment (in our case, the Humble version compatible with Ubuntu 22.04).

https://docs.ros.org/en/humble/Installation.html

### 1. Obtain the Dataset (Rosbag)

Download the prepared dataset containing real data from the movement of a robot/drone (e.g. GPS data, odometry, VIO).

- https://drive.google.com/file/d/1MF6iFzuq9PJtDL8rNpbJOpXDj5JGx6_0/view?usp=sharing

- *(Alternative for testing: You can download a sample VIO dataset from the [EuRoC MAV Dataset](https://www.research-collection.ethz.ch/entities/researchdata/bcaf173e-5dac-484b-bc37-faf97a594f1f))

### 2. Data Extraction to CSV (Write Your Own Node)

Your task is to complete the Python template (`node_template.py`), which behaves as a ROS 2 node.

#### 📋 List of Tasks (TODO) in the Code:

1. **Import messages:** Import the correct message type according to the topic in the dataset (e.g. `PoseStamped` or `Odometry`).

2. **CSV header:** Define the column names in the CSV file (`timestamp`, `x`, `y`, `z`).

3. **Subscriber:** Uncomment and configure `self.create_subscription()` with the correct message type and topic name.

4. **Timer:** Uncomment and configure `self.create_timer()` with a period of `0.1` s (10 Hz).

5. **Subscriber callback (**`**pose_callback**`**):** Store the received message in the variable `self.latest_msg`.

6. **Timer callback (**`**timer_callback**`**):** Extract the timestamp and X, Y, Z positions from the message.

7. **Write to CSV:** Write the extracted values as a new row in the CSV file.

#### 🚀 Running the Script

Once you have completed the code, remember to first source ROS 2 in the terminal and then run the script directly using Python:

```
source /opt/ros/<distro>/setup.bashpython3 node_template.py
```

⚠️ **Important: Loading the ROS 2 Environment (Sourcing)**  
Note that in every **newly opened terminal**, you must first load the ROS 2 environment. Without this, the system will not recognize commands such as `ros2` or `rviz2`, and Python will not find the `rclpy` library.

Run the command according to the installed version (replace `<distro>`, for example, with `humble`):

```
source /opt/ros/<distro>/setup.bash
```

*(Tip: If you do not want to type this command into every new terminal window, add it to the end of the* `*~/.bashrc*` *file.)*

---

### 3. Visualization in RViz2

While your script is running in the background, we also want to see the trajectory visually:

1. In the first terminal, navigate to the folder containing the dataset, source ROS, and start playing the bag:  
   `source /opt/ros/<distro>/setup.bash`  
   `ros2 bag play <name_of_folder_with_bag>`

2. In the second terminal, source ROS again and start the RViz2 visualization tool:  
   `source /opt/ros/<distro>/setup.bash`  
   `rviz2`

3. In RViz, set the correct **Fixed Frame** (usually `map` or `odom`; determine it from the data).

4. Add the trajectory visualization by clicking **Add** (bottom left) -> select the display type according to the topic (e.g. **Odometry** or **Path**).

5. Correctly configure the topic name so that RViz can see the data. A curve or arrows showing the path travelled by the robot will appear.

### 4. What to Submit

Once you have completed everything, send us:

1. The **source code** of your script (node) that stored the data.

2. The generated `**.csv**` **file** containing the collected data.

3. A **screenshot or short video** from RViz clearly showing the plotted trajectory of the robot.

Do not be afraid to Google things and use the official ROS 2 documentation or forums! Good luck, and we look forward to seeing your solution.
