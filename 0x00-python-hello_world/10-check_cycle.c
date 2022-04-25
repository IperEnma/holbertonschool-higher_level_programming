#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *aux;

	if (list)
	{
		aux = list;
		while (aux)
		{
			aux = aux->next;
			if (aux == list)
				return (1);
		}
	}

	return (0);
}
