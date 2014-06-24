cmake_minimum_required (VERSION 2.6)
project (Python_Tutorial)
#The first two lines together with add_executable is enough
 
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")


#To enable test cases, if not add_test will not be read
#enable_testing()

# enable dashboard scripting
include (CTest)
#Now enable_testing called by Ctest


add_custom_command(OUTPUT myout.txt COMMAND python ../hello.py)

add_custom_target(MyDriverTarget ALL DEPENDS myout.txt)
 
