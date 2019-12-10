#include <stdlib.h>
#include "lists.h"
/**
  * insert_node - insert node sorted.
  * @head: head.
  * @number: int of struct.
  * Return: the address of the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if ((new_node->n < current->n && current) || !current)
	{
		if (!current)
			new_node->next = NULL;
		else
			new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current)
	{
		if (current->n == number)
		{	new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		if (current->n < number && !current->next)
		{	new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		if (current->next && current->n < number && current->next->n > number)
		{	new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	free(new_node);
	return (NULL);
}
