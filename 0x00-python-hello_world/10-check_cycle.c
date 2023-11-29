#include "lists.h"
/**
 * check_cycle - fucntion checks if singly linked lsit has a cycle in it
 * @list: pointer to th beginning of the node
 * Return: o if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;
	
	if (list == NULL || list->next == NULL)
		return(0);
	current = list;
	check = current->next;
	
	while (current != NULL && check->next != NULL
			&& check->next->next != NULL)
	{
		if(current == check)
			return (1);
		current = current->next;
		check= check->next->next;
	}
	return (0);
}
