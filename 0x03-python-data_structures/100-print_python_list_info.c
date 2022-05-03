#include "capti.h"
#include "listobject.h"
void print_python_list_info(PyObject *p)
{
	int size = 0, i = 0;
	PyListObject *list;
	PyObject *structobject;
	struct _typeobject *structtype;

	list = (PyListObject *)p;	
	size = PyList_Size(p);
	printf("[*] Allocated = %ld\n", list->allocated);
	printf("[*] Size of the Python List = %d\n", size);
	for (i = 0; i < size; i++)
	{
		structobject = list->ob_item[i];
		structtype = structobject->ob_type;
		printf("Element %d: %s\n", i, structtype->tp_name);
	}
}
