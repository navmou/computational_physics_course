main: dynamic.o func.o
	gcc -o dynamic dynamic.o func.o -lm

dynamic.o: dynamic.c func.h
	gcc -c dynamic.c -lm

func.o: func.c func.h
	gcc -c func.c -lm

clean:
	rm -f *.o
	touch *.c
