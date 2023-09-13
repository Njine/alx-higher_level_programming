#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
    Py_ssize_t length, i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    length = PyBytes_GET_SIZE(p);
    printf("  size: %ld\n", length);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", length > 10 ? 10 : length);
    for (i = 0; i < (length > 10 ? 10 : length); i++)
        printf("%02x ", PyBytes_AsString(p)[i] & 0xff);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *list_item;

    if (PyList_Check(p))
    {
        printf("[*] Python list info\n");
        size = PyList_Size(p);
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < size; i++)
        {
            list_item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
            if (strcmp(Py_TYPE(list_item)->tp_name, "bytes") == 0)
                print_python_bytes(list_item);
        }
    }
}
