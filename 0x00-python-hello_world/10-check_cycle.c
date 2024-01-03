#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for cycle in linked link
 * @list: pointer to a list
 *
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first_ptr;
	listint_t *second_ptr;

	first_ptr = list;
	second_ptr = list;

	while (second_ptr != NULL && second_ptr->next != NULL)
	{
		first_ptr = first_ptr->next;
		second_ptr = second_ptr->next->next;

		if (second_ptr == first_ptr)
		{
			return (1);
		}
	}

	return (0);
}
