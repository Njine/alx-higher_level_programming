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

	if (length > 10)
		length = 10;
	else
		length++;

	printf("  first %lu bytes: ", length);

	for (i = 0; i < length - 1; i++)
		printf("%02x ", str[i] & 0xff);

	printf("%02x\n", str[length - 1] & 0xff);
}

/**
 * print_python_list - Print info about Python lists with bytes objects
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *list_item;

	if (!PyList_Check(p))
		return;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);

		if (strcmp(Py_TYPE(list_item)->tp_name, "bytes") == 0)
			print_python_bytes(list_item);
	}
}

