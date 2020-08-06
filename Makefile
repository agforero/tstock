# not actual targets
.PHONY: all clean

# all targets
all: tsdriver

# driver file
tsdriver: tstock.hpp
	g++ -c tsdriver.cpp 
	g++ tsdriver.o tstock.hpp -o tsdriver

clean:
	rm -f *.o *.exe tsdriver