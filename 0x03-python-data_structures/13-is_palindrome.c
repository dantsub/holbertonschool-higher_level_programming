#include "lists.h"
/**
  * is_palindrome - check if linked list is palindrome,
  * @head: head.
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *cp_head = *head, *cp_h, *h;
	int cont = 0;

	if (!(*head))
		return (1);
	h = NULL;
	while (cp_head)
	{
		add_nodeint(&h, cp_head->n);
		cp_head = cp_head->next;
		cont++;
	}
	cp_head = *head;
	cp_h = h;
	while (cp_head && cont / 2 > 0)
	{
		if (cp_head->n != cp_h->n)
		{
			free_listint(h);
			return (0);
		}
		cp_head = cp_head->next;
		cp_h = cp_h->next;
		cont--;
	}
	free_listint(h);
	return (1);
}
/**
  * add_nodeint - adds a new node at the beginning of a listint_t list.
  * @head: node.
  * @n: constant int.
  * Return: the address of the new element, or NULL if it failed
  */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (!(*head))
		new->next = NULL;
	else
		new->next = *head;
	*head = new;
	return (new);
}
