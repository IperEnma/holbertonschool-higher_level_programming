#include "lists.h"
/**
 * 
 *
 */
void addnode(listint_t **head, int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = n;
		new->next = *head;
		*head = new;
	}
}
/**
 *
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *new = NULL;
	listint_t *aux = *head;
	listint_t *newaux = NULL;
	if (*head == NULL)
		return (0);
	while(aux)
	{
		addnode(&new, aux->n);
		aux = aux->next;
	}
	aux = *head;
	newaux = new;
	while (aux && newaux)
	{
		if (aux->n != newaux->n)
		{
			free(new);
			return (0);
		}
		aux = aux->next;
		newaux = newaux->next;
	}
	free_listint(new);
	return (1);
}
