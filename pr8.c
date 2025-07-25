include <stdio.h>


long long convert(long long);

int main()
	{

    long long n;

    printf("Enter a binary number: ");
    scanf("%lld", &n);

    printf("%lld in binary = %lld in decimal", n, convert(n));

    return 0;
}

