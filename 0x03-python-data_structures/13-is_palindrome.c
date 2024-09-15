#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *before = NULL;
	listint_t *current_node = *head;
	listint_t *after = NULL;

	while (current_node)
	{
		after = current_node->next;
		current_node->next = before;
		before = current_node;
		current_node = after;
	}

	*head = before;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head,
*temp_ptr = *head, *dup_ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			dup_ptr = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			dup_ptr = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse_listint(&dup_ptr);

	while (dup_ptr && temp_ptr)
	{
		if (temp_ptr->n == dup_ptr->n)
		{
			dup_ptr = dup_ptr->next;
			temp_ptr = temp_ptr->next;
		}
		else
			return (0);
	}

	if (!dup_ptr)
		return (1);

	return (0);
}
