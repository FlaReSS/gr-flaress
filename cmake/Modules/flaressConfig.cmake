INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FLARESS flaress)

FIND_PATH(
    FLARESS_INCLUDE_DIRS
    NAMES flaress/api.h
    HINTS $ENV{FLARESS_DIR}/include
        ${PC_FLARESS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FLARESS_LIBRARIES
    NAMES gnuradio-flaress
    HINTS $ENV{FLARESS_DIR}/lib
        ${PC_FLARESS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FLARESS DEFAULT_MSG FLARESS_LIBRARIES FLARESS_INCLUDE_DIRS)
MARK_AS_ADVANCED(FLARESS_LIBRARIES FLARESS_INCLUDE_DIRS)

