# driver file
tsdriver: tstock.hpp
	g++ -c tsdriver.cpp 
	g++ tsdriver.o tstock.hpp -o tsdriver