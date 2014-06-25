cmake_minimum_required (VERSION 2.6)
project (Python_project)
#The first two lines together with add_executable is enough
 
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
set (EXTRA_LIBS ${EXTRA_LIBS} linear_alg)

include_directories("${PROJECT_BINARY_DIR}")
#include_directories("${PROJECT_SOURCE_DIR}/heat_equation")
#add_subdirectory (heat_equation) 
#set (EXTRA_LIBS ${EXTRA_LIBS} heat_equation)
#include_directories("${PROJECT_SOURCE_DIR}/linear_alg")
#add_subdirectory (linear_alg) 
#set (EXTRA_LIBS ${EXTRA_LIBS} linear_alg)
#include_directories("${PROJECT_SOURCE_DIR}/visual-effects")
#add_subdirectory (visual-effects) 
#set (EXTRA_LIBS ${EXTRA_LIBS} visual-effects)
#link_directories("${PROJECT_SOURCE_DIR}/visual-effects",
#  "${PROJECT_SOURCE_DIR}/linear_alg", "${PROJECT_SOURCE_DIR}/heat_equation")


#To enable test cases, if not add_test will not be read
#enable_testing()

# enable dashboard scripting
include (CTest)
#Now enable_testing called by Ctest


#add_custom_command(OUTPUT myout.txt COMMAND python ../main.py)
add_custom_command(OUTPUT SET_SOURCE_FILES_PROPERTIES COMMAND python ../main.py)

#add_custom_target(MyDriverTarget ALL DEPENDS myout.txt)
add_custom_target(MyDriverTarget ALL DEPENDS SET_SOURCE_FILES_PROPERTIES)
 
