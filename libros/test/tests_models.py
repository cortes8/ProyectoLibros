from libros.models import Autor
# Create your tests here.
class AutorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       Autor.objects.create(primer_nombre='Big', apellido='Bob')
#setUpTestData()se	 llama	 una	 vez	 al	 comienzo	 de	 la	 ejecución	 de	 la	 prueba	 para	 la	
#configuración	a	nivel	de	clase. Usaría	esto	para	crear	objetos	que	no	 se	van	a	modificar	o	
#cambiar	en	ninguno	de	los	métodos	de	prueba

#setUp() se	 llama	 antes	 de	 cada	 función	 de	 prueba	 para	 configurar	 cualquier	 objeto	 que	
#pueda	ser	modificado	por	la	prueba	(cada	función	de	prueba	obtendrá	una	versión	"nueva"	de	estos	objetos).

    def test_primer_nombre_label(self)
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('primer_nombre').verbose_name
        self.assertEqual(field_label,'primer_nombre')

    def test_año_defuncion_label(self)
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('año_defuncion').verbose_name
        self.assertEqual(field_label,'defuncion')

    def test_primer_nombre_max_length(self)
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('primer_nombre').max_length
        self.assertEqual(max_length,100)

    def test_object_name_is_apellido_name_comma_primer_nombre(self)
        autor=Autor.objects.get(id=1)
        expected_object_name = '%s, %s' % (autor.apellido, autor.primer_nombre)
        self.assertEqual(expected_object_name,str(autor))
    
    def test_get_absolute_url(self)
        autor=Autor.objects.get(id=1)
        self.assertEqual(autor.get_absolute_url(),'/libros/autor/1' )


