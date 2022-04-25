#include "lists.h"
/**
 * check_cycle - check if the list is circular
 * list - pointer to list
 * Return: 0 no cycle or 1 yes cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list)
	{
		fast = list;
		slow = list;
		while (fast)
		{
			slow = slow->next;
			fast = fast->next->next;
			if (fast == slow)
				return (1);
		}
	}

	return (0);
}
