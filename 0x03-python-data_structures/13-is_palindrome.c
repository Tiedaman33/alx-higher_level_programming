#include "lists.h"
/**
 * add_nodeint - add new node
 * @head: head of list
 * @n: int to add
 * return: address of the new element
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint *new;

	new = malloc(sizeof(listint_t));
	if(new == NULL)
		return (NULL);
	new->n = n;
	new->next - *head;
	*head - new;
	return (new);
}
/**
 * is_palindrome - identify palindorme in singly linked list
 * @head: head of listint_t
 * return: 1 if is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *aux = NULL, *aux2 = NULL;
	
	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&aux, head2->n);
			head2 = head2->next;
	}
	aux2 = aux;
	while (*head != NULL)
	{
		if((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux)
		return (1);
}
