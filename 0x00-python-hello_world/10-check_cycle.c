#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
		if (list == slow)
			return (1);
	}
	return (0);
}
