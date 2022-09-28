#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: The list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *checked = NULL;
	listint_t *mover = NULL;

	if (*head == NULL)
		return (1);

	while (current->next != checked && current->next->next != checked)
	{
		mover = current;
		while (mover->next != checked)
			mover = mover->next;
		if (mover->n != current->n)
			return (0);
		checked = mover;
		current = current->next;
	}

	return (1);
}
