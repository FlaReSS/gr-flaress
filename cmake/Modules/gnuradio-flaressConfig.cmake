find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_FLARESS gnuradio-flaress)

FIND_PATH(
    GR_FLARESS_INCLUDE_DIRS
    NAMES gnuradio/flaress/api.h
    HINTS $ENV{FLARESS_DIR}/include
        ${PC_FLARESS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_FLARESS_LIBRARIES
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

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-flaressTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_FLARESS DEFAULT_MSG GR_FLARESS_LIBRARIES GR_FLARESS_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_FLARESS_LIBRARIES GR_FLARESS_INCLUDE_DIRS)
