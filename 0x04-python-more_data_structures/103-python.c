#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Print information about Python bytes objects
* @p: Python object
*/
void print_python_bytes(PyObject *p)
{
char *str;
Py_ssize_t length, i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

PyBytes_AsStringAndSize(p, &str, &length);
printf("  size: %lu\n", length);
printf("  trying string: %s\n", str);

length = (length > 10) ? 10 : length;

printf("  first %lu bytes: ", length);

i = 0;
while (i < length - 1)
{
printf("%02x ", str[i] & 0xff);
i++;
}

printf("%02x\n", str[length - 1] & 0xff);
}

/**
* print_python_list - Print information about Python list objects
* @p: Python object
*/
void print_python_list(PyObject *p)
{
Py_ssize_t i = 0;
PyObject *list;

if (!PyList_Check(p))
return;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

while (i < PyList_Size(p))
{
list = PySequence_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(list)->tp_name);

if (strcmp(Py_TYPE(list)->tp_name, "bytes") == 0)
print_python_bytes(list);

i++;
}
}

