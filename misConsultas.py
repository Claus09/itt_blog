>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()

>>> b.name = 'Beatles Blog updated'
>>> b.save()

>>> from blog.models import Blog, Entry
>>> a = Entry.objects.get_or_create(blog_id=1,pub_date='2017-06-12', mod_date='2017-06-12',n_comments=1,n_pingbacks=1,rating=5)
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get_or_create(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()

>>> from blog.models import Author
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe)

>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
>>> entry.save()

>>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name='Foo', tagline='Bar')
>>> b.objects
Traceback:
    ...
AttributeError: "Manager isn't accessible via Blog instances."

>>> all_entries = Entry.objects.all()

>>> Entry.objects.filter(id=1)
<QuerySet [<Entry: >]>
>>> Entry.objects.all().filter(id=1)
<QuerySet [<Entry: >]>
(El titulo está vacío porque no se lleno esa propiedad pero el objeto existe, y tiene id = 1)

>>> from blog.models import Blog, Entry, datetime
>>> q1 = Entry.objects.filter(blog=1)
>>> q2 = q1.exclude(pub_date=datetime.date.today())
>>> q3 = q1.filter(pub_date=datetime.date.today())

>>> q = Entry.objects.filter(blog=1)
>>> q = q.filter(pub_date=datetime.date.today())
>>> q = q.exclude(body_text="food")
>>> print(q)
<QuerySet []>

>>> one_entry = Entry.objects.get(pk=1)
>>> one_entry
<Entry: >

>>> Entry.objects.all()[5:10]
>>> Entry.objects.all()[:10:2]
>>> Entry.objects.order_by('headline')[0]
>>> Entry.objects.order_by('headline')[0:1].get()
>>> Entry.objects.filter(pub_date=datetime.date.today())

>>> Entry.objects.filter(blog_id=4)
<QuerySet [<Entry: Test4>]>
(Sólo agregué titulos)

>>> Entry.objects.get(headline="Test4")
<Entry: Test4>

>>> Blog.objects.get(name__iexact="beatles blog updated")
<Blog: Beatles Blog updated>

>>> Blog.objects.filter(entry__headline__contains='Lennon')
>>> Blog.objects.filter(entry__authors__name='Lennon')
>>> Blog.objects.filter(entry__authors__name__isnull=True)
>>> Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)
>>> Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
>>> Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
(Realizan la misma operación pero con varias restricciones)

>>> Entry.objects.filter(n_comments=F('n_pingbacks'))
<QuerySet [<Entry: >]>
>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
>>> Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
>>> Entry.objects.filter(authors__name=F('blog__name'))
(Realizan la misma operación pero con distintas restricciones)

>>> from datetime import timedelta
>>> Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
>>> F('somefield').bitand(16)
(Permite buscar entradas que fueron modificadas tres días después)

>>> Blog.objects.get(id__exact=14)
>>> Blog.objects.get(id=14)
>>> Blog.objects.get(pk=14)
>>> Blog.objects.filter(pk__in=[1,4,7])
>>> Blog.objects.filter(pk__gt=14)
(Hacen lo mismo pero se escribe de distinta forma)

>>> Entry.objects.filter(headline__contains='test')
<QuerySet [<Entry: Test>, <Entry: Test2>, <Entry: Test3>, <
Entry: Test4>, <Entry: Test5>, <Entry: Test6>, <Entry: Test7>,
<Entry: Test8>, <Entry: Test9>, <Entry: Test10>]>

>>> from django.db.models import Q
>>> Q(question__startswith='What')
<Q: (AND: ('question__startswith', 'What'))>
(Operaciones complejas con un objeto Q)

>>> from blog.models import Blog, Entry
>>> a = Blog.objects.all()
>>> b = Entry.objects.all()
>>> a == b
False
(Comparaciones entre objetos)

>>> a.delete()
(14, {u'blog.Entry': 6, u'blog.Blog': 3, u'blog.Entry_authors': 5})
>>> b.delete()
(7, {u'blog.Entry': 7, u'blog.Entry_authors': 0})

>>> Entry.objects.all().delete()
(Elimina todos los objetos por completo)

>>> blog = Blog(name='My blog', tagline='Blogging is easy')
>>> blog.save()
>>> blog.pk = None
>>> blog.save()

>>> Entry.objects.filter(pub_date=datetime.date.today()).update(headline='Everything is the same')
>>> b = Blog.objects.get(pk=1)
>>> Entry.objects.all().update(blog=b)
>>> Entry.objects.select_related().filter(blog=b).update(headline='Everything is the same')
>>> Entry.objects.all().update(n_pingbacks=F('n_pingbacks') + 1)
(Realizan el mismo proceso de actualización pero con varias condiciones)



>>> Entry.objects.all().delete()
(Elimina todos los registros)

>>> e = Entry.objects.get(id=2)
>>> e.blog
>>> e = Entry.objects.get(id=2)
>>> e.blog = some_blog
>>> e.save()
>>> e = Entry.objects.get(id=2)
>>> e.blog = None
>>> e.save()
>>> e = Entry.objects.get(id=2)
>>> print(e.blog)
>>> e = Entry.objects.select_related().get(id=2)
>>> print(e.blog)
(Búsquedas y relaciones con la pk de una entrada usando un objeto)

>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all()
>>> b.entry_set.filter(headline__contains='Lennon')
>>> b.entry_set.count()
(Regresa un conteo de las entradas pertenecientes a un cierto blog x usando un llave)

>>> e = Entry.objects.get(id=3)
>>> e.authors.all()
>>> e.authors.count()
>>> e.authors.filter(name__contains='John')
>>> a = Author.objects.get(id=5)
>>> a.entry_set.all()
(Nos regresa a los autores asociados a una cierta entrada por medio de una llave)

>>> Entry.objects.filter(blog=blogobj)
<QuerySet []>
>>> Entry.objects.filter(blog=blogobj.id)
<QuerySet []>
>>> Entry.objects.filter(blog=1)
<QuerySet [<Entry: How to create a blog form terminal>]>
>>> Entry.objects.filter(blog=2)
<QuerySet []>
>>> Entry.objects.filter(blog=1)
<QuerySet [<Entry: How to create a blog form terminal>]>
>>>
(Se realiza la misma operación pero se escribe diferente)
##NOTA: Las evidencias de imagenes y pantallazos están en google drive
