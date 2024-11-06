#include <bits/stdc++.h>
#include <Windows.h> 

unsigned __int64 __fastcall sub_140001000(__int64* a1, int a2, void *a3)
{
  signed __int64 v4; // rbx
  int v6; // edi
  signed __int64 v7; // rsi
  signed __int64 i; // rcx
  signed __int64 j; // rdx
  signed __int64 k; // r11
  unsigned __int8 v11; // r9
  unsigned __int8 v12; // r10
  char v13; // cl
  char v14; // r8
  __int16 v15; // kr00_2
  __int64 v16; // r14
  int v17; // ebx
  int v18; // ecx
  __int64 v19; // rdx
  __int64 v20; // rax
  __int64 v21; // rdx
  int v22; // r8d
  int *v23; // rcx
  unsigned __int64 result; // rax
  int v25; // r8d
  signed __int64 m; // r10
  int v27; // r9d
  char v28[16]; // [rsp+20h] [rbp-E0h] BYREF
  __int128 v29[16]; // [rsp+30h] [rbp-D0h] BYREF
  char Src[304]; // [rsp+130h] [rbp+30h] BYREF
  char v31[256]; // [rsp+260h] [rbp+160h] BYREF

  v4 = a2;
  memset(Src, 0, sizeof Src);
  v6 = 0;
  v7 = v4;
  if ( (int)v4 > 0 )
  {
    for ( i = 0; i < v4; ++i )
      Src[i] = *(char *)(a1 + 2 * i);
  }

  v29[0] = ((__int128)431F6B044265353A7078530320547431;
  v29[1] = ((__int128)51562C591A2F4B52130B082176003706;
  v29[2] = ((__int128)17122A41293C7A6463251526050E3B7F;
  v29[3] = ((__int128)5A141C5F7116476F6C4433663D57392E;
  v29[4] = ((__int128)286A5D7E6D69183F620F681B30014F0C;
  v29[5] = ((__int128)7948103845467B503E025E0972555B22;
  v29[6] = ((__int128)73770A0D7D1127342B7C492D6E613660;
  v29[7] = ((__int128)231975071D4E4A6740241E4D324C5C58;
  if ( (int)v4 > 0 )
  {
    for ( j = 0; j < v4; ++j )
      Src[j] = *((__int128 *)v29 + (unsigned __int8)Src[j]);
    for ( k = 0; k < v4; k += 4 )
    {
      v11 = Src[k + 3];
      v12 = Src[k + 2];
      v13 = ((unsigned __int8)Src[k] >> 3) | (32 * v11);
      v14 = 32 * Src[k + 1];
      Src[k + 1] = (32 * Src[k]) | ((unsigned __int8)Src[k + 1] >> 3);
      v15 = 32 * v12;
      Src[k + 2] = v14 | HIBYTE(v15);
      Src[k] = v13;
      Src[k + 3] = v15 | (v11 >> 3);
    }
  }
  v16 = 256;
  strcpy(v28, "easy_GUI");
  v17 = 0;
  memset(v31, 0, sizeof(v31));
  v18 = 0;
  v19 = 0;
  do
  {
    *((char *)v29 + v19) = v18;
    v20 = v18 & 7;
    ++v19;
    ++v18;
    v31[v19-1] = v28[v20];
  }while ( v18 < 256 );
  v21 = 0;
  do
  {
    v22 = *((unsigned __int8 *)v29 + v21);
    v17 = (v22 + v31[v21] + v17) % 256;
    v23 = (int *)((char *)v29+v17) ;
    result = (unsigned __int8)*v23;
    *((__int128 *)v29 + v21++) = result;
    *v23 = v22;
    --v16;
  }while ( v16 );
  v25 = 0;
  if ( v7 > 0 )
  {
    for ( m = 0; m < v7; ++m )
    {
      v6 = (v6 + 1) % 256;
      v27 = *((unsigned __int8 *)v29 + v6);
      v25 = (v27 + v25) % 256;
      *((__int128 *)v29 + v6) = *((__int128 *)v29 + v25);
      *((__int128 *)v29 + v25) = v27;
      Src[m] ^= *((__int128 *)v29 + (unsigned __int8)(v27 + *((__int128 *)v29 + v6)));
    }
    return (unsigned __int64)memcpy(a3, Src, v7);
  }
  return result;
}

int main()
{
  char v93[512];
 // __int64 string[104]={-33,-57,77,20,-63,-20,8,-28,95,63,3,-76,-112,74,-71,-113,-113,-6,113,67,-57,-15,-99,-35,79,-64,18,68,92,-99,-120,54,45,22,29,-19,-68,-17,-69,91,-97,119,-21,88,0};
  __int64 string[104]={'f','l','a','g','{',0};
  int x = sub_140001000(string,5,v93);
  printf("%d\n",x);
  for(int i=0;i<5;i++)
  {
    printf("%d\n",v93[i]);
  }
}