#include "lists.h"

/**
 * check_cycle - Determines whether a linked list has a cycle.
 * @list: Pointer to the start of the linked list.
 *
 * Return: 1 if a cycle is found, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
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
