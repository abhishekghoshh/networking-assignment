#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
	string ip;
	int ip_class[4]={0,0,0,0},ip_match;
	cout<<"Enter your IP"<<endl;
	cin>>ip;
	ip_match=1;
	for(int i=0;i<ip.length();i++)
	{
		if(ip[i]=='.')
		{
			ip_match++;
			if(ip_match==5)
			{
				cout<<"Please enter a valid ip"<<endl;
				return 0;
			}
			continue;
		}
	ip_class[ip_match-1]=ip_class[ip_match-1]*10+(ip[i]-'0');
	}
	int m=ip_class[0];
	if(ip_class[0]=255&&ip_class[1]<=255&&ip_class[2]<=255&&ip_class[3]<=255&&ip_match==4)
	{
		cout<<"IP in the class of ";
		if(m<=127)
		cout<<"A";
		else if(m<=191)
		cout<<"B";
		else if(m<=223)
		cout<<"C";
		else if(m<=239)
		cout<<"D";
		else
		cout<<"E";
	}
	else
	{
		cout<<"Please enter a valid ip"<<endl;
	}
	return 0;
}
