#include<stdio.h>
#include<stdlib.h>
#include"string.h"

void mySwap(int *a,int *b){
	int temp=0;
	temp = *a;
	*a = *b;
	*b = temp;
}
void printA(int a[],int n){
	for(int i=0;i<n;i++){
		printf("%d ",a[i]);
	}
	printf("\n");
}
void reverseStr(char st[]){
	int k=strlen(st);
	for(int i=0;i<k/2;i++){
		int j=k-1-i;
		char temp;
		temp=st[i];
		st[i]=st[j];
		st[j]=temp;
	}
	printf("reversed string is:%s\n",st);
}
int indexSubStr(char str[],char sub[]){
	int l1=strlen(str);
	int l2=strlen(sub);
	int i=0,j=0;
	while(i<l1&&j<l2){
		if(str[i]==sub[j]){i++;j++;}
		else{i=i-j+1;j=0;}  //i-j means the start compare position of str.
	}
	if(j==l2) return i-j;
	return -1;
}
void mySort(int *a,int n){
	for(int i=0;i<n;i++){
		int minp=i;
		for(int j=i+1;j<n;j++){
			if((*(a+j))<(*(a+minp))){minp=j;}
		}
		if(i!=minp){mySwap(a+i,a+minp);}
	}
}
/////////////////////////////////
int partion(int a[],int p,int r){
	int x=a[p];
	int i=p;
	int j=r+1;
	while(1){
		do{j-=1;}while(a[j]>x);
		do{i+=1;}while(a[i]<=x);
		if(i<j)
			mySwap(&a[i],&a[j]);
		else
			return j;
	}
}
void quickSortRecu(int a[],int p,int r){
	if(p<r)
	{
		int q=partion(a,p,r);
		mySwap(&a[p],&a[q]);
		quickSortRecu(a,p,q-1);
		quickSortRecu(a,q+1,r);
	}
}
void quickSort(int a[],int n){
	quickSortRecu(a,0,n-1);
}

int binarySearch(int a[],int n,int x){
	int b=0;
	int e=n;
	int m=0;
	while(b<=e&&m>-1&&m<n){
		m=(b+e)/2;
		if(x==a[m])
			return m;
		else if (x<a[m])
			e=m-1;
		else
			b=m+1;
	}
	return -1;
}
///////////////////////////////////////////////
int maxSubSum(int a[],int n,int * endIndex){
	int maxSubSum=0;
	int b=0;
	for(int i=0;i<n;i++){
		if(b>0)
			b=b+a[i];
		else
			b=a[i];
		if(b>maxSubSum){
			maxSubSum=b;
			*endIndex=i;
		}
	}
	return maxSubSum;
}
int minEditDis(char a[],char b[],int i,int j){
	int d1=0,d2=0l,d3=0;
	if(i==0)
		return j;
	else if(j==0)
		return i;
	else if(a[i-1]==b[j-1])
		return minEditDis(a,b,i-1,j-1);
	else{
		d1=minEditDis(a,b,i-1,j)+1;
		d2=minEditDis(a,b,i,j-1)+1;
		d3=minEditDis(a,b,i-1,j-1)+1;
	}
	if (d1<=d2&&d1<=d3){
		return d1;
	}
	else if (d2<=d1&&d2<=d3){
		return d2;
	}
	else if (d3<=d1&&d3<=d2){
		return d3;
	}
//	else
//		return 9999999;
}
int minED1(char a[],char b[]){
	return minEditDis(a,b,strlen(a),strlen(b));
}
int main()
{
	int a[]={4,3,4,2,5};
	int b[]={2,1};
//	printf("%d\n",b[100]);
	int su[]={2,-5,8,11,-3,4,-1};
	char s1[]="ababcabcacbab";
	char s2[]="bcacb";
	char str[]="Computer Science";
	reverseStr(str);
	printf("subStr index:%d\n",indexSubStr(s1,s2));
	mySort(a,5);
	printA(a,5);
	quickSort(b,2);
	printA(b,2);
	int index=binarySearch(b,2,8);
	printf("binarySearch found index:%d\n",index);
	int endIndex;
	int maxs=maxSubSum(su,7,&endIndex);
	printf("maxsubsum is:%d, endsubindex is:%d\n",maxs,endIndex);
	char string1[]="b";
	char string2[]="eabcs";
	char string3[]="dinitrophenylhydrazine";
    char string4[]="benzalphenylhydrazone";
	printf("min edit distance of '%s' to '%s' is %d\n",string3,string4,minED1(string3,string4));
}
