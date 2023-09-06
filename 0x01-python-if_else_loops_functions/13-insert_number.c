#include "lists.h"
#include <stdlib.h>

/**
* insert_node - Inserts a number into a sorted singly-linked list.
* @head: A pointer to the head of the linked list.
* @number: The number to insert.
*
* Return: A pointer to the new node, or NULL if it fails.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *current = *head;
listint_t *prev = NULL;

if (!new_node)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (!current || current->n >= number)
{
new_node->next = current;
*head = new_node;
return (new_node);
}

while (current && current->n < number)
{
prev = current;
current = current->next;
}

prev->next = new_node;
new_node->next = current;

return (new_node);
}
