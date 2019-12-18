#include "lists.h"
/**
  * is_palindrome - check if linked list is palindrome,
  * @head: head.
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *cp_head = *head;
	int cont = 0, buff[1024], idx;

	if (!(*head) || !cp_head->next)
		return (1);
	while (cp_head)
	{	buff[cont] = cp_head->n;
		cp_head = cp_head->next;
		cont++;
	}
	idx = cont - 1;
	cont = 0;
	while (cont < idx)
	{
		if (buff[idx] != buff[idx - cont])
			return (0);
		cont++;
	}
	return (1);
}
