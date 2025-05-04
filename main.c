#include "ft_printf.h"
#include <stdio.h>

// cc main.c -L. -lftprintf -w -o o && ./o 

int main()
{
	int 	a;
	int	b;
	char	*s;

	a = ft_printf("Hello World\n");
	b = printf("Hello World\n");

	printf("%d, %d\n", a, b);

        a = ft_printf("%s\n", "Banana Frita");
        b = printf("%s\n", "Banana Frita");

        printf("%d, %d\n", a, b);

	s = NULL;
        a = ft_printf("%s\n", s);
        b = printf("%s\n", s);

        printf("%d, %d\n", a, b);

        a = ft_printf("%p\n", s);
        b = printf("%p\n", s);

        printf("%d, %d\n", a, b);
        
        a = ft_printf("%c%c%c%c\n", 'I', 'v', 'a', 'n');
        b = printf("%c%c%c%c\n", 'I', 'v', 'a', 'n');

        printf("%d, %d\n", a, b);
        
        a = ft_printf("%x\n", 0xBABACA);
        b = printf("%x\n", 0xBABACA);
        
        printf("%d, %d\n", a, b);
        
        a = ft_printf("%X\n", 0xB00B5);
        b = printf("%X\n", 0xB00B5);

        printf("%d, %d\n", a, b);
        
        a = ft_printf("%X\n", -42);
        b = printf("%X\n", -42);

        printf("%d, %d\n", a, b);
        
        a = ft_printf("%%\n");
        b = printf("%%\n");

        printf("%d, %d\n", a, b);

        a = ft_printf("\t\n\v\f\r");
        b = printf("\t\n\v\f\r");

        printf("%d, %d\n", a, b);

        a = ft_printf("");
        b = printf("");

        printf("%d, %d\n", a, b);
        
        a = ft_printf("", s, s, s);
        b = printf("", s, s, s);

        a = ft_printf("%c\n", s, s, s);
        b = printf("%c\n", s, s, s);

        a = ft_printf("%c %c %c\n", s, s, s);
        b = printf("%c %c %c\n", s, s, s);


        printf("%d, %d\n", a, b);


	return (0);
}
