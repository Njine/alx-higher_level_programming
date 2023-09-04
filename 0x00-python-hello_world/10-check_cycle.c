#include "lists.h"

/**
 * has_cycle - Checks if a linked list contains a cycle.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int has_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;          /* Move slow pointer by one step */
		fast = fast->next->next;    /* Move fast pointer by two steps */

		if (slow == fast)
			return (1);  /* If they meet, there's a cycle */
	}

	return (0); /* No cycle found */
}

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: Linked list to check.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	if (!list)
		return (0);

	return (has_cycle(list));
}
