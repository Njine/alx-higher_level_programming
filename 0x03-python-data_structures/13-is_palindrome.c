#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *prev_of_slow_ptr = *head;
    listint_t *second_half, *mid_node;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle of the list */
    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev_of_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    /* Handle odd length lists */
    if (fast_ptr != NULL)
    {
        mid_node = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    /* Reverse the second half of the list */
    second_half = reverse_list(&slow_ptr);

    /* Compare the first half and reversed second half */
    is_palindrome = compare_lists(*head, second_half);

    /* Restore the original list */
    slow_ptr = reverse_list(&second_half);

    /* If the list had an odd number of elements, reconnect the middle node */
    if (mid_node != NULL)
    {
        prev_of_slow_ptr->next = mid_node;
        mid_node->next = slow_ptr;
    }
    else
    {
        prev_of_slow_ptr->next = slow_ptr;
    }

    return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 *
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return (0);
        head1 = head1->next;
        head2 = head2->next;
    }

    return (1);
}
