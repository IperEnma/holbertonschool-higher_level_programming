#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	
	if (!list)
		return (-1);
	fast = list->next->next;
	slow = list->next;
	while (fast)
	{
		if (fast == slow)
			return (1);
		if (slow == list)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
