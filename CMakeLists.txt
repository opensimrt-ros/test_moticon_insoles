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
	#catkin_add_nosetests(test) ## this is already an integration test and needs a master. I dont know how was it working before, but it isnt now

  add_rostest(test/republisher.test)
endif()
