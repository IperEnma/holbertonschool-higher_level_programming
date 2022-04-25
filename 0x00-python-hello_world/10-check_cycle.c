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

	slow = slow->next;
	fast = fast->next->next;

	while (slow && fast && fast->next)
	{
		if (fast == slow)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
