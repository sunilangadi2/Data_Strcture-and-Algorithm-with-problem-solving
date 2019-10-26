/* C Program to open binary file called myfile,
   read five bytes from it,and close the file */

#include<stdio.h>
#include<stdlib.h>

int main()
{
	char buf[5]={0};  //buffer with only five bytes
	int i;
	FILE *fp=fopen("myfile.txt","rb");

	if (fp==NULL)
	{
		perror("Failed to open file:\"myfile\"");
		return EXIT_FAILURE;

	}

	for(i=0;i<5;i++)
	{
		int rc=getc(fp);
		if(rc==EOF)
		{
			return EXIT_FAILURE;
		}
		buf[i]=rc;
	}
	printf("%s",buf);

	fclose(fp);

	return EXIT_SUCCESS;
}
