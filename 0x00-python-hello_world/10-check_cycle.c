#include "lists.h"

/**
 * check_cycle - Checks if linked list contains cycle.
 * @list: Linked list for checking.
 *
 * Return: 1 if list has a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	do {
		slow = slow->next;
		fast = fast->next;

		if (fast)
			fast = fast->next;  /* Move fast pointer by two steps */

		if (slow == fast)
			return (1);

	} while (slow && fast);

	return (0);
}