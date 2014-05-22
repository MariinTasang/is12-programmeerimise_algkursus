#include <stdio.h>

/* selle koodi k2ivitamisel kuvatakse 4*4 maleruut */
/* yhe ruudu laius on 5 ja korgus 2 symbolit */

int w;
int h; 

int x; 
int y;

/*ridade arv*/
int nr;


int main(void) {

	for (nr = 0; nr < 4; ++nr) {
		for (w = 0; w < 4; ++w) {
				printf("+");
				for (x = 0; x < 5; ++x) {
						printf("-");
				}
		}
	printf("+\n");

	for (h = 0; h < 2; ++h) {
		for (w = 0; w < 4; ++w) {
				printf("|");
				for (x = 0; x < 5; ++x) {
						printf(" ");
				}
		}
	printf("|\n");
	}
	}


	for (w = 0; w < 4; ++w) {
			printf("+");
			for (x = 0; x < 5; ++x) {
					printf("-");
			}
	}
	
	printf("+\n");
	
}
