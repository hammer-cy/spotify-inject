all:
	cython main.py -3 --embed
	gcc -Os -I /usr/include/python3.9 -o spotify main.c -lpython3.9 -lpthread -lm -lutil -ldl

clean:
	rm -rf main.c
	rm -rf spotify
