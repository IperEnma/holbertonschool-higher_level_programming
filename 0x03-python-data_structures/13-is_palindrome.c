#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - is or not palindrome
 * @head: first node
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	int compare[3000], count = 0, count2 = 0;
	listint_t *aux;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	aux = *head;

	while (aux)
	{
		compare[count] = aux->n;
		aux = aux->next;
		count++;
	}
	count--;
	for (count2 = 0; count2 < count; count2++, count--)
	{
		if (compare[count] != compare[count2])
			return (0);
	}
	return (1);
}
