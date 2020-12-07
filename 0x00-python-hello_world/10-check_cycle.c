#include "lists.h"
/**
 * int check_cycle - listint_t *list
 * @list: linked list of ints
 * description: check to see if singly linked list has a cycle
 * Return: 0 if no cycle. Else 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *paceNode, *raceNode;

	while (raceNode && raceNode->next)
	{
		paceNode = list->next;
		raceNode = list->next->next;
		if(raceNode == paceNode)
			return(1);
	}
	return (0);
}
