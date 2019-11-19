import unittest
from libros.models import Autor
from prueba import probar
# Create your tests here.
class AutorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       Autor.objects.create(primer_nombre='carlos', apellido='cirtes')

    def test_primer_nombre_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('primer_nombre').verbose_name
        self.assertEqual(field_label,'primer_nombre')

    def test_año_defuncion_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('año_defuncion').verbose_name
        self.assertEqual(field_label,'defuncion')

    def test_primer_nombre_max_length(self):
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('primer_nombre').max_length
        self.assertEqual(max_length,100)

    def test_object_name_is_apellido_name_comma_primer_nombre(self):
        autor=Autor.objects.get(id=1)
        expected_object_name = '%s, %s' % (autor.apellido, autor.primer_nombre)
        self.assertEqual(expected_object_name,str(autor))
    
    def test_get_absolute_url(self):
        autor=Autor.objects.get(id=1)
        self.assertEqual(autor.get_absolute_url(),'/libros/autor/1' )


class TestProbar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(probar(3,5),8)
        self.assertEqual(probar(3,0),3)
        self.assertEqual(probar(3,1),4)

