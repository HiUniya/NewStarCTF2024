#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	cin>>s;
	for(int i=0;i<s.size();i++)
	{
		if(i%2==1)
		{
			if(s[i]>='a'&&s[i]<='z')
			{
				s[i] = 'a' +(s[i]-'a'+13)%26;
			}
			else if(s[i]>='A'&&s[i]<='Z')
			{
				s[i] = 'A' +(s[i]-'A'+13)%26;
			}
		}
	}
	cout<<s<<"\n";
}