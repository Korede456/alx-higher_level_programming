#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - returns a new sorted linked list
 * @head: pointer to a linked list
 * @number: a node data
 *
 * Return: address of a new node
 */

listint_t *insert_node(listint_t **head, int number);

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;

	/* allocate memory for the new node */

	newNode = malloc(sizeof(listint_t));

	/* return Null if memory allocation fails */

	if (!newNode)
	{
		return (NULL);
	}
	/* initialize newNode */

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	/* initialize current */
	current = *head;

/* look for the right place to place the newNode if */
/* the above condition was never met*/

	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}

	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}
