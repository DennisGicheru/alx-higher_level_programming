#include "lists.h"

/**
* check_cycle - checks linked list for cycle
* @head: pointer to head of the list
* Return: 0 if no cycle, 1 if cycle is present
*/

int check_cycle(listint_t *head)
{
	int *node1, *node2;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		node1 = (int *)&head;
		node2 = (int *)&head->next;

		if (head->next == NULL)
			return (0);

		if (*node1 - *node2 <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
