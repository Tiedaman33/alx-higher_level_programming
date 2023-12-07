#include "lists.h"
/**
 * free_dlistint - free i node in list
 * @head: pointer to lits
 * Return: 0 success
 */
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
		return;

	while (head->next)
	{
		head = head->next;
		free(head->prev);
	}
	free(head);
}
