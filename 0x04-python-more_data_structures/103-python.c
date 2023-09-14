#include <stdio.h>
#include <Python.h>

/* Function to print information about Python bytes object */
void print_python_bytes(PyObject *p)
{
char *str;
Py_ssize_t length, i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
printf("  [ERROR] Invalid Bytes Object\n");
else
{
PyBytes_AsStringAndSize(p, &str, &length);
printf("  size: %lu\n", length);
printf("  trying string: %s\n", str);
printf("  first %lu bytes: ", (length > 10) ? 10 : length);
for (i = 0; i < ((length > 10) ? 10 : length); i++)
printf("%02x ", str[i] & 0xff);
printf("\n");
}
}

/* Function to print information about Python list */
void print_python_list(PyObject *p)
{
Py_ssize_t i, size;
PyObject *list_item;

if (!PyList_Check(p))
return;

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
list_item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
if (PyBytes_Check(list_item))
print_python_bytes(list_item);
}
}
