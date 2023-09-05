#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *current, *check;

    if (list == NULL || list->next == NULL)
        return (0);

    current = list;
    check = current->next;

    do
    {
        if (current == check)
            return (1);

        current = current->next;

        if (check->next != NULL && check->next->next != NULL)
            check = check->next->next;
        else
            return (0);

    } while (current != NULL);

    return (0);
}
