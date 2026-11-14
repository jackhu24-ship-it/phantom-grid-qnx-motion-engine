cmake_minimum_required(VERSION 3.16)
project(PHANToM_GRID_QNX_Motion_Kernel LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Check if compiling under QNX Toolchain
if(DEFINED CMAKE_SYSTEM_NAME AND CMAKE_SYSTEM_NAME STREQUAL "QNX")
    message(STATUS "Configuring for BlackBerry QNX Neutrino RTOS")
    add_compile_options(-Vgcc_ntox86_64 -O3 -Wall -Wextra)
else()
    message(STATUS "Configuring for Host Native / QEMU Emulation")
    add_compile_options(-O3 -Wall -Wextra -pthread)
endif()

add_executable(qnx_motion_kernel qnx_motion_kernel.cpp)

if(NOT WIN32)
    target_link_libraries(qnx_motion_kernel pthread)
endif()
