#include <bits/stdc++.h>
using namespace std;
int main()
{

	string s="0x31,0x74,0x54,0x20,0x03,0x53,0x78,0x70,0x3A,0x35,0x65,0x42,0x04,0x6B,0x1F,0x43,0x06,0x37,0x00,0x76,0x21,0x08,0x0B,0x13,0x52,0x4B,0x2F,0x1A,0x59,0x2C,0x56,0x51,0x7F,0x3B,0x0E,0x05,0x26,0x15,0x25,0x63,0x64,0x7A,0x3C,0x29,0x41,0x2A,0x12,0x17,0x2E,0x39,0x57,0x3D,0x66,0x33,0x44,0x6C,0x6F,0x47,0x16,0x71,0x5F,0x1C,0x14,0x5A,0x0C,0x4F,0x01,0x30,0x1B,0x68,0x0F,0x62,0x3F,0x18,0x69,0x6D,0x7E,0x5D,0x6A,0x28,0x22,0x5B,0x55,0x72,0x09,0x5E,0x02,0x3E,0x50,0x7B,0x46,0x45,0x38,0x10,0x48,0x79,0x60,0x36,0x61,0x6E,0x2D,0x49,0x7C,0x2B,0x34,0x27,0x11,0x7D,0x0D,0x0A,0x77,0x73,0x58,0x5C,0x4C,0x32,0x4D,0x1E,0x24,0x40,0x67,0x4A,0x4E,0x1D,0x07,0x75,0x19,0x23,";
	string str[45];
	for(int i=0;i<44;i++)
	{
		cin>>str[i];
	}
	for(int i=0;i<44;i++)
	{
		str[i]="0x"+str[i];
		int x=s.find(str[i]);
		//cout<<x<<" ";
		cout<<char(x/5)<<"";
	}
}