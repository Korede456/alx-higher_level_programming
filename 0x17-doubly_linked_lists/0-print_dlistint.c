#include "lists.h"

/**
 * print_dlistint - print the data in a list
 * @h: points to the head node
 *
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count;
	dlistint_t *current;

	count = 0;
	current = malloc(sizeof(dlistint_t));
	current->n = h->n;
	current->next = h->next;
	current->prev = h->prev;

	while (current)
	{
		count += 1;
		printf("%d\n", current->n);
		current = current->next;
	}
	free(current);
	return (count);
}
