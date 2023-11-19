C_CODE ?= 0
ifeq ($(C_CODE), 1)
# C
DEBUG ?= 1
ifeq ($(DEBUG), 1)
C_COMPILER_FLAGS = -g3 -Wall -std=c11
else
C_COMPILER_FLAGS = -O2 -Wall -std=c11
endif

C_COMPILER_CALL = $(C_COMPILER) $(C_COMPILER_FLAGS)

C_SRCS = $(wildcard *.c) 
C_OBJECTS = $(patsubst %.c, %.o, $(C_SRCS))

c_all: $(C_EXECUTABLE)

$(C_EXECUTABLE): $(C_OBJECTS)
	$(C_COMPILER_CALL) -o $@ $^

%.o: %.c
	$(C_COMPILER_CALL) -c -o $@ $<

ifeq ($(OS), Windows_NT)
clean:
	-del $(C_EXECUTABLE).exe *.o
else
clean:
	-rm *.o
endif
endif

CPP_CODE ?= 0
ifeq ($(CPP_CODE), 1)
# CPP
DEBUG ?= 1
ifeq ($(DEBUG), 1)
CPP_COMPILER_FLAGS = -g3 -Wall -std=c++17 -U__STRICT_ANSI__
else
CPP_COMPILER_FLAGS = -O2 -Wall -std=c++17 -U__STRICT_ANSI__
endif

CPP_COMPILER_CALL = $(CPP_COMPILER) $(CPP_COMPILER_FLAGS)
CPP_SRCS = $(wildcard *.cc *.cpp) 
CPP_OBJECTS = $(patsubst %.cc %.cpp, %.o, $(CPP_SRCS))

cpp_all: $(CPP_EXECUTABLE)

$(CPP_EXECUTABLE): $(CPP_OBJECTS)
	$(CPP_COMPILER_CALL) -o $@ $^

%.o: %.c
	$(CPP_COMPILER_CALL) -c -o $@ $<
endif