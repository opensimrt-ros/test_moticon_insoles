cmake_minimum_required(VERSION 3.0.2)
project(test_moticon_insoles)

find_package(catkin REQUIRED COMPONENTS
  moticon_insoles
  rospy
  rostest
)
catkin_package(
)
#############
## Testing ##
#############

## Add folders to be run by python nosetests
if(CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test)
endif()
