#include "lists.h"
/**
 * print_python_list_info - function that prints some basic info.
 * @: python list
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0, elem < PY_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, PY_TYPE(PyList_GetItem(p, elem))->tp_name);
}
