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
	int cont = 0, buff[2048], idx = 0;

	if (!(*head) || !cp_head->next)
		return (1);
	while (cp_head)
	{	buff[cont] = cp_head->n;
		cp_head = cp_head->next;
		cont++;
	}
	while (cont > idx)
	{
		if (buff[idx] != buff[cont - 1])
			return (0);
		cont--;
		idx++;
	}
	return (1);
}
