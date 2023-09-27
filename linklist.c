#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

struct node 
{
    int data;
    struct node *next;
};

// struct node *head, *ptr;
// ptr = (struct node*)malloc(sizeof(struct node)); 

void main()
{
    int choice, item;

    do
    {
        print("\n Enter the item which you want to insert\n");

        int item = get_string("Enter number here")
        insert(item);

    } while (choice == 0);
    
}


void insert(int item) 
{
    struct node *ptr = (struct node*)malloc(sizeof(struct node *temp));

    if (ptr == NULL)
    {
        printf('\noverflow');
    }
    else 
    {
        ptr -> data = item;
        if (head == NULL)
        {
            head = ptr;
            ptr -> next = head;
        }
        else
        {
            temp = head;
            while (temp -> next != head)
            {
                temp = temp ->next
            }
            ptr -> head = head;
            temp -> next = ptr;
            head = ptr;
        }

    printf("\nNode Insert\n");
    }
}