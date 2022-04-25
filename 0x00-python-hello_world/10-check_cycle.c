#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	if (list)
	{
		fast = list;
		while (list)
		{
			list = list->next;
			if (!fast->next->next)
				break;
			fast = fast->next->next;
			if (fast == list)
				return (1);
		}
	}
	return (0);
}
