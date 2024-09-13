main: test.o func.o
	gcc -o test test.o func.o  -lgsl -lgslcblas

test.o: test.c func.h
	gcc -c test.c -lgsl -lgslcblas

func.o: func.c func.h
	gcc -c func.c -lgsl -lgslcblas

clean:
	rm -f *.o
	touch *.c
