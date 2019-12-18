#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle in it.
  * @list: a list.
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle.
  */
int check_cycle(listint_t *list)
{
	listint_t *hare, *turtle;

	hare = turtle = list;
	while (hare && turtle && hare->next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;
		if (hare == turtle)
			return (1);
	}
	return (0);
}
