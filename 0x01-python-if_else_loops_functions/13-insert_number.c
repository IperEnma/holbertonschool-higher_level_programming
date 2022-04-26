#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
		
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	if (current->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
