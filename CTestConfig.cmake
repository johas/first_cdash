## This file should be placed in the root directory of your project.
## Then modify the CMakeLists.txt file in the root directory of your
## project to incorporate the testing dashboard.
## # The following are required to uses Dart and the Cdash dashboard
##   ENABLE_TESTING()
##   INCLUDE(CTest)
#set (CTEST_PROJECT_NAME "johannes-Latitude-E6530_Tutorial")
#
##For Nightly testing
##set(CTEST_NIGHTLY_START_TIME "01:00:00 UTC")
#
#set(CTEST_DROP_METHOD "http")
#set(CTEST_DROP_SITE "my.cdash.org")
#set(CTEST_DROP_LOCATION "/cdash/submit.php?project=johannes-Latitude-E6530_Tutorial")
#set(CTEST_DROP_SITE_CDASH TRUE)
# The abobe is the old one, and not working
## This file should be placed in the root directory of your project.
## Then modify the CMakeLists.txt file in the root directory of your
## project to incorporate the testing dashboard.
##
## # The following are required to submit to the CDash dashboard:
##   ENABLE_TESTING()
##   INCLUDE(CTest)
# This is the Downloaded CTestfile from cdash

set(CTEST_PROJECT_NAME "johannes-Latitude-E6530_Tutorial")
set(CTEST_NIGHTLY_START_TIME "00:00:00 EST")

set(CTEST_DROP_METHOD "http")
set(CTEST_DROP_SITE "my.cdash.org")
set(CTEST_DROP_LOCATION "/submit.php?project=johannes-Latitude-E6530_Tutorial")
set(CTEST_DROP_SITE_CDASH TRUE)
