#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: points to the list's head
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int array[100];
	int array2[100];
	int idx;
	int idx2;
	int array_size;
	int size;

	idx = 0;
	idx2 = 0;

	if (*head == NULL)
	{
		return (1);
	}
	current = *head;

	while (current->next != NULL)
	{
		array[idx] = current->n;
		idx += 1;
		current = current->next;
	}
	array_size = sizeof(array) / sizeof(int);
	while (array_size > 0)
	{
		array2[array_size - 1] = array[array_size - 1];
		array_size--;
	}

	size = sizeof(array) / sizeof(int);
	while (idx2 < size)
	{
		if (array[idx2] != array2[idx2])
			return (0);
		idx2++;
	}
	return (1);
}
