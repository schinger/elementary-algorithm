#include<stdio.h>
#include<stdlib.h>
#include<stack>
using namespace std;

typedef struct LNode{
	int data;
	struct LNode *next;
}LNode, *Link;

Link creatList(int a[],int n){
	Link L,p;
	L=(Link)malloc(sizeof(LNode));
	L->next=NULL;
	for(int i=n-1;i>-1;i--){
		p = (Link)malloc(sizeof(LNode));
		p->data=a[i];
		p->next=L->next;
		L->next=p;
	}
	return L;
}
void traverseList(Link L){
	printf("print List element:");
	Link p=L->next;
	while(p!=NULL){
		printf("%d ",p->data);
		p=p->next;
	}
	printf("\n");
}
void reverseList(Link L){
	Link pre,cur,nex;
	pre = NULL;
	cur = L->next;
	while(cur!=NULL){
		nex = cur->next;
		cur->next=pre;
		pre = cur;
		cur = nex;
	}
	L->next=pre;
}
Link mergeList(Link a,Link b){
	Link pa=a->next,pb=b->next;
	Link c=a,pc=a;
	while(pa&&pb){
		if(pa->data<=pb->data){
			pc->next=pa;pc=pa;pa=pa->next;
		}
		else{
			pc->next=pb;pc=pb;pb=pb->next;
		}
	}
	pc->next=(pa?pa:pb);
	return c;
}
/////////////////////////////////////////////////////
typedef struct BiTNode{
	char data;
	struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;

void printChar(char c){
	printf("%c ",c);
}

int i=0;
char a[]="abc##de#g##f###";
BiTree T;
void createBiTree(BiTree &T){ //PreOrCreate
	char ch = a[i++];
	if(ch=='#') T=NULL;
	else{
		T=(BiTree)malloc(sizeof(BiTNode));
		T->data=ch;
		createBiTree(T->lchild);
		createBiTree(T->rchild);
	}
}
void PreOrTraverse(BiTree T, void (* Visit)(char c)){
	if(T){
		Visit(T->data);
		PreOrTraverse(T->lchild,Visit);
		PreOrTraverse(T->rchild,Visit);
	}
}

void InOrTraverse(BiTree T, void (* Visit)(char c)){
	if(T){
		InOrTraverse(T->lchild,Visit);
		Visit(T->data);
		InOrTraverse(T->rchild,Visit);
	}
}

void PostOrTraverse(BiTree T, void (* Visit)(char c)){
	if(T){
		PostOrTraverse(T->lchild,Visit);
		PostOrTraverse(T->rchild,Visit);
		Visit(T->data);
	}
}
void PreOrTraverse2(BiTree T, void (* Visit)(char c)){
    stack<BiTree> s;
    BiTree p=T;
    while(p!=NULL||!s.empty()){
        while(p!=NULL){
            Visit(p->data);
            s.push(p);
            p=p->lchild;
        }
        if(!s.empty()){
            p=s.top();
            s.pop();
            p=p->rchild;
        }
    }
}
void InOrTraverse2(BiTree T, void (* Visit)(char c)){
    stack<BiTree> s;
    BiTree p=T;
    while(p!=NULL||!s.empty()){
        while(p!=NULL){
            s.push(p);
            p=p->lchild;
        }
        if(!s.empty()){
            p=s.top();
            Visit(p->data);
            s.pop();
            p=p->rchild;
        }
    }
}
void PostOrTraverse2(BiTree T, void (* Visit)(char c)){ //http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html
    stack<BiTree> s;
    BiTree cur;
    BiTree pre=NULL;
    s.push(T);
    while(!s.empty()){
        cur=s.top();
        if((cur->lchild==NULL&&cur->rchild==NULL)||
           (pre!=NULL&&(pre==cur->lchild||pre==cur->rchild))){
            Visit(cur->data);
            s.pop();
            pre=cur;
        }
        else{
            if(cur->rchild!=NULL)
                s.push(cur->rchild);
            if(cur->lchild!=NULL)
                s.push(cur->lchild);
        }
    }
}


int main(){
	int a[]={1,2,4,5,8};
	int b[]={1,2,8,9,13,22,31};
	Link la=creatList(a,5);
	Link lb=creatList(b,7);
	traverseList(la);
	traverseList(lb);
	Link lc=mergeList(la,lb);
	traverseList(lc);
	reverseList(lc);
	traverseList(lc);

	createBiTree(T);
	PreOrTraverse(T,printChar);
	printf("\n");
	PreOrTraverse2(T,printChar);
	printf("\n");
	InOrTraverse(T,printChar);
	printf("\n");
	InOrTraverse2(T,printChar);
	printf("\n");
	PostOrTraverse(T,printChar);
	printf("\n");
	PostOrTraverse2(T,printChar);
	printf("\n");
}
