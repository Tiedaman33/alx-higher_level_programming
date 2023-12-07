#include "lists.h"
/**
 * sum_dlistint -  return sum of all data
 * @head: pointer to first element in node
 * Return: 0 alaways sucess
 */
int sum_dlistint(dlistint_t *head)
{
	int sum;

	sum = 0;

	if (head != NULL)
	{
		while (head->prev != NULL)
			head = head->prev;

		while (head != NULL)
		{
			sum += head->n;
			head = head->next;
		}
	}
	return (sum);
}
