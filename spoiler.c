static char *ft_itoa_base_ptr(unsigned long num, int base, char *digits)
{
    char *str;
    unsigned long temp = num;
	int len = 1;

    while (temp /= base)
        len++;
    str = malloc(sizeof(char) * (len + 1));
    
    if (!str)
        return NULL;
    
    str[len] = '\0';
    while (len--)
    {
        str[len] = digits[num % base];
        num /= base;
    }

    return str;
}

static int ft_putptr(unsigned long ptr)
{
    int len = 0;
	char *str;

    if (ptr == 0)
		return (write(1, "(nil)", 5)); // Write will return 5
	str = ft_itoa_base_ptr(ptr, 16, "0123456789abcdef");        
    len += ft_putstr("0x");
    if (str)
    {
        len += ft_putstr(str);
        free(str);
    }
    return len;
}
