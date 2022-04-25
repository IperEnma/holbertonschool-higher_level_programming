#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *control = list;

	if (list)
	{
		fast = list;
		while (list)
		{
			if (!fast->next->next)
				break;
			fast = fast->next->next;
			list = list->next;
			if (fast == list)
				return (1);
			if (list == control)
				return (1);
		}
	}
	return (0);
}
