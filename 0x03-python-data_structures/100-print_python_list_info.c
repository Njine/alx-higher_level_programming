#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size_p, idx = 0;
    PyObject *element;

    size_p = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size_p);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    while (idx < size_p)
    {
        element = PyList_GET_ITEM(p, idx);
        printf("Element %ld: %s\n", idx, element->ob_type->tp_name);
        idx++;
    }
}
