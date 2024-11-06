#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s="flag{";
	int now=5;
	while(true)
	{
		for(int i=33;i<=125;i++)
		{
			char p=i;
			string tmp = s+p;
			ofstream fout("./data.txt",ios::out);
			if(!fout.is_open())
			{
				return -1;
			}
			fout<<tmp;
			fout.close();
			FILE *fp = popen("./upx < data.txt > data.out","r");
			int code = pclose(fp);
			if(WEXITSTATUS(code)==now+1||WEXITSTATUS(code)==0)
			{
				now++;
				s+=p;
				break;
			}
		}
		if(now==22) break;
	}
	cout<<s<<"\n";
	return 0;
}

/*
(base) [uniya@uniyawork Downloads]$ ./solve
flag{Do_you_know_UPX?}

*/