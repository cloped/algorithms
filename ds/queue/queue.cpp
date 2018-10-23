#include <bits/stdc++.h>
#include <cstdlib>
using namespace std;

/**
 * Queue is a FIFO structure = First In First Out.
 * Our queue will be made of Books with ID, title and abstract.
 */
typedef struct Book {
	int id;
	char title[20];
	char abstract[100];
} Book;

/**
 * Each element of the queue will haver a pointer for the next
 * his previous.
 */
typedef struct ElementQueue {
	Book book;
	struct ElementQueue *next;
} ElementQueue;

/**
 * Our queue will have the pointer to the begin and the end.
 * This makes insertion and deletion faster.
 */
typedef struct Queue {
	ElementQueue *head;
	ElementQueue *tail;
} Queue;

/**
 * Create queue with null in head and tail.
 */
void createQueue(Queue &queue) {
	queue.head = NULL;
	queue.tail = NULL;
}

int queueIsEmpty(Queue queue) {
	if (queue.head == NULL) {
		return 1;
	} else {
	 	return 0;
	}
}

void insertQueue(Queue &queue, Book book) {
	/**
	 * Here there are 2 cases:
	 *	1 - Queue is empty so we need to set also the head.
	 *	2 - Queue has at least 1 element, so we add at the end.
	*/
	ElementQueue *newElement;

	newElement = (ElementQueue *) malloc(sizeof(ElementQueue));
	newElement->book = book;
	newElement->next = NULL;

	if (queueIsEmpty(queue) == 1) {
		queue.head = queue.tail = newElement;
	} else {
		ElementQueue *actual;
		actual = queue.head;

		while(actual->next != NULL) {
			actual = actual->next;
		}

		actual->next = newElement;
	}
}

int main(){
	Queue myBooks;
	createQueue(myBooks);
	
}