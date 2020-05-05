#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject pointer
*/
void print_python_list_info(PyObject *p)
{
long int size, a;
Py_ssize_t i;
PyObject *item;
size = (((PyVarObject *)(p))->ob_size);
printf("[*] Size of the Python List = %ld\n", size);
a = (((PyListObject *)(p))->allocated);
printf("[*] Allocated = %ld\n", a);
for (i = 0; i < size; i++)
{
item = PyList_GET_ITEM(p, i);
printf("Element %ld: %s\n", i, (((PyObject *)(item))->ob_type)->tp_name);
}
}
