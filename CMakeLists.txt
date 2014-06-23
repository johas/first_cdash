cmake_minimum_required (VERSION 2.6)
project (Tutorial)
#The first two lines together with add_executable is enough
#Here I add version number.
# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
 
# configure a header file to pass some of the CMake settings
# to the source code
# does this system provide the log and exp functions?
#include_directories ("/usr/share/cmake-2.8/Modules")
set (CMAKE_ROOT "/usr/share/cmake-2.8")
include (${CMAKE_ROOT}/Modules/CheckFunctionExists.cmake)
check_function_exists (log HAVE_LOG)
check_function_exists (exp HAVE_EXP)

configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
 
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# should we use our own math functions?
option (USE_MYMATH 
  "Use tutorial provided math implementation" OFF)
#Strange when on USE_MYMATH is false if OFF it is true

# add the MathFunctions library?

if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions) 
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)



#To enable test cases, if not add_test will not be read
#enable_testing()

# enable dashboard scripting
include (CTest)
#Now enable_testing called by Ctest


add_executable (Tutorial.x tutorial.cxx)
target_link_libraries (Tutorial.x  ${EXTRA_LIBS})
# add the install targets
install (TARGETS Tutorial.x DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"        
         DESTINATION include)

#test cases, Last step of step3

# does the application run
#add_test (TutorialRuns Tutorial.x 25)
 
# does it sqrt of 25
#add_test (TutorialComp25 Tutorial.x 25)
 
#Instead of adding tests like these we can define a macro, check uncommented
# below
#set_tests_properties (TutorialComp25 
#  PROPERTIES PASS_REGULAR_EXPRESSION "25 is 5") #read output, instead of
##using grep from output file
# 
## does it handle negative numbers
#add_test (TutorialNegative Tutorial.x -25)
#set_tests_properties (TutorialNegative
#  PROPERTIES PASS_REGULAR_EXPRESSION "-25 is 0")
# 
## does it handle small numbers
#add_test (TutorialSmall Tutorial.x 0.0001)
#set_tests_properties (TutorialSmall
#  PROPERTIES PASS_REGULAR_EXPRESSION "0.0001 is 0.01")
# 
## does the usage message work?
#add_test (TutorialUsage Tutorial.x)
#set_tests_properties (TutorialUsage
#  PROPERTIES 
#  PASS_REGULAR_EXPRESSION "Usage:.*number")
#
#macro testcase more convenient in this case
#define a macro to simplify adding tests, then use it
macro (do_test arg result)
  add_test (TutorialComp${arg} Tutorial.x ${arg})
  set_tests_properties (TutorialComp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result})
endmacro (do_test)
 
# do a bunch of result based tests
do_test (25 "25 is 5")
do_test (-25 "-25 is 0")
do_test(0.0001 "0.0001 is 0.01")
