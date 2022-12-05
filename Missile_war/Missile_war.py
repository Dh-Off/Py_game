#include <stdio.h>
int main() {
	int i, j, k, d, e;
	d = 1; e = 1;
	printf("┌────────────────────────────────┐\n");
	printf("│   *  *     * *    *    *    *  │\n");
	printf("│* *    *    *    *   *  *     * │\n");
	printf("│*      *        *  *      *   * │\n");
	printf("│  *     *  *   *      *     *  *│\n");
	printf("│*      *  *     *   *    *   *  │\n");
	printf("│ *  * ┌────────────────┐  *    *│\n");
	for (i = 0; i <= 3; i++)
	{
		if (d <2)
		{
			printf("│     *│  ");
		}
		for (k = 8; k <= 14 - i; k++)
		{
			printf(" ");
		}

		for (j = 0; j < i * 2 - 1; j++)
		{
			printf("*");
		}
		if (e < 2)
		{
			printf("\t│  *    *│");
		}
		else
		{
		}

		printf("\n");
	}
	for (i = 0; i <= 3; i++)
	{
		if (d <2)
		{
			printf("│ *    │  ");

		}
		for (k = 9; k <= 14 - i; k++)
		{
			printf(" ");
		}
		for (j = 0; j < i * 2 + 1; j++)
		{
			printf("*");
		}
		if (e < 5)
		{
			printf("\t│    *   │");
		}
		else
		{
		}
		printf("\n");
	}
	for (i = 0; i <= 5; i++)
	{
		if (d <2)
		{
			printf("│    * │  ");
		}
		else 
		{
		}
		for (k = 9; k <= 14 - i; k++)
		{
			printf(" ");
		}
		for (j = 0; j < i * 2 + 1; j++)
		{
			printf("*");
		}
		if (e < 2)
		{
			printf("\t");
			printf("│ *     *│");
		}
		else
		{
		}
		
		printf("\n");
	}
	printf("│  * *  ** * │    │ *   ***  * **│\n");
	printf("│ * ** * ■■└────┘  ■■■ ◀━━━┿━━━ (Gift)\n");
	printf("│********************************│\n");
	printf("│□□□□□□□□□□□□□□□□│\n");
	printf("│    ┌─────────────────────┐     │\n");
	printf("│    │ * Merry Christmas * │     │\n");
	printf("│    └─────────────────────┘     │\n");
	printf("└────────────────────────────────┘\n\n");
	return 0;
}