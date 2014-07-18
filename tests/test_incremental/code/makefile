all: code fake_impl

fake_impl: subclass_fake.o

code: main.o subclass.o
	$(CXX) -o $@ $^

main.o: main.cpp subclass.h common_utility_file_included_everywhere.h
	$(CXX) -I. -c main.cpp

subclass_fake.o: subclass.cpp subclass.h
	$(CXX) -DFAKE_IMPL -I. -c subclass.cpp -o subclass_fake.o

subclass.o: subclass.cpp subclass.h
	$(CXX) -I. -c subclass.cpp

clean:
	rm -rf code *.o
