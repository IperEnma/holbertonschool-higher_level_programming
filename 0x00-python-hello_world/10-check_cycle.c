#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
