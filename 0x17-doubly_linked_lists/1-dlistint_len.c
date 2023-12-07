#include "lists.h"
/**
 * dlistint_len - fucntion that returns number of elemnts
 * @h:  pointer to list
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	int count;

	count = 0;

	if (h == NULL)
		return (count);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}

	return (count);
}
