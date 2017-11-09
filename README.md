# poseSimulator

## Introduction
Pose simulator is for the generation of pose training data. 

Pose, as an important feature of human, is necessary to increase the tracking system. 

This is the result of Openpose. 

![PoseSimulator](http://www.consortium.ri.cmu.edu/data/openpose/OpenPose1.png)
![OpenPose](https://flintbox.com/file/download/10586)

With a pose data, we should be able to track human with a better result because of the information gain. However, it is difficult to get a large size of pose data currently. The basic focus on last recent years was on bounding boxes. Pose is much more difficult to lable by human. Here, we introduce our PoseSimulator, a tracking result based on human pose based on real world data. 

## Sample Input Data Format
inputData.txt
person1Pose person2Pose person3Pose ...
outputData.txt
person1Box person2Box person3Box

# Main executor
randomWalk.py
If you want to change parameters, please change the number on the top. (comments)
